import sqlite3

# Creating database connection
conn = sqlite3.connect('song_book.db')
# create cursor
c = conn.cursor()

#Songname, artist_name, genre, relaease year, language, Album_name
# Creating table


c.execute("""CREATE TABLE admin(
    admin_name text,
    password text
    )""")

c.execute("""CREATE TABLE user(
    user_name text,
    password text
    )""")

c.execute("""CREATE TABLE songs(
    song_name text,
    artist_name text,
    genre text,
    release_date text,
    language text,
    album_name text
    )""")

c.execute("""CREATE TABLE album(
    album_name text,
    artist_name text,
    FOREIGN KEY(artist_name) REFERENCES SONG(artist_name)
    FOREIGN KEY(album_name) REFERENCES SONG(album_name)
    )""")
c.execute("INSERT INTO admin (admin_name, password) VALUES ('Maxson', 'Maxson@123')")    
c.execute("INSERT INTO admin (admin_name, password) VALUES ('admin', '123')")
c.execute("INSERT INTO admin (admin_name, password) VALUES ('admin2', '223')")
c.execute("INSERT INTO user (user_name, password) VALUES ('Sarkheel', '1223')")
c.execute("INSERT INTO user (user_name, password) VALUES ('user', '123')")
c.execute("INSERT INTO user (user_name, password) VALUES ('user1', '1233')")


# Commit changes
conn.commit()
# closing connection
conn.close()

