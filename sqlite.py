import sqlite3


def insertDataIn(titleText, contentText):
    connect = sqlite3.connect('flaskBlogDB.sqlite')
    c = connect.cursor()
    try:
        c.execute('''CREATE TABLE posts
                    (titleText, contentText);''')
        c.execute("INSERT INTO posts VALUES (?, ?)", (titleText, contentText))
        connect.commit()
    except:
        c.execute("INSERT INTO posts VALUES (?, ?)", (titleText, contentText))
        connect.commit()


def selectData():
    try:
        connect = sqlite3.connect('flaskBlogDB.sqlite')
        c = connect.cursor()
        c.execute("SELECT * FROM posts")
        return c.fetchall()
    except:
        return "No posts were found"
        
        
        
 