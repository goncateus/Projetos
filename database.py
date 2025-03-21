import sqlite3

DB_NAME = 'pessoas.db'

def connect():
    return sqlite3.connect(DB_NAME)

def create_tables():
    with connect() as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS pessoas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                endereco TEXT NOT NULL,
                telefone TEXT NOT NULL
            )
        ''')

