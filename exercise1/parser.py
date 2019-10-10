from scipy.io import arff
import pandas as pd
from itertools import product
from numpy import append

data = arff.loadarff('weather.nominal.arff')
dataFrame = pd.DataFrame(data[0])

rules = product(append(dataFrame['outlook'].unique(), b'whatever'), append(dataFrame['temperature'].unique(), b'whatever'), append(dataFrame['humidity'].unique(), b'whatever'), append(dataFrame['windy'].unique(), b'whatever'), dataFrame['play'].unique())

rules_list = set(rules)
rules_confidence = []
rules_support = []

# support and confidence
# support => number of times that happens / number of rules
# confidence => number of times 
for rule in rules_list:
    rule_list = list(rule)
    if rule_list[0] == b'whatever':
        rule_list[0] = dataFrame['outlook']
    if rule_list[1] == b'whatever':
        rule_list[1] = dataFrame['temperature']
    if rule_list[2] == b'whatever':
        rule_list[2] = dataFrame['humidity']
    if rule_list[3] == b'whatever':
        rule_list[3] = dataFrame['windy']    
    r = len(dataFrame.loc[(dataFrame['outlook'] == rule_list[0]) & (dataFrame['temperature'] == rule_list[1]) & (dataFrame['humidity'] == rule_list[2]) & (dataFrame['windy'] == rule_list[3] )])
    cmax = len(dataFrame.loc[(dataFrame['outlook'] == rule_list[0] ) & (dataFrame['temperature'] == rule_list[1]) & (dataFrame['humidity'] == rule_list[2]) & (dataFrame['windy'] == rule_list[3]) & (dataFrame['play'] == rule_list[4])])
    n = len(dataFrame)
    if r == 0:
        rules_confidence.append(0)
    else:
        rules_confidence.append(cmax/r)
    rules_support.append(r/n)


# print rules
print("Outlook - Temperature - Humidity -  Windy - Play - Confidence - Support")
i = 0
for rule in rules_list:
    print(rule[0].decode("utf-8") + " - " + rule[1].decode("utf-8") + " - " + rule[2].decode("utf-8") + " - " + rule[3].decode("utf-8") + " - " + rule[4].decode("utf-8") + " - " + str(rules_confidence[i]) + " - " + str(rules_support[i]))
    i += 1


print("There are " + str(len(rules_list))  + " rules.")

