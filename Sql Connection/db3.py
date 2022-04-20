from re import I
import mysql.connector

db = mysql.connector.connect(host='localhost',user='root',passwd='',database='8ampython')

cur = db.cursor()

cur.execute('SELECT * FROM STUDENT')

data = cur.fetchall()

for i in data:
    print(i)

db.close()