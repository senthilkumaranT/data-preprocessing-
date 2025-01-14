# -*- coding: utf-8 -*-
"""data preprocessing .ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1BoLf5NyPujPpBgVjZhz7zo05AP-bJt_d

IMPORTING THE LIBRARY
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

"""IMPORTING THE DATASET"""

data =pd.read_excel("/content/data_for_preprocessing.xlsx")
X= data.iloc[:, :-1].values
y= data.iloc[:,-1].values

print(X)

print(y)

"""HANDLING MISSING DATA"""

from  sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values = np.nan, strategy = "mean")
imputer.fit(X[:, 1:3])
X[:,1:3]=imputer.transform(X[:,1:3])

print(X)

"""Encoding Categorical Data"""

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

ct = ColumnTransformer(transformers = [("encoder",OneHotEncoder(),[0])],remainder="passthrough")
X = np.array(ct.fit_transform(X))

print(X)

from sklearn.preprocessing import LabelEncoder
Le = LabelEncoder()
y = Le.fit_transform(y)

print(y)

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=1)

print(X_train)

print(X_test)

print(y_train)

print(y_test)