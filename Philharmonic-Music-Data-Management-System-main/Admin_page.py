from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
from delete import *
from Add import *
import sqlite3
from viewAll import *

def admin():

    root = Toplevel()
    root.title("ADMIN PAGE")
    root.geometry("1200x720+30+30")

    # Background Image
    bg = ImageTk.PhotoImage(file="admin.jpg")
    Label(root, image=bg).place(x=0, y=0, relwidth=1, relheight=1)

    # title
    Label(root, text="          ADMIN FUNCTIONS           ", font=("Ariel", 20, "bold"), fg="#FC46AA", padx=20, pady=20).place(x=400, y=180)


    # buttons
    add = Button(root, text= "          Add Track            ", fg = "#FC46AA", font = ("times new roman", 18), command = add_songs).place(x = 500, y = 295)
    view = Button(root,text = "         View Tracks          ", fg = "#FC46AA", font = ("times new roman",18), command = viewallsongs).place(x = 500,y = 368)
    delete = Button(root,text= "       Delete Tracks          ", fg = "#FC46AA", font = ("times new roman", 18), pady = 5, command = delete_song).place(x = 500,y = 442)

    root.mainloop()


