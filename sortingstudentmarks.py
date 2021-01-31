# Step 1 to import relevant package :

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Import the dataset pandas :
healthData = pd.read_csv("C:/Program/AppData/healthdata.csv")

# Seperate the dataset into training and testing set :

# X always treated as input features :
X = healthData.iloc[:, :, -1].values
y = healthData.iloc[:, 3].values

# Deal with missing values, for dealing with missing values we need to use the imputer class

from sklearn.preprocessing import Imputer
missingvalueImputer = Imputer(missing_value = 'Nan',
                             strategy = 'mean',
                             axis = 0)

missingalueImputer = missingalueImputer.fit(X[:, 1:3])
# relevant equations

# Delaing with Categorical data need to import LableEncoder
