import sqlite3
import config

class UserData:
    def __init__(self, db_path=config.BOT_DB):
        self.db_path = db_path
        self.conn = sqlite3.connect(self.db_path)
        self.create_table()

    def create_table(self):
        with self.conn:
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS user_data (
                    id TEXT UNIQUE ,
                    first_name TEXT,
                    last_name TEXT,
                    username TEXT,
                    phhone TEXT,
                    location TEXT
                )
            ''')
    def add_user(self, user_id):
        with self.conn:
            self.conn.execute('''
                INSERT OR IGNORE INTO user_data (id)
                VALUES (?)
            ''', (user_id,))

    def has_joined(self, user_id):
        cursor = self.conn.cursor()
        cursor.execute('''
            SELECT COUNT(*) FROM user_data WHERE id = ?
        ''', (user_id,))
        count = cursor.fetchone()[0]
        return count > 0

    def create_user(self,column, values , user_id):
        with self.conn:
            self.conn.execute(f'''
                UPDATE user_data
                SET {column} = ?
                WHERE id = ?
            ''', (*values, user_id))