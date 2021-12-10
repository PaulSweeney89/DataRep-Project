import mysql.connector
from mysql.connector import cursor

db = mysql.connector.connect(
    host = 'localhost',
    user= 'root',
    password = 'root',
    database ='embodiedCarbonDB'
)
    #print ("connection made")

def getAll():
    cursor = db.cursor()
    sql = 'SELECT * FROM iceData'
    cursor.execute(sql)
    results = cursor.fetchall()
    returnArray = []
    #print(results)
    for result in results:
        resultAsDict = convertToDict(result)
        returnArray.append(resultAsDict)

    return returnArray

def convertToDict(result):
    colnames = ['ID','Material', 'Name', 'Density', 'EmbodiedCarbon']
    elem = {}

    if result:
        for i , colName in enumerate(colnames):
            value = result[i]
            elem[colName] = value
    return elem

x = getAll()
print(x)