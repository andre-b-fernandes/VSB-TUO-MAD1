import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

def plot_clusters_2d(clusters, centroids, x_label, y_label):
    plt.figure()
    
    colors = cm.rainbow(np.linspace(0, 1, len(centroids)))
    for i in range(0, len(centroids)):
        plt.plot(centroids.iloc[i][x_label], centroids.iloc[i][y_label], 'kx')
    
    for i in range(0,len(clusters)):
        plt.scatter(clusters[i][x_label], clusters[i] [y_label], c=colors[i])

    plt.title('Clusters')
    plt.xlabel(x_label)
    plt.ylabel(y_label)

def show():
    plt.show()