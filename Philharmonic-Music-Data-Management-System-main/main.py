from tkinter import *
from PIL import ImageTk, Image
from Admin_page import *
from User_page import *
import sqlite3
from tkinter import messagebox

root = Tk()
root.title("Login Page")
root.geometry("1200x720+30+30")

a_input = StringVar()
a_pass = StringVar()
u_input = StringVar()
u_pass = StringVar()

# Background image defining
bg = ImageTk.PhotoImage(file="login.png")
Label(root, image=bg).place(x=0, y=0, relwidth=1, relheight=1)
Label(root, text="LOGIN PAGE")

# page title
Label(root, text="WELCOME TO PHILHARMONIC MUSIC APP", font=("Ariel", 20, "bold"), fg="#FC46AA", padx=20, pady=20).place(
    x=280, y=180)

# defining frame for admin login
frame_1 = Frame(root, padx=20, pady=20)
frame_1.place(x=80, y=400, height=250, width=450)

# widgets inside frame_1
Label(frame_1, text="ADMIN", font=("Comic Sans", 30, "bold"), fg="#FC46AA").place(x=120, y=20)
Label(frame_1, text="Username: ", font=("Comic Sans", 16, "italic"), fg="#FC46AA").place(x=20, y=100)
Label(frame_1, text="Password: ", font=("Comic Sans", 16, "italic"), fg="#FC46AA").place(x=20, y=140)

# write blocks
admin_name = Entry(frame_1, font=("ariel", 14), bg="lightgray", textvariable=a_input)
admin_name.place(x=130, y=105)
admin_psw = Entry(frame_1, font=("ariel", 14), bg="lightgray", textvariable=a_pass)
admin_psw.place(x=130, y=145)


# defining frame for user login
frame_2 = Frame(root, padx=20, pady=20)
frame_2.place(x=640, y=400, height=250, width=450)


# widgets for frame 2
Label(frame_2, text="USER", font=("Comic Sans", 30, "bold"), fg="#FC46AA").place(x=140, y=20)
Label(frame_2, text="Username: ", font=("Comic Sans", 16, "italic"), fg="#FC46AA").place(x=20, y=100)
Label(frame_2, text="Password: ", font=("Comic Sans", 16, "italic"), fg="#FC46AA").place(x=20, y=140)

# write blocks
usr_name = Entry(frame_2, font=("ariel", 14), bg="lightgray", textvariable=u_input)
usr_name.place(x=130, y=105)
usr_psw = Entry(frame_2, font=("ariel", 14), bg="lightgray", textvariable=u_pass)
usr_psw.place(x=130, y=145)



# function for opening admin page
def login_admin():
    # Creating database connection
    conn = sqlite3.connect('song_book.db')
    # create cursor
    c = conn.cursor()

    c.execute("SELECT * FROM admin WHERE admin_name=? AND password=?", (a_input.get(), a_pass.get()))
    ad = c.fetchone()
    if ad:
        admin_name.delete(0, END)
        admin_psw.delete(0, END)
        admin()
    else:
        admin_name.delete(0, END)
        admin_psw.delete(0, END)
        messagebox.showinfo('info', 'Login Failed')

    # Commit changes
    conn.commit()
    # closing connection
    conn.close()

def login_usr():
    # Creating database connection
    conn = sqlite3.connect('song_book.db')
    # create cursor
    c = conn.cursor()

    c.execute("SELECT * FROM user WHERE user_name=? AND password=?", (u_input.get(), u_pass.get()))
    ad = c.fetchone()
    if ad:
        usr_name.delete(0, END)
        usr_psw.delete(0, END)

        user()
    else:
        usr_name.delete(0, END)
        usr_psw.delete(0, END)
        messagebox.showinfo('info', 'Login Failed')

    # Commit changes
    conn.commit()
    # closing connection
    conn.close()


# login button
admin_log_butn = Button(frame_1, text="LOGIN", fg="#FC46AA", font=("times new roman", 18), command=login_admin)
admin_log_butn.place(x=160, y=180)
user_log_btn = Button(frame_2, text="LOGIN", fg="#FC46AA", font=("times new roman", 18), command=login_usr)
user_log_btn.place(x=160, y=180)

root.mainloop()
