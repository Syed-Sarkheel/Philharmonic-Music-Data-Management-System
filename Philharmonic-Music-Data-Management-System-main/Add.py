from tkinter import *
from PIL import ImageTk, Image
import sqlite3


def add_songs():
    global title_box, artist_box, genre_box, release_year_box, language_box, album_box
    root = Toplevel()
    root.title("Add Songs")
    root.geometry("1200x720+30+30")
    # Background Image
    bg = ImageTk.PhotoImage(file="add.jpg")
    Label(root, image=bg).place(x=0, y=0, relwidth=1, relheight=1)

    # Creating Frame for title
    Add_songs = Frame(root)
    Label(Add_songs, text="Add Songs", font=("Ariel", 30, "bold"), fg="#FC46AA").place(x=0, y=0)
    Add_songs.place(x=500, y=30, height=50, width=215)

    Label(root, text="Title: ", font=("Comic Sans", 16, "italic"), fg="#FC46AA").place(x=250, y=200)
    Label(root, text="Artist Name: ", font=("Comic Sans", 16, "italic"), fg="#FC46AA").place(x=250, y=250)
    Label(root, text="Genre: ", font=("Comic Sans", 16, "italic"), fg="#FC46AA").place(x=250, y=300)
    Label(root, text="Release Year: ", font=("Comic Sans", 16, "italic"), fg="#FC46AA").place(x=250, y=350)
    Label(root, text="Language: ", font=("Comic Sans", 16, "italic"), fg="#FC46AA").place(x=250, y=400)
    Label(root, text="Album: ", font=("Comic Sans", 16, "italic"), fg="#FC46AA").place(x=250, y=450)

    title_box = Entry(root, font=("ariel", 14), bg="white")
    title_box.place(x=420, y=200, height=30, width=500)

    artist_box = Entry(root, font=("ariel", 14), bg="white")
    artist_box.place(x=420, y=250, height=30, width=500)

    genre_box=Entry(root, font=("ariel", 14), bg="white")
    genre_box.place(x=420,y=300,height=30,width=500)

    release_year_box=Entry(root, font=("ariel", 14), bg="white")
    release_year_box.place(x=420,y=350,height=30,width=500)

    language_box=Entry(root, font=("ariel", 14), bg="white")
    language_box.place(x=420,y=400,height=30,width=500)

    album_box = Entry(root, font=("ariel", 14), bg="white")
    album_box.place(x=420,y=450,height=30,width=500)

    def add():

        # Creating database connection
        conn = sqlite3.connect('song_book.db')
        # create cursor
        c = conn.cursor()

        data_insert_query = ''' INSERT INTO songs (song_name, artist_name, genre ,release_date, language, album_name) VALUES (?, ?, ?, ?, ?, ?)'''
        data_insert_tupple= (title_box.get(), artist_box.get(), genre_box.get(), release_year_box.get(), language_box.get(), album_box.get())

        c.execute(data_insert_query, data_insert_tupple)

        data_insert_query1 = ''' INSERT INTO album ( album_name, artist_name,song_name, release_date) VALUES (?, ?, ?, ?)'''
        data_insert_tupple1= (album_box.get(), artist_box.get(), title_box.get(), release_year_box.get())
        c.execute(data_insert_query1, data_insert_tupple1)

        data_insert_query2 = ''' INSERT INTO artist ( album_name, artist_name, song_name) VALUES (?, ?, ?)'''
        data_insert_tupple2= (album_box.get(), artist_box.get(), title_box.get())
        c.execute(data_insert_query2, data_insert_tupple2)   
    
        # Commit changes
        conn.commit()
        # closing connection
        conn.close()

        title_box.delete(0, END)
        artist_box.delete(0, END)
        genre_box.delete(0, END)
        release_year_box.delete(0, END)
        language_box.delete(0, END)
        album_box.delete(0, END)

    Add_button = Button(root, text="ADD", fg="#FC46AA", font=("times new roman", 22), command=add).place(x=400, y=530)
    Cancel_button = Button(root, text="CANCEL", fg="#FC46AA", font=("times new roman", 22), command=root.destroy).place(x=700, y=530)
    root.mainloop()


