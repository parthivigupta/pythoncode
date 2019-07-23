# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 14:04:10 2019

@author: p0g00dg
"""
import Dataset as db
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering
from scipy.cluster.hierarchy import dendrogram, linkage

S_X1 = db.S_X1

linked = linkage(S_X1, 'single')

plt.figure()
dendrogram(linked,
            orientation='top',
            distance_sort='descending',
            show_leaf_counts=True)
plt.show()

cluster = AgglomerativeClustering(n_clusters=db.clusters, affinity='euclidean', linkage='ward')
Y1 = cluster.fit_predict(S_X1)


plt.scatter(S_X1[:,0],S_X1[:,1], c=cluster.labels_, cmap='rainbow', s=20)
plt.show()