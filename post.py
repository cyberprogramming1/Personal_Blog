# post.py
from db import DatabaseConnection

class Post:
    def __init__(self, db):
        self.db = db

    def create_post(self, user_id, title, content):
        self.db.cursor.execute("INSERT INTO Posts (UserID, Title, Content) VALUES (?, ?, ?)", (user_id, title, content))
        self.db.commit()
    print("Post created successfully!")


    def read_posts(self):
        self.db.cursor.execute("SELECT PostID, Title, CreatedAt FROM Posts")
        rows = self.db.cursor.fetchall()
        for row in rows:
            print(f"ID: {row.PostID}, Title: {row.Title}, Created At: {row.CreatedAt}")

    def read_post(self, post_id):
        self.db.cursor.execute("SELECT * FROM Posts WHERE PostID = ?", (post_id,))
        row = self.db.cursor.fetchone()
        if row:
            print(f"ID: {row.PostID}\nTitle: {row.Title}\nContent: {row.Content}\nCreated At: {row.CreatedAt}")
        else:
            print("Post not found.")

    def update_post(self, post_id, title, content):
        self.db.cursor.execute("UPDATE Posts SET Title = ?, Content = ? WHERE PostID = ?", (title, content, post_id))
        self.db.commit()
        print("Post updated successfully!")

    def delete_post(self, post_id):
        self.db.cursor.execute("DELETE FROM Posts WHERE PostID = ?", (post_id,))
        self.db.commit()
        print("Post deleted successfully!")
