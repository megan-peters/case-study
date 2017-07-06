import pymysql
import csv

mydb = pymysql.connect('gpdw.inmz.net','megan','MeeNgie9','tmp')

cursor = mydb.cursor()

count = 0

with open('regions.csv') as mycsv:
    reader = csv.reader(mycsv)
    for row in reader:
        count+=1
        if count == 1:
            continue


        query = """INSERT INTO  Regions(id, country_id, name, iso_code)
                   VALUES (%s, %s, %s, %s)"""
            
        cursor.execute(query, row)

mydb.commit()
mydb.close()

