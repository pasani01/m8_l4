import sqlite3
from config import BOT_DB


class ObjectData:
    def __init__(self, db_path=BOT_DB):
        self.db_path = db_path
        self.conn = sqlite3.connect(self.db_path)
        self.create_table()

    def create_table(self):
        with self.conn:
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS object_data (
                    id INTEGER  PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    description TEXT,
                    price REAL,
                    category_id references category_data(id)
                )
            ''')

    def add_object(self, column, value):
        with self.conn:
            self.conn.execute(f'''
                INSERT OR IGNORE INTO object_data ({column})
                VALUES (?)
            ''', (value,))

    def add_object(self, columns, placeholders, values):
        with self.conn:
            self.conn.execute(f'''
                INSERT OR IGNORE INTO object_data ({columns})
                VALUES ({placeholders})
            ''', values)


class CatagoryData:
    def __init__(self, db_path=BOT_DB):
        self.db_path = db_path
        self.conn = sqlite3.connect(self.db_path)
        self.create_table()

    def create_table(self):
        with self.conn:
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS category_data (
                    id INTEGER  PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    description TEXT
                )
            ''')
    
    def add_category(self, columns, placeholders, values):
        with self.conn:
            self.conn.execute(f'''
                INSERT OR IGNORE INTO category_data ({columns})
                VALUES ({placeholders})
            ''', values)
    
    def get_catagory(self):
        with self.conn:
            cursor = self.conn.execute('SELECT * FROM category_data')
            return cursor.fetchall()