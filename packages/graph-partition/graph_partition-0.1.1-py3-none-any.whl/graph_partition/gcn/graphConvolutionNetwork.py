import torch
from torch import from_numpy, Tensor
import numpy as np
from typing import Union, List, Dict, Any

from graph_partition.evaluation_metric.evaluate_metric import evaluate_clustering_metrics
from graph_partition.gcn.buildGraphConvolution import BuildGraphConvolution


class GraphConvolutionNetwork:
    __early_stopping_round__ = 10000
    __tolerance__ = 1e-04

    def __init__(
        self,
        cost_matrix: np.ndarray,
        num_class: int,
        hidden_layers: Union[List[int], int],
        feature_matrix: np.ndarray = None,
        learning_rate: float = 0.0001,
        use_learning_rate_scheduler: bool = False,
        l2_penalty: float = 0,
        imbalance_loss_factor: float = 1,
        continuous_relaxation_factor: float = 1,
        dropout_rate: float = 0.1,
        epoch: int = 20000,
    ):
        # Identifying the device
        self._device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        print(f"{self._device} will be used for computation \n")

        self.cost_matrix = from_numpy(cost_matrix.astype(np.float64)).to(self._device)
        self.adjacency_matrix = self.get_adjacency_matrix()
        # Calculation of feature matrix, if nodes doesn't have any features/signals then we can simply use an identity matrix
        if feature_matrix is None:
            self.feature_matrix = from_numpy(
                np.eye(self.cost_matrix.shape[0]).astype(np.float64)
            ).to(self._device)
        else:
            self.feature_matrix = from_numpy(feature_matrix.astype(np.float64)).to(
                self._device
            )
        # Hidden Layers
        if isinstance(hidden_layers, int):
            self.hidden_layers = [hidden_layers]
        else:
            self.hidden_layers = hidden_layers

        # User inputs number of vehicles
        self.num_class = num_class
        # Use of Scheduler
        self.scheduler = use_learning_rate_scheduler
        #  initial learning rate
        self.learning_rate = learning_rate
        # Weight decay parameter
        self.l2_penalty = l2_penalty
        # Cluster imbalance loss
        self.imbalance_loss_factor = imbalance_loss_factor
        # Continuous loss factor to make softmax out put to more towards binary
        self.continuous_relaxation_factor = continuous_relaxation_factor
        # Dropout Rate as regularization
        self.dropout_rate = dropout_rate

        # Use of actual cost means the actual assignment of classes rather than using the expected cost
        self._best_class_list = None

        # Number of Epochs
        self.epoch = epoch

        # Building the model
        self._gcn_model = BuildGraphConvolution(
            adjacency_matrix=self.adjacency_matrix,
            num_features=self.feature_matrix.shape[1],
            num_class=num_class,
            hidden_layers=self.hidden_layers,
            dropout_rate=self.dropout_rate,
        )

        # Defining the Optimizer
        self._optimizer = torch.optim.Adam(
            self._gcn_model.parameters(),
            lr=self.learning_rate,
            weight_decay=self.l2_penalty,
        )

        # learning rate Scheduler
        self._scheduler = torch.optim.lr_scheduler.StepLR(
            self._optimizer, step_size=int(self.epoch / 5), gamma=0.1
        )

        # Actual predictions from the network
        self.cluster_label: List = []
        self.evaluation_metric: Dict[str, Any] = {}

    def fit(self):
        loss_list = []
        _min_loss = 1e09
        _normalized_cost_matrix = np.array(self.cost_matrix) / np.sum(
            np.array(self.cost_matrix)
        )
        _normalized_cost_matrix = from_numpy(_normalized_cost_matrix).to(self._device)

        for e in range(self.epoch):
            # Forward pass
            _output = self._gcn_model(self.feature_matrix)

            # Number of nodes
            N = _output.shape[0]
            M = _output.shape[1]
            # Partition loss
            _loss1 = torch.sum(
                torch.diagonal(
                    torch.matmul(
                        torch.matmul(_output.T, _normalized_cost_matrix), _output
                    )
                )
            )

            # Cluster imbalance loss
            _loss2 = torch.sum(torch.square(torch.sum(_output, dim=0)))
            _max_loss2, _min_loss2 = N**2, N**2 / M
            _scaling_factor = _max_loss2 - _min_loss2
            _loss2 = (_loss2 - _min_loss2) / _scaling_factor

            # Continuous Relaxation: it's value is ranging from [1, M]
            _loss3 = M * torch.sum(torch.square(_output)) / N

            _loss = (
                _loss1
                + self.imbalance_loss_factor * _loss2
                + self.continuous_relaxation_factor / _loss3
            )

            # Back Propagation and Weights Update
            self._optimizer.zero_grad()
            _loss.backward()
            self._optimizer.step()
            if self.scheduler:
                self._scheduler.step()

            loss_list.append(_loss.item())
            _min_loss = _loss.item() if _loss.item() < _min_loss else _min_loss
            # Verbose
            if (e + 1) % 1000 == 0:
                print(
                    "Epoch [{}/{}], "
                    "Total Loss: {:.6f}, "
                    "Partitioning Cost {:.6f}, "
                    "Imbalance cost {:.6f}, "
                    "Continuous Relaxation cost {:.6f}".format(
                        e + 1,
                        self.epoch,
                        loss_list[-1],
                        _loss1,
                        self.imbalance_loss_factor * _loss2,
                        self.continuous_relaxation_factor / _loss3,
                    )
                )
            # Early stopping
            if self.early_stopping(loss_list, _min_loss):
                print(
                    "Epoch [{}/{}], "
                    "Total Loss: {:.6f}, "
                    "Partitioning Cost {:.6f}, "
                    "Imbalance cost {:.6f}, "
                    "Continuous Relaxation cost {:.6f}".format(
                        e + 1,
                        self.epoch,
                        loss_list[-1],
                        _loss1,
                        self.imbalance_loss_factor * _loss2,
                        self.continuous_relaxation_factor / _loss3,
                    )
                )
                print("Model can't be improved further")
                break
        # Training is completed now predicting the class labels
        self.cluster_label = self.predict()
        self.evaluation_metric = evaluate_clustering_metrics(
            self.cost_matrix.numpy().tolist(), self.cluster_label
        )

    def predict(self, X: Tensor = None) -> List:
        if X is None:
            X = self.feature_matrix

        _predict = self._gcn_model(X.to(self._device))
        _, _class = torch.max(_predict.data, 1)
        _cluster_label = _class.to("cpu").numpy().tolist()

        return _cluster_label

    def early_stopping(self, loss_list: list, min_loss: float) -> bool:
        if len(loss_list) < 10 + self.__early_stopping_round__:
            return False
        else:
            if all([x > min_loss for x in loss_list[-self.__early_stopping_round__ :]]):
                return True
            else:
                return False

    def get_adjacency_matrix(self, threshold: float = 0.1):
        N = len(self.cost_matrix)
        # Converting it to numpy array
        _cost_matrix = np.array(self.cost_matrix)
        # will convert it to symmetric matrix
        _cost_matrix = 0.5 * (_cost_matrix + _cost_matrix.T)
        _adjacency_matrix = np.zeros((N, N))
        _degree_matrix_inv_sqrt = np.zeros((N, N))
        for i in range(N):
            _cost_threshold = max(500, np.quantile(_cost_matrix[i], threshold))
            for j in range(N):
                if i == j or _cost_matrix[i][j] <= _cost_threshold:
                    _adjacency_matrix[i, j] = 1
            # Degree Matrix diagonal entry is the sum of that row
            _degree_matrix_inv_sqrt[i, i] = 1 / np.sqrt(_adjacency_matrix[i].sum())

        # Normalizing the adjacency matrix
        _adjacency_matrix_transformed = np.matmul(
            np.matmul(_degree_matrix_inv_sqrt, _adjacency_matrix),
            _degree_matrix_inv_sqrt,
        )

        return from_numpy(_adjacency_matrix_transformed.astype(np.float64)).to(
            self._device
        )
