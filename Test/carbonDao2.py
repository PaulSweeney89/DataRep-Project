import mysql.connector
from mysql.connector import cursor

class CarbonDao2:
    db = ""
    def __init__(self):
        self.db = mysql.connector.connect(
            host = 'localhost',
            user= 'root',
            password = 'root',
            database ='embodiedCarbonDB'
        )
        #print ("connection made")

    def create(self, elem):
        cursor = self.db.cursor()
        sql = "insert into iceData2 (ID, Material, Density, EmbodiedCarbon) values (%s,%s,%s,%s,%s)"
        values = [
            elem['ID'],
            elem['Material'],
            elem['Density'],
            elem['EmbodiedCarbon']
        ]
        cursor.execute(sql, values)
        self.db.commit()
        return cursor.lastrowid

    def getAll(self):
        cursor = self.db.cursor()
        sql = 'SELECT * FROM iceData2'
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        #print(results)
        for result in results:
            resultAsDict = self.convertToDict(result)
            returnArray.append(resultAsDict)

        return returnArray

    def findByID(self, ID):
        cursor = self.db.cursor()
        sql = 'SELECT * FROM iceData2 WHERE ID = %s'
        values = [ ID ]
        cursor.execute(sql, values)
        result = cursor.fetchone()
        return self.convertToDict(result)
        

    def update(self, elem):
       cursor = self.db.cursor()
       sql = "UPDATE iceData2 SET Material = %s Density = %s, EmbodiedCarbon = %s, WHERE ID = %s"
       values = [
           elem['Material'],
           elem['Density'],
           elem['EmbodiedCarbon'],
           elem['ID']
       ]
       cursor.execute(sql, values)
       self.db.commit()
       return elem

    def delete(self, ID):
       cursor = self.db.cursor()
       sql = 'DELETE FROM iceData2 WHERE ID = %s'
       values = [ID]
       cursor.execute(sql, values)
       
       return {}



    def convertToDict(self, result):
        colnames = ['ID','Material', 'Density', 'EmbodiedCarbon']
        elem = {}

        if result:
            for i , colName in enumerate(colnames):
                value = result[i]
                elem[colName] = value
        return elem

carbonDao2 = CarbonDao2()
