## create MYSQL Table from iceDB.csv file using Python

import mysql.connector
from mysql.connector import Error
import pandas as pd

# Import ICE Data from csv file as Pandas DataFrame
iceDF = pd.read_csv('iceDB.csv', index_col=False, delimiter = ',')

# Connect to embodiedCarbonDB
try:
	conn = mysql.connector.connect(
		host='localhost', 
		database='embodiedCarbonDB', 
		user='root', 
		password='root'
		)
	if conn.is_connected():
		cursor = conn.cursor()
		cursor.execute("select database();")
		record = cursor.fetchone()
		print("You're connected to database: ", record)
		cursor.execute('DROP TABLE IF EXISTS iceData;')
		print('Creating table....')

		# create table iceData
		sql ='''CREATE TABLE iceData(
			ID INT PRIMARY KEY,
			Material VARCHAR(255),
			Name VARCHAR(255),
			Density FLOAT(20),
			EmbodiedCarbon FlOAT(20)
		)'''

		cursor.execute(sql)
		print("Table is created....")

		# Loop through the ICE DataFrame
		for i, row in iceDF.iterrows():
			sql = "INSERT INTO embodiedCarbonDB.iceData VALUES (%s, %s, %s, %s, %s)"
			cursor.execute(sql, tuple(row))
			print("Record inserted")
			conn.commit()

# Manually update ID column to AUTO_INCREMENT using MYSQL Command:
# ALTER TABLE iceData MODIFY COLUMN ID INT AUTO_INCREMENT;

except Error as e:
	print("Error while connecting to MySQL", e)
