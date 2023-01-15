import sqlite3
from tkinter import *
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk

conn = sqlite3.connect('song_book.db')
c = conn.cursor()


def viewallsongs():
    root = Tk()
    root.title("View All Songs")
    root.minsize(width=40, height=4)
    root.geometry("1000x400")


    tree = ttk.Treeview(root, column=("c1", "c2", "c3", "c4", "c5", "c6"), show='headings')
    tree.column("#1", anchor=tk.CENTER)
    tree.heading("#1", text="Song Name")
    tree.column("#2", anchor=tk.CENTER)
    tree.heading("#2", text="Artist Name")
    tree.column("#3", anchor=tk.CENTER)
    tree.heading("#3", text="Genre")
    tree.column("#4", anchor=tk.CENTER)
    tree.heading("#4", text="Release Year")
    tree.column("#5", anchor=tk.CENTER)
    tree.heading("#5", text="Language")
    tree.column("#6", anchor=tk.CENTER)
    tree.heading("#6", text="Album Name")
    tree.grid(sticky=(N, S, W, E))
    root.treeview = tree
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    tree.grid(row=0, column=0, sticky='nsew')
    scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.grid(row=0, column=1, sticky='ns')
    ttk.Button(root, text="Close", command=root.destroy).grid(row=1, column=0, rowspan=3)

    try:
        c.execute("SELECT DISTINCT song_name,artist_name,genre,release_date,language,album_name FROM songs ")
        rows = c.fetchall()
        conn.commit()
        for i in rows:
            tree.insert("", tk.END, values=i)


    except:
        messagebox.showinfo('Error', "Failed To Fetch Songs From The Database")

    root.mainloop()
