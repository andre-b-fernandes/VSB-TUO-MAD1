import random
import math
import pandas

#Assuming same dimension
def euclidean_distance(first_tuple, second_tuple):
    return math.sqrt(sum(map(lambda first_value, second_value: (first_value -second_value)**2 , first_tuple, second_tuple)))

class K_Means_Clustering:
    def __init__(self, df, k):
        self.data_frame = df
        self.number_of_klusters = k

    def k_means_algorithm(self):
        centroids = self.generate_initial_centroids()
        clusters = self.calculate_clusters_for_centroids(centroids)
        old_centroids = pandas.DataFrame()
        while not(old_centroids.equals(centroids)):
            old_centroids = centroids
            clusters = self.calculate_clusters_for_centroids(centroids)
            centroids = self.calculate_centroids_for_clusters(clusters)
        return centroids, clusters
        
    def generate_initial_centroids(self):
        return self.data_frame.sample(n=self.number_of_klusters)

    def calculate_clusters_for_centroids(self, centroids):
        clusters = [[] for i in range(0, self.number_of_klusters)]
        for i in range(0, len(self.data_frame)):
            distances = []
            for k in range(0, len(centroids)):
                distances.append(euclidean_distance(tuple(self.data_frame.iloc[i]), tuple(centroids.iloc[k])))
            clusters[distances.index(min(distances))].append(self.data_frame.iloc[i])
        return list(map(lambda cluster: pandas.DataFrame(cluster), clusters ))
    
    def calculate_centroids_for_clusters(self, clusters):
        return pandas.DataFrame(map(self.calculate_centroid_for_cluster, clusters))

    def calculate_centroid_for_cluster(self, cluster):
        return cluster.mean(axis=0)