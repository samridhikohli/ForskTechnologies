# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 17:17:46 2018

@author: MUJ
"""
#MACHINE LEARNING

#y=f(x) Here x is INDEPENDENT VARIABLE and y is DEPENDENT VARIABLE

#independent variables are called FEATURES

#dependent variables are called LABELS

#a data set which has both features and labels is called a LABELLED DATA SET (SUPERVISED MACHINE LEARNING) || PREDICTIONS

#a data set with only features and no labels is called UNLABELLED DATA SET (UNSUPERVISED MACHINE LEARNING)

#data taken out of data set to train the machine/model is called TRAINING DATA (60-80%),this data has feautres and labels

#the remaining data to test its training is called TEST DATA (20-40%),this data has features and labels

"""to test the training we only give features as input and the prediction is compared with the label 
if the prediction and label match then it is called GOOD TRAINING else BAD TRAINING"""


import pandas as pd

dataset=pd.read_csv("Data.csv") 

#FEATURES AND LABELS
features=dataset.iloc[:,:-1].values
"""array([['France', 44.0, 72000.0],
       ['Spain', 27.0, 48000.0],
       ['Germany', 30.0, 54000.0],
       ['Spain', 38.0, 61000.0],
       ['Germany', 40.0, nan],
       ['France', 35.0, 58000.0],
       ['Spain', nan, 52000.0],
       ['France', 48.0, 79000.0],
       ['Germany', 50.0, 83000.0],
       ['France', 37.0, 67000.0]], dtype=object)"""

labels=dataset.iloc[:,3].values
"""
 array(['No', 'Yes', 'No', 'No', 'Yes', 'Yes', 'No', 'Yes', 'No', 'Yes'], dtype=object)"""
 
 
 dataset2=pd.read_csv("Cricket_Salary_Data.csv") 
 features=dataset2.iloc[:,:-1].values
 """array([['Rohit Sharma', 30.0, 10000L],
       ['Shikhar Dhawan', 31.0, 5000L],
       ['Virat Kohli', 28.0, 20000L],
       ['Ajinkya Rahane', 29.0, 20000L],
       ['Suresh Raina', 31.0, 10000L],
       ['Manish Pandey', 28.0, 5000L],
       ['MS Dhoni', 36.0, 20000L],
       ['Hardik Pandya', 24.0, 10000L],
       ['Bhuvneshwar Kumar', 27.0, 10000L],
       ['Yuzvendra Chahal', nan, 5000L],
       ['Jasprit Bumrah', 23.0, 10000L],
       ['Kuldeep Yadav', 24.0, 5000L],
       ['Shardul Thakur', nan, 5000L]], dtype=object)"""

 labels=dataset2.iloc[:,3].values
 """array(['B', 'C', 'A', 'A', 'B', 'C', 'A', 'B', 'B', 'C', 'B', 'C', 'C'], dtype=object)"""
 
 #SPLITTING THE DATASET INTO TRAINING AND TESTING DATA
from sklearn.model_selection import train_test_split
features_train,features_test,labels_train,labels_test=train_test_split(features,labels,test_size=0.2,random_state=0)
 """  FEATURES_TEST
 array([['MS Dhoni', 36.0, 20000L],
       ['Kuldeep Yadav', 24.0, 5000L],
       ['Suresh Raina', 31.0, 10000L]], dtype=object)"""

"""  FEATURES_TRAIN
array([['Jasprit Bumrah', 23.0, 10000L],
       ['Virat Kohli', 28.0, 20000L],
       ['Bhuvneshwar Kumar', 27.0, 10000L],
       ['Shikhar Dhawan', 31.0, 5000L],
       ['Hardik Pandya', 24.0, 10000L],
       ['Yuzvendra Chahal', nan, 5000L],
       ['Ajinkya Rahane', 29.0, 20000L],
       ['Rohit Sharma', 30.0, 10000L],
       ['Manish Pandey', 28.0, 5000L],
       ['Shardul Thakur', nan, 5000L]], dtype=object)"""

"""  LABELS_TRAIN
array(['B', 'A', 'B', 'C', 'B', 'C', 'A', 'B', 'C', 'C'], dtype=object)"""

""" LABELS_TEST
 array(['A', 'C', 'B'], dtype=object)"""

#PREPROCESSING|ETL ACTIVITIES|WRANGLING|CLEANING

#1>handle missing value
from sklearn.preprocessing import Imputer                        #Imputer class,imputer object
imputer=Imputer(missing_values='NaN',strategy='mean',axis=0)
imputer=imputer.fit(features[:,1:2])                             #fiting the data into the object
features[:,1:2]=imputer.transform(features[:,1:2])               #transforming the data
"""array([['Rohit Sharma', 30.0, 10000L],
       ['Shikhar Dhawan', 31.0, 5000L],
       ['Virat Kohli', 28.0, 20000L],
       ['Ajinkya Rahane', 29.0, 20000L],
       ['Suresh Raina', 31.0, 10000L],
       ['Manish Pandey', 28.0, 5000L],
       ['MS Dhoni', 36.0, 20000L],
       ['Hardik Pandya', 24.0, 10000L],
       ['Bhuvneshwar Kumar', 27.0, 10000L],
       ['Yuzvendra Chahal', 28.272727272727273, 5000L],
       ['Jasprit Bumrah', 23.0, 10000L],
       ['Kuldeep Yadav', 24.0, 5000L],
       ['Shardul Thakur', 28.272727272727273, 5000L]], dtype=object)"""
#works only for numeric data and gives the nd.array ie. only the raw data the title and index goes 
#so better to use is fillna in pandas


#2>converting catagorical data to numerical form called LABEL ENCODING
from sklearn.preprocessing import LabelEncoder
labelencoder=LabelEncoder()
features[:,0]=labelencoder.fit_transform(features[:,0])
"""
array([[7L, 30.0, 10000L],
       [9L, 31.0, 5000L],
       [11L, 28.0, 20000L],
       [0L, 29.0, 20000L],
       [10L, 31.0, 10000L],
       [6L, 28.0, 5000L],
       [5L, 36.0, 20000L],
       [2L, 24.0, 10000L],
       [1L, 27.0, 10000L],
       [12L, 28.272727272727273, 5000L],
       [3L, 23.0, 10000L],
       [4L, 24.0, 5000L],
       [8L, 28.272727272727273, 5000L]], dtype=object)"""

#if the order issue is to be removed after label encoding then we do ONE HOT ENCODING (dont want to preserve the order that we got from label encoding)

#3>one hot encoding of the labelled data
from sklearn.preprocessing import OneHotEncoder
onehotencoder=OneHotEncoder(categorical_features=[0])
features=onehotencoder.fit_transform(features).toarray()
"""
1	0	0	0	0	0	0	0	1	0	0	0	0	0	30	10000
1	0	0	0	0	0	0	0	0	0	1	0	0	0	31	5000
1	0	0	0	0	0	0	0	0	0	0	0	1	0	28	20000
0	1	0	0	0	0	0	0	0	0	0	0	0	0	29	20000
1	0	0	0	0	0	0	0	0	0	0	1	0	0	31	10000
1	0	0	0	0	0	0	1	0	0	0	0	0	0	28	5000
1	0	0	0	0	0	1	0	0	0	0	0	0	0	36	20000
1	0	0	1	0	0	0	0	0	0	0	0	0	0	24	10000
1	0	1	0	0	0	0	0	0	0	0	0	0	0	27	10000
1	0	0	0	0	0	0	0	0	0	0	0	0	1	28.2727	5000
1	0	0	0	1	0	0	0	0	0	0	0	0	0	23	10000
1	0	0	0	0	1	0	0	0	0	0	0	0	0	24	5000
"""


