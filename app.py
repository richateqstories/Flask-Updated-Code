


from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

#This is a function to read data
@app.route("/index")
@app.route('/')
def list():
    conn = sqlite3.connect('test.db')
    conn.row_factory=sqlite3.Row
    cur = conn.cursor()
    cur.execute('SELECT * FROM contacts')
    rows = cur.fetchall()
    return render_template('index.html',rows=rows)

#This is a function to insert data 
@app.route('/add_data',methods=['GET','POST'])
def add_data():
    if request.method == 'GET':
        return render_template('add_data_form.html')

    elif request.method =='POST':
        try:
            name = request.form['name']
            contact = request.form['contact']
            print(name,contact)
            conn = sqlite3.connect('test.db')
            cur = conn.cursor()
            cur.execute('INSERT INTO contacts(name,number) VALUES(?,?)',(name,contact))
            conn.commit()
            msg="Contact successfully saved"

        except:
            conn.rollback()
            msg="Failed to save contact"

        finally:
            return render_template('msg.html',msg=msg)


#this is a function to edit data
@app.route('/edit/<sl>',methods=['GET','POST'])
def edit_data(sl):
    id=(sl)
    id1 = (sl,)
    if request.method =='GET':
        conn = sqlite3.connect('test.db')
        conn.row_factory=sqlite3.Row
        cur = conn.cursor()
        cur.execute('SELECT * FROM contacts WHERE sl= (?)',(id1))
        rows = cur.fetchone()
        return render_template('edit.html',rows=rows)
    
    elif request.method =='POST':
        try:
            name = request.form['name']
            contact = request.form['contact']
            conn = sqlite3.connect('test.db')
            cur = conn.cursor()
            cur.execute('UPDATE contacts SET name=(?),number=(?) WHERE sl=(?)',(name,contact,id))
            conn.commit()
            msg="Contact successfully updated"

        except:
            conn.rollback()
            msg="Failed to update contact"

        finally:
            return render_template('msg.html',msg=msg)

#this is a function to delete data
@app.route('/delete/<sl>',methods=['GET','POST'])
def delete_data(sl):
    id=(sl,)
    if request.method =='GET':
        conn = sqlite3.connect('test.db')
        conn.row_factory=sqlite3.Row
        cur = conn.cursor()
        cur.execute('SELECT * FROM contacts WHERE sl =(?)',(id))
        rows = cur.fetchone()
        return render_template('delete.html',rows=rows)
    
    elif request.method =='POST':
        try:
            
            conn = sqlite3.connect('test.db')
            cur = conn.cursor()
            cur.execute('DELETE FROM contacts  WHERE sl=(?)',(id))
            conn.commit()
            msg="Contact successfully deleted"

        except:
            conn.rollback()
            msg="Failed to delete contact"

        finally:
            return render_template('msg.html',msg=msg)       
        





if __name__=='__main__':
    app.run(debug=True,port=80)