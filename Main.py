from flask import Flask, render_template, request, redirect
app = Flask(__name__)
import sqlite3
import random


#Route to home page
@app.route('/', methods = ['POST', 'GET'])
def index():
    return render_template('LoginScreen.html')

#Route to sign up page
@app.route('/signup', methods = ['POST', 'GET'])
def signup():
    return render_template('SignUp.html')

@app.route('/signupvalid', methods = ['POST', 'GET'])
def signupvalid():
    if request.method == "POST":
        try: 
            first = request.form['First']
            last = request.form['Last']
            fsuid = request.form['Fsuid']
            username = request.form['Username']
            password = request.form['Password']
            confirmPass = request.form['ConfirmPassword']
            user = username

            con = sqlite3.connect('database.db')
            
            with sqlite3.connect('database.db') as con:
                cur = con.cursor()
                if(password == confirmPass):
                    cur.execute("INSERT INTO Login (Username,Password,First,Last,FSUID) VALUES (?,?,?,?,?)", (username, password, first, last, fsuid))
            return redirect("/")
        except:
            con.rollback()
            return render_template('Error.html')
        finally:
            con.close()

@app.route('/welcome', methods = ['POST', 'GET'])
def welcome():
    if request.method == "POST":
        try: 
            username = request.form['Username']
            password = request.form['Password']

            conn = sqlite3.connect('database.db')
            cursor = conn.cursor()

            cursor.execute("SELECT FSUID FROM Login WHERE Username = ? AND Password = ?", (username,password))
            rows = cursor.fetchall()
            if len(rows) == 0:
                return render_template("NoMatchingUser.html")
            user = rows[0][0]
            return redirect('/main')
        except:
            return redirect("/")
        finally:
            conn.close()

@app.route('/main', methods = ['POST', 'GET'])
def main():
    return render_template('MainPage.html')



if __name__ == "__main__":
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.close()
    app.run()
