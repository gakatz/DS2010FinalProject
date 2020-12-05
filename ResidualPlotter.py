from sklearn.linear_model import LinearRegression
from numpy import genfromtxt
from yellowbrick.regressor import ResidualsPlot
import pandas as pd
import numpy as np

# Create the train and test data
x_training = pd.read_csv("MarathonDataXTraining.csv") # reading CSV into numpy array
y_training = pd.read_csv("MarathonDataYTraining.csv", usecols = [2]) # reading CSV into numpy array
x_testing = pd.read_csv("MarathonDataXTesting.csv") # reading CSV into numpy array
y_testing = pd.read_csv("MarathonDataYTesting.csv", usecols = [2]) # reading CSV into numpy array

y_training = np.delete(y_training, 0, axis = 1)
y_training = np.delete(y_training, 1, axis = 1)
y_testing = np.delete(y_testing, 0, axis = 1)
y_testing = np.delete(y_testing, 1, axis = 1)

y_training = y_training.flatten()
y_testing = y_testing.flatten()

print(x_training.shape)
print(y_training.shape)
print(x_testing.shape)
print(y_testing.shape)


# Creating an instance of the class Linear Regression
model = LinearRegression()

# Making residual plot
visualizer = ResidualsPlot(model)

visualizer.fit(x_training, y_training)  # Fit the training data to the visualizer
visualizer.score(x_testing, y_testing)  # Makes predictions using the x_testing data and compares that to the actual marathon times
visualizer.show(model)                 # Finalize and render the figure