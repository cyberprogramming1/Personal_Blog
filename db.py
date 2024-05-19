# db.py
import pyodbc

class DatabaseConnection:
    def __init__(self, server, database):
        self.connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
        self.conn = pyodbc.connect(self.connection_string)
        self.cursor = self.conn.cursor()
    
    def commit(self):
        self.conn.commit()

    def close(self):
        self.cursor.close()
        self.conn.close()
