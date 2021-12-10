# create MYSQL database for embodied carbon data

import mysql.connector as msql
from mysql.connector import Error

try:
    conn = msql.connect(
        host='localhost', 
        user='root',  
        password='root', 
        )
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("CREATE DATABASE embodiedCarbonDB")
        print("Database is created")
except Error as e:
    print("Error while connecting to MySQL", e)