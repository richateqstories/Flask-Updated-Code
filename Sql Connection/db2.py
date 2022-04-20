import mysql.connector

db = mysql.connector.connect(host='localhost',user='root',passwd='',database='8ampython')

cur = db.cursor()

cur.execute("INSERT INTO STUDENT VALUES(2,'Vishnu','vishnu@gmail.com' )")

db.commit()

db.close()