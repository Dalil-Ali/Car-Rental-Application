import tkinter as tk
import customtkinter
import sqlite3

def have_account():
    root.destroy()
    import login

def check_pass():
    password = password_input.get()
    if len(password) < 8:
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    return True

def enter_data():
    firstname = firstName_input.get()
    lastname = lastName_input.get()
    username = username_input.get()
    email = email_input.get()
    password = password_input.get()
    error = check_pass()

    

    if error == False:
        error = tk.Label(root, text='Password must be at least 8 characters long, contain', fg = '#E0F2F1', bg='#26A69A')
        error.place(relx=0.5, rely=0.7255, anchor='center')
        error = tk.Label(root, text='at least 1 digit, 1 uppercase letter, and 1 lowercase letter.', fg = '#E0F2F1', bg='#26A69A')
        error.place(relx=0.5, rely=0.755, anchor='center')
    else:
        conn = sqlite3.connect('users.db')
        table_create = '''CREATE TABLE IF NOT EXISTS user_data(
            firstname TEXT, lastname TEXT, username TEXT, email TEXT, password TEXT
        )
        '''

        data_insert = '''INSERT INTO user_data(
        firstname, lastname, username, email, password) VALUES (?,?,?,?,?)
        '''
        data_insert_tuple = (firstname, lastname, username, email, password)
        conn.execute(table_create)
        cursor = conn.cursor()
        cursor.execute(data_insert, data_insert_tuple)
        conn.commit()
        conn.close()
        error = tk.Label(root, text='Password must be at least 8 characters long, contain', fg = '#26A69A', bg='#26A69A')
        error.place(relx=0.5, rely=0.7255, anchor='center')
        error = tk.Label(root, text='at least 1 digit, 1 uppercase letter, and 1 lowercase letter.', fg = '#26A69A', bg='#26A69A')
        error.place(relx=0.5, rely=0.755, anchor='center')

        connected_message = tk.Label(root ,text='Account created successfuly. Sending you to Login ...', bg='#26A69A', fg='#E0F2F1')
        connected_message.place(relx=0.5, rely=0.74, anchor='center')
        
        root.update_idletasks()
        root.after(3000, have_account)
        
    
    


root = tk.Tk()
root.resizable(False,False)
root.geometry("700x600")
root.title("Location de Voiture - Sign Up")
favicon = tk.PhotoImage(file = "resources/favicon.png")
root.iconphoto(False, favicon)


bgimg= tk.PhotoImage(file = "resources/bground.png")
limg= tk.Label(root, i=bgimg)
limg.pack()

login = tk.Label(root ,text='Sign Up', bg='#26A69A', font=('Ariel 23 bold'), fg="#263239")
login.place(relx=0.5, rely=0.14, anchor="center")






firstName_label = tk.Label(root ,text='First Name ', bg='#26A69A', font=('Ariel 10 '), fg="#263239")
firstName_label.place(relx=0.3, rely=0.22)
firstName_input = tk.Entry(root, width=45)
firstName_input.place(relx=0.5, rely=0.275, anchor='center')

lastName_label = tk.Label(root ,text='Last Name: ', bg='#26A69A', font=('Ariel 10 '), fg="#263239")
lastName_label.place(relx=0.3, rely=0.32)
lastName_input = tk.Entry(root, width=45)
lastName_input.place(relx=0.5, rely=0.375, anchor='center')

username_label = tk.Label(root ,text='Username: ', bg='#26A69A', font=('Ariel 10 '), fg="#263239")
username_label.place(relx=0.3, rely=0.42)
username_input = tk.Entry(root, width=45)
username_input.place(relx=0.5, rely=0.475, anchor='center')

email_label = tk.Label(root ,text='Email: ', bg='#26A69A', font=('Ariel 10 '), fg="#263239")
email_label.place(relx=0.3, rely=0.52)
email_input = tk.Entry(root, width=45)
email_input.place(relx=0.5, rely=0.575, anchor='center')

password_label = tk.Label(root ,text='Password: ', bg='#26A69A', font=('Ariel 10 '), fg="#263239")
password_label.place(relx=0.3, rely=0.62)
password_input = tk.Entry(root, show="*", width=45)
password_input.place(relx=0.5, rely=0.675, anchor='center')



buttonLogin = customtkinter.CTkButton(master=root, text="Sign Up", command=enter_data, bg='#26A69A', fg_color="#E0F2F1", text_color='#263239' )
buttonLogin.place(relx=0.5, rely=0.82, anchor=tk.CENTER)

account_label = tk.Label(root ,text='Already have an account ? ', bg='#26A69A', font=('Ariel 8 '), fg="#263239")
account_label.place(relx=0.47, rely=0.874, anchor=tk.CENTER)

button = tk.Button(root, text="Login", command=have_account, bg='#26A69A', font=('Ariel 8 underline'), bd=0, fg='#E0F2F1', cursor='hand2', activebackground='#26A69A', activeforeground='red'  )
button.place(relx=0.59, rely=0.871, anchor=tk.CENTER)





root.mainloop()