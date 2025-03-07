import numpy as np


def k_means(X, k, max_iters=100, tol=1e-4):
    n_samples, n_features = X.shape

    indices = np.random.choice(n_samples, k, replace=False)
    centroids = X[indices]

    for iteration in range(max_iters):
        distances = np.linalg.norm(X[:, np.newaxis] - centroids, axis=2)

        labels = np.argmin(distances, axis=1)

        new_centroids = np.zeros_like(centroids)
        for j in range(k):
            points_in_cluster = X[labels == j]
            if len(points_in_cluster) > 0:
                new_centroids[j] = np.mean(points_in_cluster, axis=0)
            else:
                new_centroids[j] = centroids[j]

        if np.linalg.norm(new_centroids - centroids) < tol:
            print(f"Сходимость достигнута на итерации {iteration}")
            break

        centroids = new_centroids

    return labels, centroids


if __name__ == "__main__":
    np.random.seed(42)
    X = np.random.randn(300, 2)

    labels, centroids = k_means(X, k=3)
    print("Итоговые центроиды:")
    print(centroids)
