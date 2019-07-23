# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 10:47:53 2019

@author: p0g00dg
"""
import Dataset as db
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN

S_X1 = db.S_X1

dbscan = DBSCAN(eps=0.55, min_samples=10)
Y1 = dbscan.fit_predict(S_X1)

plt.scatter(S_X1[:,0],S_X1[:,1], c=dbscan.labels_, cmap='rainbow', s=20)
plt.show()

