import mysql.connector
from mysql.connector import cursor
import DBconfig as cfg

class CarbonDao:
    db = ""
    def __init__(self):
        self.db = mysql.connector.connect(
            host =      cfg.mysql['host'],
            user =      cfg.mysql['user'],
            password =  cfg.mysql['password'],
            database =  cfg.mysql['database']
        )
        #print ("connection made")


    def create(self, elem):
        cursor = self.db.cursor()
        sql = "insert into iceData (ID, Material, Name, Density, EmbodiedCarbon) values (%s,%s,%s,%s,%s)"
        values = [
            elem['ID'],
            elem['Material'],
            elem['Name'],
            elem['Density'],
            elem['EmbodiedCarbon']
        ]
        cursor.execute(sql, values)
        self.db.commit()
        return cursor.lastrowid


    def getAll(self):
        cursor = self.db.cursor()
        sql = 'SELECT * FROM iceData'
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        #print(results)
        for result in results:
            resultAsDict = self.convertToDict(result)
            returnArray.append(resultAsDict)

        return returnArray


    def findById(self, ID):
        cursor = self.db.cursor()
        sql = 'SELECT * FROM iceData WHERE ID = %s'
        values = [ID]
        cursor.execute(sql, values)
        result = cursor.fetchone()
        return self.convertToDict(result)
        

    def update(self, elem):
       cursor = self.db.cursor()
       sql = "UPDATE iceData SET Material = %s, Name = %s, Density = %s, EmbodiedCarbon = %s WHERE ID = %s"
       values = [
           elem['Material'],
           elem['Name'],
           elem['Density'],
           elem['EmbodiedCarbon'],
           elem['ID']
       ]
       cursor.execute(sql, values)
       self.db.commit()
       return elem


    def delete(self, ID):
       cursor = self.db.cursor()
       sql = 'DELETE FROM iceData WHERE ID = %s'
       values = [ID]
       cursor.execute(sql, values)
       
       return {}


    def convertToDict(self, result):
        colnames = ['ID','Material', 'Name', 'Density', 'EmbodiedCarbon']
        elem = {}

        if result:
            for i , colName in enumerate(colnames):
                value = result[i]
                elem[colName] = value
        return elem

carbonDao = CarbonDao()
