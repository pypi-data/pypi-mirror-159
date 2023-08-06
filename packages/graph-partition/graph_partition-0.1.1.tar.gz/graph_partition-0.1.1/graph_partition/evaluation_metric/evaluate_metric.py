from typing import List

from evaluation_metric.cluster_imbalance import measure_cluster_imbalance
from evaluation_metric.getAgreementRateMetric import GetAgreementRateMetric
from evaluation_metric.getClusterDiameter import GetClusterDiameter
from evaluation_metric.getClusteringCost import GetClusteringCost


def evaluate_clustering_metrics(cost_matrix: List[List], class_label: List):
    # Calculating the actual cost and other metrics
    _actual_cost = GetClusteringCost(cost_matrix, class_label)
    _arm = GetAgreementRateMetric(cost_matrix, class_label)
    _dia = GetClusterDiameter(cost_matrix, class_label)
    _min_cluster, _max_cluster, _cif = measure_cluster_imbalance(class_label)
    _evaluation_metrics = {
        "cost": round(_actual_cost.cost, 4),
        "ARM": _arm.ARM,
        "Cluster Diameters": _dia.cluster_diameters,
        "Cluster Imbalance Factor": round(_cif, 4),
        "Min Cluster Size": _min_cluster,
        "Max Cluster Size": _max_cluster,
    }
    return _evaluation_metrics
