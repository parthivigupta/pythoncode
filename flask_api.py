# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 10:31:25 2019
Flask API
@author: p0g00dg
"""

import sql_conn
from flask import Flask, jsonify, request

def conn(item_num, vendor_num):
    connection = sql_conn.connect()
    try:
        if connection.is_connected():
            cursor = connection.cursor()
            query = sql_conn.query(item_num,vendor_num)
            cursor.execute(query)
            col = cursor.column_names
            records = cursor.fetchall()
            return(records, col)
    
    except sql_conn.Error as e :
        print ("Error while connecting to MySQL", e)
    finally:
        #closing database connection.
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
             
def result(records, col):
    data = {}
    mylist = []
    data.clear()   
    mylist.clear()
    
    for i in range(len(records)):
       for j in range(len(col)):
           data[col[j]] = records[i][j]   
       mylist.append(data)
       data = {}
    
    return mylist
   
  
app = Flask(__name__)


def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()
       
@app.route('/result', methods=['GET'])
def tier_result():
    item_num  = request.args.get('item_num', None)
    vendor_num   = request.args.get('vendor_num', None)
    records, col = conn(item_num, vendor_num)
    tier_result = result(records, col)
    return jsonify(tier_result)

@app.route('/shutdown', methods=['POST'])
def shutdown():
    shutdown_server()
    return 'Server shutting down...'

if __name__ == '__main__':
   app.run(debug=True)


    


    