# python script to create MYSQL database for embodied carbon data

import mysql.connector as msql
from mysql.connector import Error
# Import Database Configuration
import DBconfig as cfg                            

try:
    conn = msql.connect(
        host =      cfg.mysql['host'],
        user =      cfg.mysql['user'],
        password =  cfg.mysql['password'],
        database =  cfg.mysql['database']
    )

    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("CREATE DATABASE embodiedCarbonDB")
        print("Database is created")

except Error as e:
    print("Error while connecting to MySQL", e)