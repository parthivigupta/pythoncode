# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 20:23:40 2019

@author: p0g00dg
"""
import Dataset as db
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

S_X1 = db.S_X1
kmeans = KMeans(n_clusters = db.clusters, init = 'k-means++', random_state = 1)

Y1 = kmeans.fit_predict(S_X1)

plt.scatter(S_X1[:,0],S_X1[:,1], c=kmeans.labels_, cmap='rainbow', s=20)
plt.show()
#plt.scatter(X2[Y2==0]['To'], X2[Y2==0]['Rate'] , s=5, c='red', label='Cluster1')
#plt.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1], s=100, c='yellow', label='Centroid')
