import pandas as pd
from app import App
import sys, getopt

number_of_clusters = int(getopt.getopt(sys.argv[1:],"")[1][0])
label_1 = getopt.getopt(sys.argv[1:],"")[1][1]
label_2 = getopt.getopt(sys.argv[1:],"")[1][2]


df = pd.read_csv("../african_crises.csv", sep=",")

application = App(df)
application.reduce_dimensionality(['case', 'year'])
application.perform_algorithm( number_of_clusters, label_1, label_2)

