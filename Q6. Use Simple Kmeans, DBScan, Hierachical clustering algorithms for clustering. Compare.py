# Q6. Use Simple Kmeans, DBScan, Hierachical clustering algorithms for clustering. Compare
# the performance of clusters by changing the parameters involved in the algorithms.
# Code :
from sklearn.cluster import KMeans, DBSCAN, AgglomerativeClustering
from sklearn.datasets import load_iris
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt

# Load the Iris dataset
iris = load_iris()
X, y = iris.data, iris.target
# Define clustering algorithms
algorithms = {
'KMeans': KMeans(),
'DBSCAN': DBSCAN(),
'Hierarchical': AgglomerativeClustering()
}
# Initialize parameters for different algorithms
parameters = {
'KMeans': range(2, 6), # Try number of clusters from 2 to 5
'DBSCAN': [0.1, 0.5, 1.0], # Try different eps values
'Hierarchical': ['ward', 'complete', 'average', 'single']
}
# Iterate over each clustering algorithm
for algorithm_name, algorithm in algorithms.items():
print(f"Clustering algorithm: {algorithm_name}")
# Try different parameters for the algorithm
for param in parameters[algorithm_name]:
if algorithm_name == 'DBSCAN':
cluster_labels = algorithm.fit_predict(X)
elif algorithm_name == 'Hierarchical':
cluster_labels = algorithm.fit_predict(X)
else: # KMeans
cluster_labels = algorithm.set_params(n_clusters=param).fit_predict(X)
# Evaluate the clustering performance using silhouette score

17

silhouette_avg = silhouette_score(X, cluster_labels)
print(f"- Parameters: {param}, Silhouette Score: {silhouette_avg:.4f}")
# Plot the clusters for visualization
if algorithm_name == 'KMeans':
plt.scatter(X[:, 0], X[:, 1], c=cluster_labels, cmap='viridis')
plt.title(f'KMeans Clustering with {param} clusters')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.show()