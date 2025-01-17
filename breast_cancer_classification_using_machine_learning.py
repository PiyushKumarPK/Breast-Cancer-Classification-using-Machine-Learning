# -*- coding: utf-8 -*-
"""Breast Cancer Classification using Machine Learning.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1JYroIIpWrbCsc7gRoHHBMKXWhfzWpXrF

**Importing the dependencies**
"""

import numpy as np
import pandas as pd
import sklearn.datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

#numpy libray is one of the most library that we have in python and it is used to make numpy array
#pandas is the library which is we know very helpful in order to create pandas data frame so the generally the dataset we will have in the form od CVS file or numpy array so we will load this data into a data frame which we are know more of structured tables so that is importance of pandas whuch is used to create dataframe which help us know analyze and process the data in more sctured form
#accuracy score which is used to determine know how many correct prediction our model is making and all that

"""***Data collection and preprocessing ***"""

# data_frame = pd.read_csv('/content/data.csv')
                #or
# # loadind the dataset from sklearn
breast_cancer_dataset = sklearn.datasets.load_breast_cancer()

print(breast_cancer_dataset)

# loading the data to a pandas data frame
data_frame = pd.DataFrame(breast_cancer_dataset.data, columns = breast_cancer_dataset.feature_names)
#i am bascically doing here is i am going to load all this data so we can see name of the dataset is breast_cancer_dataset and we have in the form of dictionary so we can consider this data as key and all the values that are associated to it we know that dictionary there are key values pairs . if i want to access all those values we need to mention the key which is nothing but the dataand all the target values are present in key called target. if we come below all the column name  or all the target_names

#print the first 5 rows of the dataframe
data_frame.head()

#print the last 5 rows of the dataframe
data_frame.tail()

#Number of rows and columns in the dataset
data_frame.shape

#getting some information about the data
data_frame.info()

#checking missing value
data_frame.isnull().sum()

#statistical measure about the data
data_frame.describe()

#checking the Number of Target variable means labels [M = malignant, B = benign]
data_frame['label'].value_counts()

"""1-->Benign,
0-->Malignant
"""

data_frame.groupby('label').mean()

#separating the features and target columns
X = data_frame.drop(columns='label',axis=1)
Y = data_frame['label']

print(X)

print(Y)

"""**Splitting tha data into training data and testing data**"""

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=2)

print(X.shape, X_train.shape, X_test.shape)

"""**Model Training**"""

#logistic regression is very useful for binary classification problem where we just have two classes in this two classes that we have benigh and maligant
from sklearn.linear_model import LogisticRegression

#Here model is variable
model = LogisticRegression()

model.fit(X_train, Y_train)

"""**Model Evaluation**"""

#Accuracy on training data
from sklearn.metrics import accuracy_score

#accuracy score
X_train_prediction = model.predict(X_train)
trainig_data_accuracy = accuracy_score(Y_train, X_train_prediction)

print('Accuracy on training data', trainig_data_accuracy)

#Accuracy on test data
X_test_prediction = model.predict(X_test)
test_data_accuracy = accuracy_score(Y_test, X_test_prediction)

print('Accuracy on test data', test_data_accuracy)

""" **Building a Predictive**"""

input_data = (13.54,14.36,87.46,566.3,0.09779,0.08129,0.06664,0.04781,0.1885,0.05766,0.2699,0.7886,2.058,23.56,0.008462,0.0146,0.02387,0.01315,0.0198,0.0023,15.11,19.26,99.7,711.2,0.144,0.1773,0.239,0.1288,0.2977,0.07259)

# change the input data to a numpy array
input_data_as_numpy_array = np.asarray(input_data)

# reshape the numpy array as we are predicting for one datapoint
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction = model.predict(input_data_reshaped)
print(prediction)

if (prediction[0] == 0):
  print('The Breast cancer is Malignant')

else:
  print('The Breast Cancer is Benign')

input_data = (19.81,22.15,130,1260,0.09831,0.1027,0.1479,0.09498,0.1582,0.05395,0.7582,1.017,5.865,112.4,0.006494,0.01893,0.03391,0.01521,0.01356,0.001997,27.32,30.88,186.8,2398,0.1512,0.315,0.5372,0.2388,0.2768,0.07615)

# change the input data to a numpy array
input_data_as_numpy_array = np.asarray(input_data)

# reshape the numpy array as we are predicting for one datapoint
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction = model.predict(input_data_reshaped)
print(prediction)

if (prediction[0] == 0):
  print('The Breast cancer is Malignant')

else:
  print('The Breast Cancer is Benign')