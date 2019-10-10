import math
import pandas

def parse_row(row):
    return float(row['Sepal.Length'].replace(',', '.')), float(row['Sepal.Width'].replace(',', '.')), float(row['Petal.Length'].replace(',', '.')), float(row['Petal.Width'].replace(',', '.'))

def calculate_cosine_similarity(first_row, second_row):
    f_sep_len, f_sep_wid, f_pet_len, f_pet_wid = parse_row(first_row)
    s_sep_len, s_sep_wid, s_pet_len, s_pet_wid = parse_row(second_row)
    
    dot_product = f_sep_len*s_sep_len + f_sep_wid*s_sep_wid + f_pet_len*s_pet_len + f_pet_wid*s_pet_wid
    norm_first = math.sqrt(f_sep_len*f_sep_len + f_sep_wid*f_sep_wid + f_pet_len*f_pet_len + f_pet_wid*f_pet_wid)
    norm_second = math.sqrt(s_sep_len*s_sep_len + s_sep_wid*s_sep_wid + s_pet_len*s_pet_len + s_pet_wid*s_pet_wid)

    return round(dot_product/(norm_first * norm_second), 3)

def calculate_euclidean_distance(first_row, second_row):
    f_sep_len, f_sep_wid, f_pet_len, f_pet_wid = parse_row(first_row)
    s_sep_len, s_sep_wid, s_pet_len, s_pet_wid = parse_row(second_row)

    sep_len_term = (f_sep_len - s_sep_len)*(f_sep_len - s_sep_len)
    sep_wid_term = (f_sep_wid - s_sep_wid)*(f_sep_wid - s_sep_wid)
    pet_len_term = (f_pet_len - s_pet_len)*(f_pet_len - s_pet_len)
    pet_wid_term = (f_pet_wid - s_pet_wid)*(f_pet_wid - s_pet_wid)
    
    return round(math.sqrt( sep_len_term + sep_wid_term + pet_len_term + pet_wid_term),3)

def calculate_mean(value, total):
    return round(value/total,3)

def calculate_median(column, total):
    index = (total + 1)/2
    if index % 2 == 0:
        return column[index]
    else:
        floor = float(column[math.floor(index)].replace(',','.'))
        ceiling = float(column[math.ceil(index)].replace(',','.'))
        return round((floor + ceiling)/2,3)

def calculate_standard_deviation(variance):
    return round(math.sqrt(variance),3)

data = pandas.read_csv("iris.csv", sep=';')

row_iterator = data.iterrows()
_, last = next(row_iterator)  # take first item from row_iterator

print("\n")
print("Rows\t\tCosine Similarity\tEuclidean Distance")

sep_len_total = float(last['Sepal.Length'].replace(',', '.'))
sep_wid_total = float(last['Sepal.Width'].replace(',', '.'))
pet_len_total = float(last['Petal.Length'].replace(',', '.'))
pet_wid_total = float(last['Petal.Width'].replace(',', '.'))

for i, row in row_iterator:
    cosine_similarity = calculate_cosine_similarity(last, row) 
    euclidean_distance = calculate_euclidean_distance(last, row)
    
    print(str(i - 1) + "/" + str(i) + "\t\t" + str(cosine_similarity) + "\t\t\t" + str(euclidean_distance))

    sep_len_total += float(row['Sepal.Length'].replace(',', '.'))
    sep_wid_total += float(row['Sepal.Width'].replace(',', '.'))
    pet_len_total += float(row['Petal.Length'].replace(',', '.'))
    pet_wid_total += float(row['Petal.Width'].replace(',', '.'))

    last = row

sep_len_mean = calculate_mean(sep_len_total, len(data))
sep_wid_mean = calculate_mean(sep_wid_total, len(data))
pet_len_mean = calculate_mean(pet_len_total, len(data))
pet_wid_mean = calculate_mean(pet_wid_total, len(data))

row_iterator = data.iterrows()

sep_len_variance = 0
sep_wid_variance = 0
pet_len_variance = 0
pet_wid_variance = 0

for i, row in row_iterator:
    sep_len_variance +=  (float(row['Sepal.Length'].replace(',', '.')) - sep_len_mean) * (float(row['Sepal.Length'].replace(',', '.')) - sep_len_mean)
    sep_wid_variance +=  (float(row['Sepal.Width'].replace(',', '.')) - sep_wid_mean) * (float(row['Sepal.Width'].replace(',', '.')) - sep_wid_mean)
    pet_len_variance +=  (float(row['Petal.Length'].replace(',', '.')) - pet_len_mean) * (float(row['Petal.Length'].replace(',', '.')) - pet_len_mean)
    pet_wid_variance +=  (float(row['Petal.Width'].replace(',', '.')) - pet_wid_mean) * (float(row['Petal.Width'].replace(',', '.')) - pet_wid_mean)

sep_len_total_variance = calculate_mean(sep_len_variance, len(data))
sep_wid_total_variance = calculate_mean(sep_wid_variance, len(data))
pet_len_total_variance = calculate_mean(pet_len_variance, len(data))
pet_wid_total_variance = calculate_mean(pet_wid_variance, len(data))

sep_len_median = calculate_median(data.sort_values(by=['Sepal.Length'])['Sepal.Length'], len(data))
sep_wid_median = calculate_median(data.sort_values(by=['Sepal.Width'])['Sepal.Width'], len(data))
pet_len_median = calculate_median(data.sort_values(by=['Petal.Length'])['Petal.Length'], len(data))
pet_wid_median = calculate_median(data.sort_values(by=['Petal.Width'])['Petal.Width'], len(data))

sep_len_standard_deviation = calculate_standard_deviation(sep_len_total_variance)
sep_wid_standard_deviation = calculate_standard_deviation(sep_wid_total_variance) 
pet_len_standard_deviation = calculate_standard_deviation(pet_len_total_variance) 
pet_wid_standard_deviation = calculate_standard_deviation(pet_wid_total_variance)

print("\n\n")
print("\t\tMean\t\tMedian\t\tVariance\t\tStandard Deviation\t")
print("Sepal Length\t" + str(sep_len_mean) + "\t\t" + str(sep_len_median) + "\t\t" + str(sep_len_total_variance) + "\t\t\t" + str(sep_len_standard_deviation))
print("Sepal Width\t" + str(sep_wid_mean) + "\t\t" + str(sep_wid_median) + "\t\t" + str(sep_wid_total_variance) + "\t\t\t" + str(sep_wid_standard_deviation))
print("Petal Length\t" + str(pet_len_mean) + "\t\t" + str(pet_len_median) + "\t\t" + str(pet_len_total_variance) + "\t\t\t" + str(pet_len_standard_deviation))
print("Petal Width\t" + str(pet_wid_mean) + "\t\t" + str(pet_wid_median) + "\t\t" + str(pet_wid_total_variance) + "\t\t\t" + str(pet_wid_standard_deviation))