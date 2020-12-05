from sklearn.linear_model import LinearRegression
import numpy as np
from yellowbrick.regressor import ResidualsPlot
import pandas as pd

# Create the train and test data
x_training = pd.read_csv("MarathonDataXTraining.csv") # reading CSV into a dataframe
y_training = pd.read_csv("MarathonDataYTraining.csv") # reading CSV into a dataframe
x_testing = pd.read_csv("MarathonDataXTesting.csv") # reading CSV into a dataframe
y_testing = pd.read_csv("MarathonDataYTesting.csv") # reading CSV into a dataframe


# Creating an instance of the class Linear Regression
model = LinearRegression()

# Making residual plot
visualizer = ResidualsPlot(model)

visualizer.fit(x_training, y_training)  # Fit the training data to the visualizer
visualizer.score(x_testing, y_testing)  # Makes predictions using the x_testing data and compares that to the actual marathon times
visualizer.show()                 # Finalize and render the figure