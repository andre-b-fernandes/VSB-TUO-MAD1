import csv,sys
from matplotlib import pyplot as plt

class Graph:
    def __init__(self, data):
        self.matrix = self.calculate_adjecency_matrix(data)
        self.node_degree = self.calculate_node_degree()

    def calculate_adjecency_matrix(self, data):
        number_of_nodes = int(data[len(data) - 1][0])
        matrix = [ [ 0 for i in range(number_of_nodes) ] for j in range(number_of_nodes) ]
        for row in data:
            row_node_number = int(row[0]) - 1
            col_node_number = int(row[1]) - 1
            matrix[row_node_number][col_node_number] = 1
            matrix[col_node_number][row_node_number] = 1
        return matrix

    def calculate_node_degree(self):
        node_degree = []
        for row in self.matrix:
            count = sum(row)
            node_degree.append(count)
        return node_degree
    
    def print_matrix(self):
        print("\r\n\t\t\t\t\tAdjacency Matrix\r\n")
        for row in self.matrix:
            for col in row:
                print(str(col) + "  ", end='')
            print("")
        print("\r\n\t\t\t\t\t\tEND\r\n")

    def print_node_degree(self):
        for degree in self.node_degree:
            print(str(degree))
    
    def max_degree(self):
        node_degree = sorted(self.node_degree)
        return node_degree[len(node_degree) - 1]

    def min_degree(self):
        node_degree = sorted(self.node_degree)
        return node_degree[0]

    def mean_degree(self):
        sum_degree = 0
        for degree in self.node_degree:
            sum_degree += degree
        return sum_degree/len(self.node_degree)
    
    def print_degree_information(self):
        print("\r\n\t\tDegree Information\r\n")
        max_degree = self.max_degree()
        min_degree = self.min_degree()
        mean_degree = self.mean_degree()
        print("\t\tMax degree:\t" + str(max_degree) )
        print("\t\tMin degree:\t" + str(min_degree) )
        print("\t\tMean degree:\t" + str(mean_degree) )
        print("\r\n\t\tEND\r\n")
    
    def show_histogram(self):
        plt.hist([self.node_degree], color=['red'])
        plt.xlabel("# degree")
        plt.ylabel("# of nodes")
        plt.title("Frequency distribution")
        plt.show()

       
def read_file(file_name):
    data = []
    with open(file_name, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        for row in csv_reader:
            data.append(row)
    return data


data = read_file('KarateClub.csv')

graph = Graph(data)
graph.print_matrix()
graph.print_degree_information()
graph.show_histogram()