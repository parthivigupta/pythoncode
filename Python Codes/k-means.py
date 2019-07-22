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

from_data = tier_data['From']
to_data = tier_data['To']
rate = tier_data['Rate']

#plt.scatter(from_data, rate, s=5, c='gray', label='from values')
#plt.show()
#plt.scatter(to_data, rate, s=5, c='gray', label='to values')
#plt.show()
X1 = DataFrame(tier_data, columns = ['From','Rate'])
X2 = DataFrame(tier_data, columns = ['To','Rate'])   
k = 3

kmeans = KMeans(n_clusters = k, init = 'k-means++', random_state = 1)

Y1 = kmeans.fit_predict(X1)
plt.scatter(X1[Y1==0]['From'], X1[Y1==0]['Rate'] , s=5, c='red', label='Cluster1')
plt.scatter(X1[Y1==1]['From'], X1[Y1==1]['Rate'] , s=5, c='blue', label='Cluster2')
plt.scatter(X1[Y1==2]['From'], X1[Y1==2]['Rate'] , s=5, c='green', label='Cluster3')
plt.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1], s=100, c='yellow', label='Centroid')
plt.show()

Y2 = kmeans.fit_predict(X1)
plt.scatter(X2[Y2==0]['To'], X2[Y2==0]['Rate'] , s=5, c='red', label='Cluster1')
plt.scatter(X2[Y2==1]['To'], X2[Y2==1]['Rate'] , s=5, c='blue', label='Cluster2')
plt.scatter(X2[Y2==2]['To'], X2[Y2==2]['Rate'] , s=5, c='green', label='Cluster3')
plt.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1], s=100, c='yellow', label='Centroid')
plt.show()

#plt.scatter(tier_seq, rate,  color='gray', s=6)