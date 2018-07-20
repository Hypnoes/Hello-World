import tensorflow as tf
import numpy as np

from numpy import random

def create_samples(n_clusters, n_samples_per_cluster, n_features, embiggen_factor, seed):
    random.seed(seed)
    slices = []
    centroids = []

    for i in range(n_clusters):
        samples = tf.random_normal((n_samples_per_cluster, n_features),
                                   mean=0.0, stddev=5.0, dtype=tf.float32, seed=seed, name=f'cluster_{i}')
        current_centroid = (random.random((1, n_features)) * embiggen_factor) - (embiggen_factor/2)
        centroids.append(current_centroid)
        samples += current_centroid
        slices.append(samples)

    # Create a big "sample" dataset
    samples = tf.concat(slices, 0, name='samples')
    centroids = tf.concat(centroids, 0, name='controids')
    return centroids, samples

def plot_cluster(all_samples, centroids, n_samples_per_cluster):
    import matplotlib.pyplot as plt
    # Plot out the different clusters
    # Choose a different color for each cluster
    color = plt.cm.rainbow(np.linspace(0, 1, len(centroids)))
    for i, centroid in enumerate(centroids):
        # Grab just the samples fpr the given cluster and plot them out with a new color
        samples = all_samples[i * n_samples_per_cluster : (i + 1) * n_samples_per_cluster]
        plt.scatter(samples[:, 0], samples[:, 1], c=color[i])
        # Also plot centroid
        plt.plot(centroid[0], centroid[1], marksize=32, marker='x', color='k', mew=10)
        plt.plot(centroid[0], centroid[1], marksize=28, marker='x', color='m', mew=5)
    plt.show()

if __name__ == '__main__':
    n_features = 2
    n_clusters = 3
    n_samples_per_cluster = 500
    seed = 700
    embiggen_factor = 70

    random.seed(seed)

    centroids, samples = create_samples(n_clusters, n_samples_per_cluster,
                                        n_features, embiggen_factor, seed)

    model = tf.global_variables_initializer()
    with tf.Session() as session:
        sample_values = session.run(samples)
        centroid_values = session.run(centroids)

        plot_cluster(sample_values, centroid_values, n_samples_per_cluster)
