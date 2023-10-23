import sqlite3

#Create database with Tables: Login, Comments, Likes, Messages
conn = sqlite3.connect('database.db')
cursor = conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS Login (Username TEXT, Password TEXT, First TEXT, Last TEXT, FSUID TEXT, ProfilePic INT)')
Cursor.execute('CREATE TABLE IF NOT EXISTS Posts (Username TEXT, PostType INT, Title TEXT, Description TEXT)')
Cursor.execute('CREATE TABLE IF NOT EXISTS Replies (PrimaryUser TEXT, SecondaryUser TEXT, Title TEXT, UserResponding TEXT, Index INT)')

cursor.close()


