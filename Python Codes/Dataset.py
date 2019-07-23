# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 15:19:30 2019

@author: p0g00dg
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas import DataFrame
from sklearn import preprocessing


#Change File Name and Sheet Name accordingly
excel_file = 'Rebates Data.xlsx'
sheet = 'Tier Results'
tier_data = pd.read_excel(excel_file, sheet_name=sheet)

from_data = tier_data['From']
to_data = tier_data['To']
rate = tier_data['Rate']

X = DataFrame(tier_data, columns = ['Rate','From'])   
X1 = np.array(X)
X = DataFrame(tier_data, columns = ['Rate','To'])  
X2 = np.array(X)

N_X1 = preprocessing.normalize(X1)
S_X1 = preprocessing.scale(X1)


N_X2 = preprocessing.normalize(X2)
S_X2 = preprocessing.scale(X2)
clusters = 4



