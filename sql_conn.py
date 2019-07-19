# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 10:18:28 2019
Connecting Database
@author: p0g00dg
"""
import mysql.connector
from mysql.connector import Error

def connect():
    connection = mysql.connector.connect(host='testcoe.mysql.database.azure.com',
                                         database='rebates',
                                         user='asvigani@testcoe',
                                         password='Sowj@nya94')
    return connection
    
def query(item_num,vendor_num):
    query = "select * from tier_results where item_number = "+item_num+" and vendor_number = "+vendor_num
    return query
    
    
