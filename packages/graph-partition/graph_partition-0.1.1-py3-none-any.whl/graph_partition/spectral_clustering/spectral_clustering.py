from typing import List
import numpy as np

from graph_partition.evaluation_metric.evaluate_metric import evaluate_clustering_metrics
from k_means.k_means import ConstrainedKMeans


class SpectralClustering:
    def __init__(self, cost_matrix: List[List], num_class: int):
        self.cost_matrix = cost_matrix
        self.number_of_clusters = num_class
        self.cluster_label = self.cluster()
        self.evaluation_metric = evaluate_clustering_metrics(
            self.cost_matrix, self.cluster_label
        )

    def transform(self):
        _cost_matrix = np.array(self.cost_matrix)
        _cost_matrix = (_cost_matrix + _cost_matrix.T) / 2
        _row_sum = _cost_matrix.sum(axis=1)
        _normalized_cost_matrix = _cost_matrix / _row_sum[:, np.newaxis]
        return _normalized_cost_matrix

    def cluster(self):
        _cost_matrix = self.transform()
        _eigen_values, _eigen_vectors = np.linalg.eig(_cost_matrix)
        # Sanity Check: to avoid the complex numbers in eigen decomposition
        _eigen_values = np.real_if_close(_eigen_values, tol=1)
        _eigen_vectors = np.real_if_close(_eigen_vectors, tol=1)
        assert (
            np.abs(_eigen_values[0] - 1) < 1e-06
        ), f"First Eigen Value is not equal to 1, it is {round(_eigen_values[0], 4)}"
        # Discard the first eigen vector
        _k_means_model = ConstrainedKMeans(
            _eigen_vectors[:, 1:], num_class=self.number_of_clusters
        )

        # kmeans = KMeans(n_clusters=self.number_of_clusters, random_state=0).fit(
        #     _eigen_vectors[:, 1:]
        # )
        return _k_means_model.cluster_label

    # def __evaluate_clustering__(self) -> Dict[str, Any]:
    #     # Calculating the actual cost and other metrics
    #     _actual_cost = GetClusteringCost(self.cost_matrix, self.cluster_label)
    #     _arm = GetAgreementRateMetric(self.cost_matrix, self.cluster_label)
    #     _dia = GetClusterDiameter(self.cost_matrix, self.cluster_label)
    #     _min_cluster, _max_cluster, _cif = measure_cluster_imbalance(self.cluster_label)
    #     _evaluation_metrics = {
    #         "cost": round(_actual_cost.cost, 4),
    #         "ARM": _arm.ARM,
    #         "Cluster Diameters": _dia.cluster_diameters,
    #         "Cluster Imbalance Factor": round(_cif, 4),
    #         "Min Cluster Size": _min_cluster,
    #         "Max Cluster Size": _max_cluster,
    #     }
    #
    #     return _evaluation_metrics
