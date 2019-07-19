# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 20:23:40 2019

@author: p0g00dg
"""

import pandas as pd
from pandas import DataFrame
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

#Change File Name and Sheet Name accordingly
excel_file = 'Rebates Data.xlsx'
sheet = 'Tier Results'
tier_data = pd.read_excel(excel_file, sheet_name=sheet)

tier_seq = tier_data['Tier Sequence']
rate = tier_data['Rate']

X = DataFrame(tier_data, columns = ['Tier Sequence','Rate'])

k = 3

kmeans = KMeans(n_clusters = k, init = 'k-means++', random_state = 1)

Y = kmeans.fit_predict(X)

plt.scatter(X[Y==0]['Tier Sequence'], X[Y==0]['Rate'] , s=5, c='red', label='Cluster1')
plt.scatter(X[Y==1]['Tier Sequence'], X[Y==1]['Rate'] , s=5, c='blue', label='Cluster2')
plt.scatter(X[Y==2]['Tier Sequence'], X[Y==2]['Rate'] , s=5, c='green', label='Cluster3')
plt.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1], s=100, c='yellow', label='Centroid')
plt.show()

#plt.scatter(tier_seq, rate,  color='gray', s=6)