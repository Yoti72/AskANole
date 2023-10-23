from flask import Flask, render_template, request, redirect
app = Flask(__name__)
import sqlite3
import Setup
import random


#Route to home page
@app.route('/', methods = ['POST', 'GET'])
def index():
    return render_template('LoginScreen.html')

#Route to sign up page
@app.route('/signup', methods = ['POST', 'GET'])
def signup():
    return render_template('SignUp.html')


if __name__ == "__main__":
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.close()
    app.run()
