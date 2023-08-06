import urllib.request
from scipy.spatial import distance_matrix

from gcn.graphConvolutionNetwork import (
    GraphConvolutionNetwork,
)
from k_means.k_means import ConstrainedKMeans
from spectral_clustering.spectral_clustering import SpectralClustering

if __name__ == "__main__":
    url = "https://cs.joensuu.fi/sipu/datasets/s1.txt"
    data = urllib.request.urlopen(url)
    ds = []
    for line in data:
        ds.append([float(x) for x in line.strip().split()])

    _cost_matrix = distance_matrix(ds[:50], ds[:50])

    _gcn_model = GraphConvolutionNetwork(
        cost_matrix=_cost_matrix, num_class=2, hidden_layers=10
    )
    _gcn_model.fit()
    print(_gcn_model.cluster_label)
    print(_gcn_model.evaluation_metric)

    _sc_model = SpectralClustering(cost_matrix=_cost_matrix, num_class=2)
    print(_sc_model.cluster_label)
    print(_sc_model.evaluation_metric)

    _k_means_model = ConstrainedKMeans(
        design_matrix=ds[:50], num_class=2, evaluate_metric=True
    )
    print(_k_means_model.cluster_label)
    print(_k_means_model.evaluation_metric)
