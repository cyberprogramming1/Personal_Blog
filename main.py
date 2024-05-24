# main.py

from db import DatabaseConnection
from user import User
from post import Post
from comment import Comment
from tag import Tag

#DESKTOP-VIKK52P
def main():
    db = DatabaseConnection(server='DEVICE\SQLEXPRESS', database='PersonalBlog')


    user_manager = User(db)
    post_manager = Post(db)
    comment_manager = Comment(db)
    tag_manager = Tag(db)

    current_user = None
    while True:
        if not current_user:
            print("\nPersonal Blog Console\n1. Register\n2. Login\n3. Exit")
            choice = input("Enter your choice: ")
            if choice == '1':
                username = input("Enter username: ")
                password = input("Enter password: ")
                user_manager.register(username, password)
            elif choice == '2':
                username = input("Enter username: ")
                password = input("Enter password: ")
                current_user = user_manager.login(username, password)
            elif choice == '3':
                break
            else:
                print("Invalid choice, please try again.")
        else:
            print("\nPersonal Blog Console\n1. Create Post\n2. Read All Posts\n3. Read Post by ID\n4. Update Post\n5. Delete Post\n6. Add Comment\n7. Read Comments\n8. Tag Post\n9. Logout")
            choice = input("Enter your choice: ")
            
            if choice == '1':
                title = input("Enter title: ")
                content = input("Enter content: ")
                post_manager.create_post(current_user, title, content)
            elif choice == '2':
                post_manager.read_posts()
            elif choice == '3':
                post_id = int(input("Enter post ID: "))
                post_manager.read_post(post_id)
            elif choice == '4':
                post_id = int(input("Enter post ID: "))
                title = input("Enter new title: ")
                content = input("Enter new content: ")
                post_manager.update_post(post_id, title, content)
            elif choice == '5':
                post_id = int(input("Enter post ID: "))
                post_manager.delete_post(post_id)
            elif choice == '6':
                post_id = int(input("Enter post ID: "))
                content = input("Enter comment: ")
                comment_manager.add_comment(current_user, post_id, content)
            elif choice == '7':
                post_id = int(input("Enter post ID: "))
                comment_manager.read_comments(post_id)
            elif choice == '8':
                post_id = int(input("Enter post ID: "))
                tag_name = input("Enter tag name: ")
                tag_manager.tag_post(post_id, tag_name)
            elif choice == '9':
                current_user = None
            else:
                print("Invalid choice, please try again.")
    
    db.close()

if __name__ == "__main__":
    main()
