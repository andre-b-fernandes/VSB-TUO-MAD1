import pandas

from naive_bayes_classifier import NaiveBayesClassifier

df = pandas.read_csv("weather.csv", sep=";")

naive_bayes = NaiveBayesClassifier(df, 0.6)
naive_bayes.train_algorithm()

accuracy = naive_bayes.test_algorithm()
print("Algorithm Accuracy : " + str(accuracy) + " %")
tuple_data = ('Overcast','Hot','Normal', True)
prediction = naive_bayes.predict(tuple_data)
print("Prediction for " + str(tuple_data) + " is " + prediction)