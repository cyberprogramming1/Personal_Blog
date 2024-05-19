# comment.py
from db import DatabaseConnection

class Comment:
    def __init__(self, db):
        self.db = db

    def add_comment(self, user_id, post_id, content):
        self.db.cursor.execute("INSERT INTO Comments (PostID, UserID, Content) VALUES (?, ?, ?)", (post_id, user_id, content))
        self.db.commit()
        print("Comment added successfully!")

    def read_comments(self, post_id):
        self.db.cursor.execute("SELECT c.CommentID, u.Username, c.Content, c.CreatedAt FROM Comments c JOIN Users u ON c.UserID = u.UserID WHERE c.PostID = ?", (post_id,))
        rows = self.db.cursor.fetchall()
        for row in rows:
            print(f"Comment ID: {row.CommentID}, User: {row.Username}, Content: {row.Content}, Created At: {row.CreatedAt}")

    def update_comment(self, comment_id, content):
        self.db.cursor.execute("UPDATE Comments SET Content = ? WHERE CommentID = ?", (content, comment_id))
        self.db.commit()
        print("Comment updated successfully!")
