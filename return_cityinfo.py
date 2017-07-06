import pymysql

city = input("City: ")

mydb = pymysql.connect('gpdw.inmz.net','megan','MeeNgie9','tmp')

cursor = mydb.cursor()

count = 0

query = f"""
         SELECT Cities.id, Cities.country_id,Cities.region_id, Cities.iso_code, Regions.name, Regions.iso_code, Countries.alpha2, Countries.alpha3, Countries.name, Countries.targetable
         FROM Cities JOIN Regions ON Regions.id = Cities.region_id JOIN Countries ON Regions.country_id = Countries.id
         WHERE Cities.name = "{city}"
         """

query2 = f"""
		  SELECT Cities.id, Cities.country_id, Cities.iso_code, Countries.alpha2, Countries.alpha3, Countries.name, Countries.targetable 
		  FROM Cities JOIN Countries ON Cities.country_id = Countries.id
		  WHERE Cities.name = "{city}"
		  """

cursor.execute(f"""SELECT COUNT(*) FROM Cities WHERE name = "{city}" AND region_id IS NULL""")
check_null = cursor.fetchone()

if check_null == (1,):
	cursor.execute(query2)
	for row in (cursor.fetchall()):
		for i in row:
			if count == 0:
				print('City id: ', end = '')
			elif count == 1:
				print('Country id: ', end = '')
			elif count == 2:
				print('City iso code: ', end = '')
			elif count == 3:
				print('Country alpha2: ', end = '')
			elif count == 4:
				print('Country alpha3: ', end = '')
			elif count == 5:
				print('Country name: ', end = '')
			else:
				print('Country targetable: ', end = '')
			print(i)
			print()
			count += 1

else:
	cursor.execute(query)
	for row in (cursor.fetchall()):
		for i in row:
			if count == 0:
				print('City id: ', end = '')
			elif count == 1:
				print('Country id: ', end = '')
			elif count == 2:
				print('Region id: ', end = '')
			elif count == 3:
				print('City iso code: ', end = '')
			elif count == 4:
				print('Region name: ', end = '')
			elif count == 5:
				print('Region iso code: ', end = '')
			elif count == 6:
				print('Country alpha2: ', end = '')
			elif count == 7:
				print('Country alpha3: ', end = '')
			elif count == 8:
				print('Country name: ', end = '')
			else:
				print('Country targetable: ', end = '')
			print(i)
			print()
			count += 1
		

mydb.close()