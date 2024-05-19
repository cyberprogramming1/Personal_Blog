create database PersonalBlog;

-- Table for users
CREATE TABLE Users (
    UserID INT PRIMARY KEY IDENTITY(1,1),
    Username NVARCHAR(50) NOT NULL UNIQUE,
    Password NVARCHAR(255) NOT NULL
);

CREATE TABLE Posts (
    PostID INT PRIMARY KEY IDENTITY(1,1),
    UserID INT FOREIGN KEY REFERENCES Users(UserID),
    Title NVARCHAR(100) NOT NULL,
    Content NVARCHAR(MAX) NOT NULL,
    CreatedAt DATETIME DEFAULT GETDATE()
);
CREATE TABLE Comments (
    CommentID INT PRIMARY KEY IDENTITY(1,1),
    PostID INT FOREIGN KEY REFERENCES Posts(PostID),
    UserID INT FOREIGN KEY REFERENCES Users(UserID),
    Content NVARCHAR(MAX) NOT NULL,
    CreatedAt DATETIME DEFAULT GETDATE()
);

-- Create Tags table
CREATE TABLE Tags (
    TagID INT PRIMARY KEY IDENTITY(1,1),
    Name NVARCHAR(50) UNIQUE NOT NULL
);

-- Create PostTags table (Many-to-Many relationship between Posts and Tags)
CREATE TABLE PostTags (
    PostID INT FOREIGN KEY REFERENCES Posts(PostID),
    TagID INT FOREIGN KEY REFERENCES Tags(TagID),
    CONSTRAINT PK_PostTags PRIMARY KEY (PostID, TagID)

);
ALTER TABLE Posts
ALTER COLUMN Title NVARCHAR(255)  -- Or your desired length


select * from Users;
select * from	Posts;
select * from Comments;
select * from Tags;
select * from PostTags;

delete Users;
delete Posts;
delete Comments;
delete Tags;
delete PostTags;





DBCC CHECKIDENT ('Users', RESEED, 0);
DBCC CHECKIDENT ('Posts', RESEED, 0);
DBCC CHECKIDENT ('Comments', RESEED, 0);
DBCC CHECKIDENT ('Tags', RESEED, 0);