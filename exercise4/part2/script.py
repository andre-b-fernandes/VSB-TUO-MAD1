import pandas, numpy, matplotlib.pyplot as plt

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

def plot_frequency_bar_char(unique_column, freq,  y_label):
    plt.figure()
    plt.bar(unique_column, freq, align='center', width=0.2, edgecolor='red', color='white')
    plt.xlabel("Attribute Values")
    plt.ylabel(y_label)
    plt.title(attribute)



data = pandas.read_csv('iris.csv', sep=';')
attributes = list(data.columns)

for attribute in attributes[0:len(attributes) - 1]:
    corrected_column = correct_column(data[attribute])
    unique_column,freq = calculate_frequencies(corrected_column)
    plot_frequency_bar_char(unique_column, freq, "Attribute Frequency")
    relative_frequencies = calculate_relative_frequencies(freq)
    plot_frequency_bar_char(unique_column, relative_frequencies, "Attribute Relative Frequency")
    cumulative_frequencies = calculate_acumulative_frequencies(relative_frequencies)
    plot_frequency_bar_char(unique_column, cumulative_frequencies, "Attribute Cumulative Frequencies")


plt.show()

