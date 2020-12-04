# Takes the MarathonData CSV and loads into PyCharm

import pandas
marathon_data = pandas.read_csv('InitialMarathonData.csv')
print(marathon_data)