import mysql.connector

db = mysql.connector.connect(host='localhost',user='root',passwd='',database='8ampython')

cur = db.cursor()

cur.execute('CREATE TABLE STUDENT(id INTEGER PRIMARY KEY, name VARCHAR(255),email VARCHAR(255))')

db.commit()

db.close()