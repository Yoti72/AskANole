import sqlite3

def start_db():
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
            PostId INTEGER,
            CommentId INTEGER PRIMARY KEY AUTOINCREMENT,
            Content TEXT,
            Author TEXT
        )
    ''')
    cursor.close()