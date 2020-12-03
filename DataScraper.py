# Takes the MarathonData CSV and loads into PyCharm

import pandas
marathon_data = pandas.read_csv('MarathonData.csv')
print(marathon_data)