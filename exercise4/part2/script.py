import math, pandas, numpy, matplotlib.pyplot as plt

def calculate_frequencies(column):
    unique, counts = numpy.unique(column, return_counts=True)
    return unique,counts

def calculate_relative_frequencies(frequencies):
    total = sum(frequencies)
    return numpy.array(list(map(lambda freq : freq/total, frequencies)))

def calculate_acumulative_frequencies(frequencies):
    return numpy.cumsum(frequencies)

def correct_column(column):
    return numpy.sort(numpy.array(list(map(lambda str : str.replace(",", "."), column))).astype(numpy.float))

def plot_scatter_plot(unique_column, freq,  y_label):
    plt.figure()
    plt.scatter(unique_column, freq)
    plt.xlabel("Attribute Values")
    plt.ylabel(y_label)
    plt.title(attribute)

def calculate_mean(column):
    return sum(column)/len(column)

def calculate_variance(column, mean):
    variances = numpy.array(list(map(lambda value: (value - mean)*(value - mean), column)))
    return sum(variances)/len(variances)

def calculate_theoretical_frequencies(column):
    mean = calculate_mean(column)
    variance = calculate_variance(column, mean)
    return  numpy.array(list(map( lambda value: (1/math.sqrt(2*math.pi*variance)) * math.exp(- (value - mean) * (value - mean) / (2*variance)), column)))
    

data = pandas.read_csv('iris.csv', sep=';')
attributes = list(data.columns)

for attribute in attributes[0:len(attributes) - 1]:
    corrected_column = correct_column(data[attribute])
    unique_column,freq = calculate_frequencies(corrected_column)
    plot_scatter_plot(unique_column, freq, "Attribute Frequency")
    relative_frequencies = calculate_relative_frequencies(freq)
    plot_scatter_plot(unique_column, relative_frequencies, "Attribute Relative Frequency")
    cumulative_frequencies = calculate_acumulative_frequencies(relative_frequencies)
    plot_scatter_plot(unique_column, cumulative_frequencies, "Attribute Cumulative Frequencies")
    theoretical_frequencies = calculate_theoretical_frequencies(unique_column)
    plot_scatter_plot(unique_column, theoretical_frequencies, "Attribute Theoretical Frequencies")


plt.show()