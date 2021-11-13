# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 17:16:02 2018

@author: MUJ
"""

#2.KNN-K Nearest Neighbour

#defualt value of k is 5
#better than logical regression
#used under classification
#non linear classifier
#it will identify 5 data points nearest to a point not belonging to any of the class
#then we will decide the class of thie point depending on the maximum number of data points belonging to a class (category)

#MANHATTAN DISTANCE
#MD=|(X2-X1)|+|(Y2-Y1)| absolute value of these

#EUCLID DISTANCE
#ED=sqroot[(X2-X1)^2+(Y2-Y1)^2]

import pandas as pd
import numpy as np

dataset1=pd.read_csv('Social_Network_Ads.csv')
features=dataset1.iloc[:,[2,3]].values
labels=dataset1.iloc[:,4].values

from sklearn.model_selection import train_test_split
features_train,features_test,labels_train,labels_test=train_test_split(features,labels,test_size=0.25,random_state=0)

from sklearn.preprocessing import StandardScaler
sc=StandardScaler()                                    
features_train=sc.fit_transform(features_train)        
features_test=sc.transform(features_test)  

from sklearn.neighbors import KNeighborsClassifier
classifier=KNeighborsClassifier(n_neighbors=5,p=2) #p=2 means Euclidian distance and p=1 means Manhattan distance
classifier.fit(features_train,labels_train)

labels_pred=classifier.predict(features_test)

from sklearn.metrics import confusion_matrix
cm=confusion_matrix(labels_test,labels_pred)




#3.SVM SUPPORT VECTOR MACHINE

#if data is linearly separable dont use this algorithm
#data should be not linearly separable
#can be used in both classification and regression

#KERNEL TRICK
#a hyperplane divides the two types of data and converts the 2D data into 3D data |KERNEL FUNCTIONS
#we then convert this 3D data back to 2D data by taking projection and we get boundary of our classifier

import pandas as pd

dataset=pd.read_csv('Match_making.csv')
features=dataset.iloc[:,:-1].values
labels=dataset.iloc[:,-1].values

from sklearn.model_selection import train_test_split
features_train,features_test,labels_train,labels_test=train_test_split(features,labels,test_size=0.2,random_state=0)

from sklearn.svm import SVC
classifier=SVC(kernel='poly',random_state=0)
classifier.fit(features_train,labels_train)

labels_pred=classifier.predict(features_test)

from sklearn.metrics import confusion_matrix
cm=confusion_matrix(labels_test,labels_pred)

#4.DECISION TREE REGRESSION

#5.RANDOM FOREST REGRESSION


#UNSUPERVISED MACHINE LEARNING

#only features no labels
#no labels so impossible to make predictions
#no predictions
#so dataset will be divided into clusters
#the interpretation of the clusters is left on us and is not pre defined


#1.CLUSSTERING

#data divided into various clusters
#K MEANS++ algorithm used
#others algorithms include dbscan(declustering) and hierarchial clustering

#K MEANS++ ALGORITHM
#every cluster has a centroid which is randomy assigned
#the boundary between two clusters is determined by the mid point of the line joining two centroids of the two clusters
#we find the center of mass of every cluster and then shift are centroids to the center of mass
#the above process of shifting centroid and reassignnment of points keeps happening till we reach the actual center of mass
#as the centroids are now shifted the boundary will also update
#Vornoi diagrams are used

#2.ASSOCIATION

#used for mainly ecommerce,retail based websites
#which item sold with respect to another item
#example milk and bread (dependency/association)
#if bought item X then we can recommend item Y
#APRORI algorithm used 



