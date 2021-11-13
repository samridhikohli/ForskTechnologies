# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 17:19:50 2018

@author: MUJ
"""

#K MEANS++ ALGORITHM|CLUSTERING

#data divided into various clusters

#WCSS 
#within cluster sum of squares
#sum of distance between point and centroid and square of this distance 
#summed up of all clusters

import pandas as pd

import matplotlib.pyplot as plt

dataset=pd.read_csv('Mall_Customers.csv')          #spending score is not a label
features=dataset.iloc[:,[3,4]].values              #treating as x and y axis


from sklearn.cluster import KMeans

#ELBOW METHOD
wcss=[]
for i in range(1,11):
    kmeans=KMeans(n_clusters=i,init='k-means++',random_state=0)
    kmeans.fit(features)
    wcss.append(kmeans.inertia_)
    
#the elbow method tells us which is the coorect number of clusters to choose
#plot this with number of clusters on x axis and wcss on y axis
#pick that value of number of clusters where a sudden shift i.e. elbow like graph occurs
    
#PLOTTING THIS ELBOW METHOD
plt.plot(range(1,11),wcss)
plt.xlabel('no od clusters')
plt.ylabel('wcss')
plt.show()

#hence the number of clusters selected is 5
    
#FITING KMEANS TO THE DATASET
kmeans=KMeans(n_clusters=5,init='k-means++',random_state=0)  #making clusters no. of clusters are 5
pred_cluster=kmeans.fit_predict(features)

#so here we are able to categorize people base on their annual income and spending score
#we can now target people based on our preference to sell our product/services in the market

#VISUALIZING CLUSTERS
plt.scatter(features[pred_cluster==0,0],features[pred_cluster==0,1],s=100,c='red',label='Cluster 1')   
plt.legend()
plt.show()
#s is size of dots and c is the colour of dots
#0,0 means 0 cluster and its x coordinate
#0,1 meanss 0 cluster and its Y coordinate
