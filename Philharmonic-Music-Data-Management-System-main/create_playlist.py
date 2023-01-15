from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
from delete import *
from Add import *
import sqlite3
from viewAll import *


def create():
      root = Toplevel()
      root.title("PLAYLIST PAGE")
      root.geometry("1200x720+30+30")

      # Background Image
      bg = ImageTk.PhotoImage(file="playlist.jpg")
      Label(root, image=bg).place(x=0, y=0, relwidth=1, relheight=1)

      # title
      Label(root, text="  CREATE PLAYLIST BASED ON  ", font=("Ariel", 25, "bold"), fg="#FC46AA", padx=10, pady=10).place(
      x=400, y=180)

      # labels
      genre_lab = Label(root, text=" GENRE: ", fg="#FC46AA", font=("times new roman", 18))
      genre_lab.place(x=180, y=300)
      year_lab = Label(root, text=" YEAR OF RELEASE: ", fg="#FC46AA", font=("times new roman", 18))
      year_lab.place(x=180, y=360)
      language_lab = Label(root, text=" LANGUAGE: ", fg="#FC46AA", font=("times new roman", 18))
      language_lab.place(x=180, y=420)
      album_lab = Label(root, text=" ALBUM: ", fg="#FC46AA", font=("times new roman", 18))
      album_lab.place(x=180, y=480)

      # entry boxes
      genre_in = StringVar()
      year_in = StringVar()
      language_in = StringVar()
      album_in = StringVar()
      genre_input = Entry(root, font=("ariel", 14), width=40, textvariable=genre_in)
      genre_input.place(x=450, y=305)
      year_input = Entry(root, font=("ariel", 14), width=40, textvariable=year_in)
      year_input.place(x=450, y=365)
      language_input = Entry(root, font=("ariel", 14), width=40, textvariable=language_in)
      language_input.place(x=450, y=425)
      album_input = Entry(root, font=("ariel", 14), width=40, textvariable=album_in)
      album_input.place(x=450, y=485)

      def gen_create(name):
            genre_input.delete(0, END)

            root1 = Toplevel()
            root1.title("View All Songs")
            root1.minsize(width=40, height=4)
            root1.geometry("1000x400")
            conn = sqlite3.connect('song_book.db')
            c = conn.cursor()

            tree = ttk.Treeview(root1, column=("c1", "c2", "c3", "c4", "c5", "c6"), show='headings')
            tree.column("#1", anchor=CENTER)
            tree.heading("#1", text="Song Name")
            tree.column("#2", anchor=CENTER)
            tree.heading("#2", text="Artist Name")
            tree.column("#3", anchor=CENTER)
            tree.heading("#3", text="Genre")
            tree.column("#4", anchor=CENTER)
            tree.heading("#4", text="Release Year")
            tree.column("#5", anchor=CENTER)
            tree.heading("#5", text="Language")
            tree.column("#6", anchor=CENTER)
            tree.heading("#6", text="Album Name")
            tree.grid(sticky=(N, S, W, E))
            root1.treeview = tree
            root1.grid_rowconfigure(0, weight=1)
            root1.grid_columnconfigure(0, weight=1)
            tree.grid(row=0, column=0, sticky='nsew')
            scrollbar = ttk.Scrollbar(root1, orient=VERTICAL, command=tree.yview)
            tree.configure(yscroll=scrollbar.set)
            scrollbar.grid(row=0, column=1, sticky='ns')
            ttk.Button(root1, text="Close", command=root1.destroy).grid(row=1, column=0, rowspan=3)

            try:
                  c.execute("SELECT song_name,artist_name,genre,release_date,language,album_name FROM songs WHERE genre = ?", (name,))
                  rows = c.fetchall()
                  conn.commit()
                  for i in rows:
                        tree.insert("", END, values=i)

            except:
                  messagebox.showinfo('Error', "Failed To Fetch Songs From The Database")

      def year_create(name):
            year_input.delete(0, END)

            root1 = Toplevel()
            root1.title("View All Songs")
            root1.minsize(width=40, height=4)
            root1.geometry("1000x400")
            conn = sqlite3.connect('song_book.db')
            c = conn.cursor()

            tree = ttk.Treeview(root1, column=("c1", "c2", "c3", "c4", "c5", "c6"), show='headings')
            tree.column("#1", anchor=CENTER)
            tree.heading("#1", text="Song Name")
            tree.column("#2", anchor=CENTER)
            tree.heading("#2", text="Artist Name")
            tree.column("#3", anchor=CENTER)
            tree.heading("#3", text="Genre")
            tree.column("#4", anchor=CENTER)
            tree.heading("#4", text="Release Year")
            tree.column("#5", anchor=CENTER)
            tree.heading("#5", text="Language")
            tree.column("#6", anchor=CENTER)
            tree.heading("#6", text="Album Name")
            tree.grid(sticky=(N, S, W, E))
            root1.treeview = tree
            root1.grid_rowconfigure(0, weight=1)
            root1.grid_columnconfigure(0, weight=1)
            tree.grid(row=0, column=0, sticky='nsew')
            scrollbar = ttk.Scrollbar(root1, orient=VERTICAL, command=tree.yview)
            tree.configure(yscroll=scrollbar.set)
            scrollbar.grid(row=0, column=1, sticky='ns')
            ttk.Button(root1, text="Close", command=root1.destroy).grid(row=1, column=0, rowspan=3)

            try:
                  c.execute("SELECT song_name,artist_name,genre,release_date,language,album_name FROM songs WHERE release_date = ?", (name,))
                  rows = c.fetchall()
                  conn.commit()
                  for i in rows:
                        tree.insert("", END, values=i)

            except:
                  messagebox.showinfo('Error', "Failed To Fetch Songs From The Database")

      def lan_create(name):
            language_input.delete(0, END)

            root1 = Toplevel()
            root1.title("View All Songs")
            root1.minsize(width=40, height=4)
            root1.geometry("1000x400")
            conn = sqlite3.connect('song_book.db')
            c = conn.cursor()

            tree = ttk.Treeview(root1, column=("c1", "c2", "c3", "c4", "c5", "c6"), show='headings')
            tree.column("#1", anchor=CENTER)
            tree.heading("#1", text="Song Name")
            tree.column("#2", anchor=CENTER)
            tree.heading("#2", text="Artist Name")
            tree.column("#3", anchor=CENTER)
            tree.heading("#3", text="Genre")
            tree.column("#4", anchor=CENTER)
            tree.heading("#4", text="Release Year")
            tree.column("#5", anchor=CENTER)
            tree.heading("#5", text="Language")
            tree.column("#6", anchor=CENTER)
            tree.heading("#6", text="Album Name")
            tree.grid(sticky=(N, S, W, E))
            root1.treeview = tree
            root1.grid_rowconfigure(0, weight=1)
            root1.grid_columnconfigure(0, weight=1)
            tree.grid(row=0, column=0, sticky='nsew')
            scrollbar = ttk.Scrollbar(root1, orient=VERTICAL, command=tree.yview)
            tree.configure(yscroll=scrollbar.set)
            scrollbar.grid(row=0, column=1, sticky='ns')
            ttk.Button(root1, text="Close", command=root1.destroy).grid(row=1, column=0, rowspan=3)

            try:
                  c.execute("SELECT song_name,artist_name,genre,release_date,language,album_name FROM songs WHERE language = ?", (name,))
                  rows = c.fetchall()
                  conn.commit()
                  for i in rows:
                        tree.insert("", END, values=i)

            except:
                  messagebox.showinfo('Error', "Failed To Fetch Songs From The Database")

      def alb_create(name):
            album_input.delete(0, END)

            root1 = Toplevel()
            root1.title("View All Songs")
            root1.minsize(width=40, height=4)
            root1.geometry("1000x400")
            conn = sqlite3.connect('song_book.db')
            c = conn.cursor()

            tree = ttk.Treeview(root1, column=("c1", "c2", "c3", "c4", "c5", "c6"), show='headings')
            tree.column("#1", anchor=CENTER)
            tree.heading("#1", text="Song Name")
            tree.column("#2", anchor=CENTER)
            tree.heading("#2", text="Artist Name")
            tree.column("#3", anchor=CENTER)
            tree.heading("#3", text="Genre")
            tree.column("#4", anchor=CENTER)
            tree.heading("#4", text="Release Year")
            tree.column("#5", anchor=CENTER)
            tree.heading("#5", text="Language")
            tree.column("#6", anchor=CENTER)
            tree.heading("#6", text="Album Name")
            tree.grid(sticky=(N, S, W, E))
            root1.treeview = tree
            root1.grid_rowconfigure(0, weight=1)
            root1.grid_columnconfigure(0, weight=1)
            tree.grid(row=0, column=0, sticky='nsew')
            scrollbar = ttk.Scrollbar(root1, orient=VERTICAL, command=tree.yview)
            tree.configure(yscroll=scrollbar.set)
            scrollbar.grid(row=0, column=1, sticky='ns')
            ttk.Button(root1, text="Close", command=root1.destroy).grid(row=1, column=0, rowspan=3)

            try:
                  c.execute("SELECT song_name,artist_name,genre,release_date,language,album_name FROM songs WHERE album_name = ?", (name,))
                  rows = c.fetchall()
                  conn.commit()
                  for i in rows:
                        tree.insert("", END, values=i)

            except:
                  messagebox.showinfo('Error', "Failed To Fetch Songs From The Database")

      # buttons
      genre_btn = Button(root, text='CREATE', font=("ariel", 12, "bold"), fg="#FC46AA", width=10, command=lambda:gen_create(genre_in.get()))
      genre_btn.place(x=940, y=300)
      year_btn = Button(root, text='CREATE', font=("ariel", 12, "bold"), fg="#FC46AA", width=10, command= lambda:year_create(year_in.get()))
      year_btn.place(x=940, y=360)
      language_btn = Button(root, text='CREATE', font=("ariel", 12, "bold"), fg="#FC46AA", width=10, command= lambda : lan_create(language_in.get()))
      language_btn.place(x=940, y=420)
      album_btn = Button(root, text='CREATE', font=("ariel", 12, "bold"), fg="#FC46AA", width=10, command=lambda: alb_create(album_input.get()))
      album_btn.place(x=940, y=480)

      root.mainloop()
