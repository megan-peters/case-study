import pymysql
import ast

mydb = pymysql.connect('gpdw.inmz.net','megan','MeeNgie9','tmp')

cursor = mydb.cursor()

count = 0

reader = open("cities.csv")
for row in reader.readlines():
	row = ast.literal_eval(row)
	i = row["id"]
	c = row["country_id"]
	try:
		r = row["region_id"]
	except KeyError:
		r = 'NULL'
	n = row["name"]
	ic = row["iso_code"]

	query = f"""INSERT INTO Cities (id, country_id, region_id, name, iso_code)
                VALUES ({i},{c},{r},"{n}","{ic}")"""
            
	cursor.execute(query)

mydb.commit()
mydb.close()
