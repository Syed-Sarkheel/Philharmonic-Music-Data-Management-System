from tkinter import *
from PIL import ImageTk, Image
from viewAll import *
from create_playlist import *

def user():
    root = Toplevel()
    root.title("USER PAGE")
    root.geometry("1200x720+30+30")

    # Backgroung Image
    bg = ImageTk.PhotoImage(file="denis-istomin-fire2.jpg")
    Label(root, image=bg).place(x=0, y=0, relwidth=1, relheight=1)

    # View playlists button
    Button(root, text="  VIEW ALL SONGS  ", font=("Comic Sans", 35, "bold"), fg="#6F4E37", command=viewallsongs).place(x=350, y=230)
    # Create PLaylist button
    Button(root, text="CREATE PLAYLIST", font=("Comic Sans", 35, "bold"), fg="#6F4E37", command=create).place(x=350, y=400)



    root.mainloop()


