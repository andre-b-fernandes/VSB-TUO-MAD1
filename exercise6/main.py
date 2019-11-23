import pandas
from k_means_clustering import K_Means_Clustering
from visualize import plot_clusters_2d,show

def parse_axis_values(x_column, y_column, clusters):
    x_values = []
    y_values = []
    for cluster in clusters:
        x_values += list(cluster[x_column])
        y_values += list(cluster[y_column])
    return x_values, y_values


data_frame = pandas.read_csv("iris.csv", sep=";")
df = data_frame.drop('Species', axis=1)

for column in df.columns.to_list():
    df[column] = df[column].str.replace(",", ".").astype(float)

k_means_wrapper = K_Means_Clustering(df, 3)
centroids, clusters = k_means_wrapper.k_means_algorithm()

sepal_x_values, sepal_y_values = parse_axis_values("Sepal.Length", "Sepal.Width", clusters)
petal_x_values, petal_y_values = parse_axis_values("Petal.Length", "Petal.Width", clusters)

plot_clusters_2d(sepal_x_values, "Sepal Length", sepal_y_values, "Sepal Width")
plot_clusters_2d(petal_x_values, "Petal Length", petal_y_values, "Petal Width")

show()