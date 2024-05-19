# user.py
import hashlib
import hashlib
import pyodbc
from db import DatabaseConnection
class User:
    def __init__(self, db):
        self.db = db

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def register(self, username, password):
        try:
            self.db.cursor.execute("INSERT INTO Users (Username, Password) VALUES (?, ?)", (username, self.hash_password(password)))
            self.db.commit()
            print("User registered successfully!")
        except pyodbc.IntegrityError:
            print("Username already exists.")

    def login(self, username, password):
        self.db.cursor.execute("SELECT UserID FROM Users WHERE Username = ? AND Password = ?", (username, self.hash_password(password)))
        row = self.db.cursor.fetchone()
        if row:
            print("Login successful!")
            return row.UserID
        else:
            print("Invalid username or password.")
            return None
