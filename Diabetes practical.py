# Save Model Using Pickle

import pandas as pd
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
import pickle
dataframe = pd.read_csv('Tutorial data diabetes.csv')

# AI used to make sure the commands worked
print(dataframe.head())

# columns selected using their numerical values
array = dataframe.values

