# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['graph_partition',
 'graph_partition.evaluation_metric',
 'graph_partition.gcn',
 'graph_partition.k_means',
 'graph_partition.spectral_clustering']

package_data = \
{'': ['*']}

install_requires = \
['k-means-constrained==0.7.1',
 'numpy==1.23.1',
 'scikit-learn==1.1.1',
 'scipy>=1.8.1,<2.0.0',
 'torch==1.12.0']

setup_kwargs = {
    'name': 'graph-partition',
    'version': '0.1.1',
    'description': 'Graph partitioning Algorithms',
    'long_description': '# Graph Partitioning\nGraph Partitioning is an age-old problem with applications in various domains, such as \nrouting vehicles for delivery and finding the right target for immunizations to control a \npandemic. Graph Convolution Networks (GCN) employ deep learning techniques to solve the \nproblem of graph partitioning.\n\n# Installation\nYou can install the graph-partition from PyPI:\n```shell\npip install graph-partition\n```\n\n# How to Use\nPrimarily there are three major algorithms are there\n- Graph Convolutional Neural Network\n- Spectral Clustering\n- Constrained K-Means Clustering\n\n### Using of Graph Convolutional Network\n```python\nimport urllib.request\nfrom scipy.spatial import distance_matrix\n\n```',
    'author': 'somsubhra88',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<3.11',
}


setup(**setup_kwargs)
