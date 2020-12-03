# Takes the data and divides it into training and testing data

from sklearn.model_selection import train_test_split
import pandas as pd

x_list = ["Name", "Category", "km4week", "sp4week", "CrossTraining", "Wall21"]
y_list = ["MarathonTime"]
x = pd.read_csv("MarathonData.csv", usecols = x_list)
y = pd.read_csv("MarathonData.csv", usecols = y_list)
# x.to_csv(index=False)
# y.to_csv(index=False)


x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.75, random_state=42)

print(f"Test labels:\n{x_train}")
print(f"Train labels:\n{y_train}")
print(f"Test labels:\n{x_test}")
print(f"Train labels:\n{y_test}")

