import numpy as np
np.random.seed(123)
from dyneusr import DyNeuGraph
from dyneusr.datasets import make_trefoil
from kmapper import KeplerMapper
from sklearn.decomposition import PCA

# Generate synthetic dataset
import tadasets
X = tadasets.sphere(n=500, r=1)

# Sort by first column
inds = np.argsort(X[:, 0])
X = X[inds].copy()
y = np.arange(X.shape[0])

# Generate shape graph using KeplerMapper
mapper = KeplerMapper(verbose=1)
lens = mapper.fit_transform(X, projection=PCA(2))
graph = mapper.map(lens, X, nr_cubes=6, overlap_perc=0.5)

# Visualize the shape graph using DyNeuSR's DyNeuGraph 
dG = DyNeuGraph(G=graph, y=y)
dG.visualize('dyneusr_sphere.html', static=True, show=True)

# Visualize the shape graph using DyNeuSR's DyNeuGraph 
dG = DyNeuGraph(G=graph, y=y)
dG.visualize('dyneusr2D_sphere.html', template='2D', static=True, show=True)

# Visualize the shape graph using DyNeuSR's DyNeuGraph 
dG = DyNeuGraph(G=graph, y=y)
dG.visualize('dyneusr3D_sphere.html', template='3D', static=True, show=True)

# Visualize the shape graph using DyNeuSR's DyNeuGraph 
dG = DyNeuGraph(G=graph, y=y)
dG.visualize('dyneusr4D_sphere.html', template='4D', static=True, show=True)

