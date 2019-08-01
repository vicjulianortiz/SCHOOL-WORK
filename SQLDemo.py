import sqlite3

db = sqlite3.connect('C:/Users/Victor/Desktop/CITIES.db')

cursor = db.cursor()

#cursor.execute('''
#            CREATE TABLE hurricanes(name TEXT PRIMARY KEY, category INT,
#                                    speed INT, countries TEXT, deaths INT)
#                ''')
#db.commit()

#name = 'Andres'
#category = 5
#speed = 101
#countries = 'USA'
#deaths =  402

# Insert user 1
#cursor.execute('''INSERT INTO hurricanes(name, category, speed, countries, deaths)
 #                 VALUES(?,?,?,?,?)''', (name,category, speed, countries, deaths))
#print('First user inserted')



cursor.execute(' SELECT DISTINCT CITY (SELECT * FROM S,P,J WHERE S.CITY = P.CITY AND S.CITY = J.CITY) ')
user1 = cursor.fetchall() 
print(user1) 
db.commit()


db.close()

