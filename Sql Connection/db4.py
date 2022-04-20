import mysql.connector

db = mysql.connector.connect(host='localhost',user='root',passwd='',database='8ampython')

cur = db.cursor()

cur.execute("UPDATE STUDENT SET name = 'TEJUS' WHERE ID = '1'  ")

db.commit()

db.close()