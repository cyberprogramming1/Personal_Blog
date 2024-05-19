# tag.py
import pyodbc
from db import DatabaseConnection
class Tag:
    def __init__(self, db):
        self.db = db

    def add_tag(self, name):
        try:
            self.db.cursor.execute("INSERT INTO Tags (Name) VALUES (?)", (name,))
            self.db.commit()
            print("Tag added successfully!")
        except pyodbc.IntegrityError:
            print("Tag already exists.")

    def tag_post(self, post_id, tag_name):
        self.db.cursor.execute("SELECT TagID FROM Tags WHERE Name = ?", (tag_name,))
        row = self.db.cursor.fetchone()
        if not row:
            self.add_tag(tag_name)
            self.db.cursor.execute("SELECT TagID FROM Tags WHERE Name = ?", (tag_name,))
            row = self.db.cursor.fetchone()
        tag_id = row.TagID
        self.db.cursor.execute("INSERT INTO PostTags (PostID, TagID) VALUES (?, ?)", (post_id, tag_id))
        self.db.commit()
        print("Tag added to post successfully!")
