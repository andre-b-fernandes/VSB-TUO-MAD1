import pandas
from k_means_clustering import K_Means_Clustering
from visualize import plot_clusters_2d,show

data_frame = pandas.read_csv("iris.csv", sep=";")
df = data_frame.drop('Species', axis=1)

for column in df.columns.to_list():
    df[column] = df[column].str.replace(",", ".").astype(float)

k_means_wrapper = K_Means_Clustering(df, 2)
centroids, clusters = k_means_wrapper.k_means_algorithm()

sepal_centroids = centroids[["Sepal.Length","Sepal.Width"]]

petal_centroids = centroids[["Petal.Length","Petal.Width"]]

plot_clusters_2d(clusters, sepal_centroids, "Sepal.Length", "Sepal.Width")
plot_clusters_2d(clusters, petal_centroids, "Petal.Length", "Petal.Width")

show()