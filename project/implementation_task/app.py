from k_means_clustering import K_Means_Clustering
from visualize import plot_clusters_2d
from math import floor,ceil,sqrt
from fpdf import FPDF

class App:

    def __init__(self, df):
        self.data_frame = df

    def __preprocess_dataframe(self):
        self.__remove_non_numeric_attributes()
        self.__clean_null_data()

    def __remove_non_numeric_attributes(self):
        self.non_numeric_attributes = []
        for attr in self.data_frame.columns:
            if str(self.data_frame[attr].dtype) == 'object':
                self.non_numeric_attributes.append(attr)
        self.data_frame = self.data_frame.drop(columns = self.non_numeric_attributes)
    
    def __clean_null_data(self):
        null_data = self.data_frame[self.data_frame.isnull().any(axis=1)]
        self.data_frame = self.data_frame[~self.data_frame.apply(tuple,1).isin(null_data.apply(tuple,1))]
    
    def calculate_stats(self):
        self.stats = dict()
        for attr in self.data_frame.columns:
            mean = sum(self.data_frame[attr])/len(self.data_frame[attr])
            sorted_column = sorted(self.data_frame[attr])
            median = (sorted_column[floor(len(sorted_column)/2)] + sorted_column[ceil(len(sorted_column)/2)])/2 if len(sorted_column)%2 == 0 else sorted_column[ceil(len(sorted_column)/2)]
            total_variance = sum([((elem - mean)**2)/len(self.data_frame[attr]) for elem in self.data_frame[attr]])
            standard_deviation = sqrt(total_variance)
            self.stats[attr] = {'mean': mean, 'median': median, 'total_variance': total_variance, 'standard_deviation': standard_deviation}
        
    def reduce_dimensionality(self, cols):
        if set(cols).issubset(self.data_frame.columns):
            self.data_frame = self.data_frame.drop(columns = cols)
        else:
            raise ValueError("The provided columns are not all part of the original dataset")
    
    def perform_algorithm(self, label1, label2):
        self.__preprocess_dataframe()
        self.calculate_stats()
        kmeans = K_Means_Clustering(self.data_frame, 2)
        centroids, clusters = kmeans.k_means_algorithm()
        plot_name = plot_clusters_2d(clusters, centroids,  label1, label2)
        self.construct_pdf(plot_name)
    
    def construct_pdf(self, image_name):
        pdf = FPDF()
        pdf.add_page()
        for attr, values in self.stats.items():
            pdf.set_font('arial', 'B', 13.0)
            pdf.cell(ln=1, h=5.0, align='L', w=0, txt=attr, border=0)
            pdf.set_font('arial', '', 11.0)
            for measure, calculated in values.items(): 
                pdf.cell(ln=1, h=5.0, align='L', w=0, txt=measure+": " + str(calculated), border=1)
        pdf.image(image_name, w=200,h=100)
        pdf.output('report.pdf', 'F')

    
        
        
        