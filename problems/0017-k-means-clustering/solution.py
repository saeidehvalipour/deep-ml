from typing import List, Tuple
import numpy as np

def k_means_clustering(points: List[Tuple[float, ...]],
                       k: int,
                       initial_centroids: List[Tuple[float, ...]],
                       max_iterations: int) -> List[Tuple[float, ...]]:

    X = np.array(points, dtype=float)
    centroids = np.array(initial_centroids, dtype=float)

    for _ in range(max_iterations):

        # Assignment step
        distances = np.sum((X[:, None, :] - centroids[None, :, :]) ** 2, axis=2)
        labels = np.argmin(distances, axis=1)

        # Update step
        new_centroids = centroids.copy()
        for j in range(k):
            cluster_points = X[labels == j]
            if len(cluster_points) > 0:
                new_centroids[j] = cluster_points.mean(axis=0)

        # Convergence check
        if np.allclose(new_centroids, centroids):
            centroids = new_centroids
            break

        centroids = new_centroids

    final_centroids = [tupl