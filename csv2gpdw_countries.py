import pymysql
import csv

mydb = pymysql.connect('gpdw.inmz.net','megan','********','tmp')

cursor = mydb.cursor()

count = 0

with open('countries.csv') as mycsv:
    reader = csv.reader(mycsv)
    for row in reader:
        count+=1
        if count == 1:
            continue

        query = """INSERT INTO  Countries(id, alpha2, alpha3, name, targetable)
                   VALUES (%s, %s, %s, %s,%s)"""
            
        cursor.execute(query, row)

mydb.commit()
mydb.close()
