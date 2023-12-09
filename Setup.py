import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Login (
        FSUID TEXT,
        Password TEXT,
        First TEXT,
        Last TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Posts (
        Id INTEGER PRIMARY KEY AUTOINCREMENT,
        FSUID TEXT,
        Title TEXT,
        Description TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Replies (
        PrimaryUser TEXT,
        SecondaryUser TEXT,
        Message TEXT,
        Ind INTEGER PRIMARY KEY AUTOINCREMENT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Comments (
        post_id INTEGER,
        comment_id INTEGER,
        content TEXT,
        author TEXT,
        PRIMARY KEY (post_id, comment_id),
        FOREIGN KEY (post_id) REFERENCES YourTable(id)
    )
''')
cursor.close()
