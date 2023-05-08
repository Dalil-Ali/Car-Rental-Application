from tkinter import *
import tkinter as tk
import customtkinter
import sqlite3


def connected():
    root.destroy()
    import signup

def have_account():
    root.destroy()
    import main

conn = sqlite3.connect('users.db')
cursor = conn.cursor()
def enter_data():
    get_data = """
        SELECT username, password FROM user_data
    """
    cursor.execute(get_data)
    window_creds = cursor.fetchall()
    
    for window_cred in window_creds:
        if username_input.get() == window_cred[0] and password_input.get() == window_cred[1]:
            have_account()
            break
        else:
            error = tk.Label(root, text='Incorrect Username or Password!', fg = '#E0F2F1', bg='#26A69A', font=('Ariel 10 '))
            error.place(relx=0.5, rely=0.6, anchor=CENTER)



root = tk.Tk()
root.resizable(False,False)
root.geometry("700x600")
root.title("Location de Voiture - Login")
favicon = PhotoImage(file = "resources/favicon.png")
root.iconphoto(False, favicon)
bgimg= tk.PhotoImage(file = "resources/bground.png")
limg= Label(root, i=bgimg)
limg.pack()

login = tk.Label(root ,text='Login', bg='#26A69A', font=('Ariel 23 bold'), fg="#263239")
login.place(relx=0.5, rely=0.2, anchor=CENTER)

username_label = tk.Label(root ,text='Username: ', bg='#26A69A', font=('Ariel 10 '), fg="#263239")
username_label.place(relx=0.3, rely=0.40)

username_input = tk.Entry(root, width=45)
username_input.place(relx=0.5, rely=0.45, anchor=CENTER)

password_label = tk.Label(root ,text='Password: ', bg='#26A69A', font=('Ariel 10 '), fg="#263239")
password_label.place(relx=0.3, rely=0.5)

password_input = tk.Entry(root, show="*", width=45)
password_input.place(relx=0.5, rely=0.55, anchor=CENTER)

buttonLogin = customtkinter.CTkButton(master=root, text="Login", command=enter_data, bg='#26A69A', fg_color="#E0F2F1", text_color='#263239' )
buttonLogin.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

account_label = tk.Label(root ,text='Dont have an account ? ', bg='#26A69A', font=('Ariel 8 '), fg="#263239")
account_label.place(relx=0.45, rely=0.85, anchor=tk.CENTER)

button = tk.Button(root, text="Create One", command=connected, bg='#26A69A', font=('Ariel 8 underline'), bd=0, fg='#E0F2F1', cursor='hand2', activebackground='#26A69A', activeforeground='red' )
button.place(relx=0.58, rely=0.85, anchor=tk.CENTER)

root.mainloop()