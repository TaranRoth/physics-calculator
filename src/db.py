from flask import current_app, g
import sqlite3

class Table:
    def __init__(self, name):
        pass

class Database:
    def __init__(self, name, app_path):
        self.path = f"{app_path}/data/{name}"
    
    def get_db(self):
        print(self.path)
        if 'db' not in g:
            g.db = sqlite3.connect(
            self.path,
            detect_types=sqlite3.PARSE_DECLTYPES
            )
            g.db.row_factory = sqlite3.Row
        return g.db

    def close_db(self):
        db = g.pop('db', None)
        if db is not None:
            db.close()

    def init_db(self):
        db = self.get_db()
        with current_app.open_resource('src/schema.sql') as f:
            db.executescript(f.read().decode('utf8'))
