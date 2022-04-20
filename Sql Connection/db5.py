import mysql.connector


def up():
    db = mysql.connector.connect(host='localhost',user='root',passwd='',database='8ampython')
    cur = db.cursor()
    cur.execute("UPDATE STUDENT SET name = 'Rahul' WHERE ID = '1'  ")
    db.commit()
    db.close()

def cre():
    db = mysql.connector.connect(host='localhost',user='root',passwd='',database='8ampython')
    cur = db.cursor()
    cur.execute('CREATE TABLE STUDENT(id INTEGER PRIMARY KEY, name VARCHAR(255),email VARCHAR(255))')
    db.commit()
    db.close()

def re():
    db = mysql.connector.connect(host='localhost',user='root',passwd='',database='8ampython')
    cur = db.cursor()
    cur.execute('SELECT * FROM STUDENT')
    data = cur.fetchall()
    for i in data:
        print(i)
    db.close()

def ins():
    db = mysql.connector.connect(host='localhost',user='root',passwd='',database='8ampython')
    cur = db.cursor()
    cur.execute("INSERT INTO STUDENT VALUES(7,'Richa','richa@gmail.com' )")
    db.commit()
    db.close()

up()
re()
ins()