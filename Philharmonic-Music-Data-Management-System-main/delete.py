from tkinter import *
import sqlite3
from PIL import ImageTk, Image

def delete_song():

    root = Toplevel()
    root.title("Deleting Song page")
    root.geometry("1200x720+30+30")

    bg = ImageTk.PhotoImage(file="delete_2.jpg")
    Label(root, image=bg).place(x=0, y=0, relwidth=1, relheight=1)

    # Page title
    Label(root, text="DELETE A SONG FROM RECORD", font=("Ariel", 30, "bold"), padx=20, pady=20, bg="#000000", fg="#FFFFFF").place(x=200, y=180)

    # labels
    Label(root, text="Song Name: ", font=("Comic Sans", 20, "italic"), bg="#000000", fg="#FFFFFF").place(x=300, y=300)
    Label(root, text="Artist Name: ", font=("Comic Sans", 20, "italic"), bg="#000000", fg="#FFFFFF").place(x=300, y=400)

    # Input fields
    song_name_box = Entry(root, font=("ariel", 20), bg="lightgray")
    song_name_box.place(x=490, y=300)
    artist_name_box = Entry(root, font=("ariel", 20), bg="lightgray")
    artist_name_box.place(x=490, y=400)

    def delete_sng(name,artist):
        # Creating database connection
        conn = sqlite3.connect('song_book.db')
        # create cursor
        c = conn.cursor()

        c.execute("DELETE FROM songs WHERE song_name = ? AND artist_name = ?", (name, artist))
        c.execute("DELETE FROM artist WHERE song_name = ? AND artist_name = ?", (name, artist))
        c.execute("DELETE FROM album WHERE song_name = ? AND artist_name = ?", (name, artist))
        
        # Commit changes
        conn.commit()
        # closing connection
        conn.close()
        song_name_box.delete(0, END)
        artist_name_box.delete(0, END)

    # Buttons for submit or quit
    Submit_btn = Button(root, text="SUBMIT", font=("Comic Sans", 25, "bold"), bg="#000000", fg="#FFFFFF", command= lambda: delete_sng(song_name_box.get(), artist_name_box.get())).place(x=300, y=500)
    quit_btn = Button(root, text="QUIT", font=("Comic Sans", 25, "bold"), bg="#000000", fg="#FFFFFF", padx=20, command=root.destroy).place(x=650, y=500)

    root.mainloop()

