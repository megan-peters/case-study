import pymysql

city = input("City: ")

mydb = pymysql.connect('gpdw.inmz.net','megan','********','tmp')

cursor = mydb.cursor()

count = 0

count_dict = {
    0: 'City id: ',
    1: 'Country id: ',
    2: 'City iso code: ',
    3: 'Country alpha2: ',
    4: 'Country alpha3: ',
    5: 'Country name: ',
    6: 'Country targetable: ',
    7: 'Region id: ',
    8: 'Region name: ',
    9: 'Region iso code:'
}

query = f"""
         SELECT Cities.id, Cities.country_id, Cities.iso_code, 
         Countries.alpha2, Countries.alpha3,
         Countries.name, Countries.targetable,
         Cities.region_id, Regions.name, Regions.iso_code 
         FROM Cities JOIN Regions ON Regions.id = Cities.region_id 
         JOIN Countries ON Regions.country_id = Countries.id
         WHERE Cities.name = "{city}"
         """

query2 = f"""
          SELECT Cities.id, Cities.country_id, Cities.iso_code, 
          Countries.alpha2, Countries.alpha3,
          Countries.name, Countries.targetable 
          FROM Cities JOIN Countries ON Cities.country_id = Countries.id
          WHERE Cities.name = "{city}"
          """

cursor.execute(
    f"""
     SELECT COUNT(*) FROM Cities 
     WHERE name = "{city}" AND region_id IS NULL
     """
)

check_null = cursor.fetchone()

if check_null == (1,):
    cursor.execute(query2)
    for row in (cursor.fetchall()):
        for i in row:
            print(count_dict[count], end = '')
            print(i)
            print()
            count += 1

else:
    cursor.execute(query)
    for row in (cursor.fetchall()):
        for i in row:
            print(count_dict[count], end = '')
            print(i)
            print()
            count += 1

mydb.close()
