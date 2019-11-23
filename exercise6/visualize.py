import matplotlib.pyplot as plt

def plot_clusters_2d(x_values, x_label, y_values, y_label):
    colors = [(0,0,0)]
    plt.figure()
    plt.scatter(x_values, y_values, c=colors)
    plt.title('Clusters')
    plt.xlabel(x_label)
    plt.ylabel(y_label)

def show():
    plt.show()