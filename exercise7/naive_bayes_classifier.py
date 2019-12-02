class NaiveBayesClassifier:

    def __init__(self, data_frame, percentage_training):
        self.data_frame = data_frame
        length = len(self.data_frame)
        training_length = round(percentage_training*length)
        self.train_df = self.data_frame.sample(training_length)
        self.test_df = self.data_frame[~self.data_frame.apply(
            tuple, 1).isin(self.train_df.apply(tuple, 1))]
        self.decision_attr = self.data_frame.columns[len(
            self.data_frame.columns) - 1]
        self.other_attr = self.data_frame.columns[0:len(
            self.data_frame.columns) - 1]

    def train_algorithm(self):
        self.calculate_decision_probabilities()
        self.calculate_conditional_probabilities()

    def calculate_decision_probabilities(self):
        decision_variables = self.data_frame[self.decision_attr].unique()
        self.decision_variable_probabilities = dict()
        for decision_variable in decision_variables:
            self.decision_variable_probabilities[decision_variable] = len(
                self.train_df.loc[self.train_df[self.decision_attr] == decision_variable])/len(self.train_df)

    def calculate_conditional_probabilities(self):
        decision_variables = self.data_frame[self.decision_attr].unique()
        self.conditional_probabilities = dict()
        for decision_variable in decision_variables:
            probabilities = dict()
            for attr in self.other_attr:
                attr_variables = self.data_frame[attr].unique()
                for variable in attr_variables:
                    probabilities[(attr, variable)] = len(self.train_df.loc[(self.train_df[attr] == variable) & (
                        self.train_df[self.decision_attr] == decision_variable)])/len(self.train_df.loc[self.train_df[self.decision_attr] == decision_variable])
            self.conditional_probabilities[decision_variable] = probabilities

    def test_algorithm(self):
        correct_predictions = 0
        for index, row in self.test_df.iterrows():
            row_tuple = tuple([row[attr] for attr in self.other_attr])
            prediction = self.predict(row_tuple)
            if prediction == row[self.decision_attr]:
                correct_predictions += 1
        return (correct_predictions/len(self.test_df)) * 100

    def predict(self, tuple_values):
        decision_variables = self.data_frame[self.decision_attr].unique()
        values = []
        for decision_variable in decision_variables:
            product = 1
            for row_attr_variable, attr in zip(tuple_values, self.other_attr):
                product *= self.conditional_probabilities[decision_variable][(attr, row_attr_variable)]
            values.append(self.decision_variable_probabilities[decision_variable] * product)
        return decision_variables[values.index(max(values))]
       
