# Car-Rental-Application
This is a **Python-Tkinter** project for a **Rental Car Application** that includes a *login and signup* feature for users. The application allows users to *add, edit, and delete car listings*, with information such as car model, price, and availability. The application uses **SQLite3** to manage and store car listings. The GUI is created using Tkinter and custom widgets, providing a user-friendly experience.
## Login File
This code imports the necessary modules: tkinter, customtkinter, and sqlite3. The tkinter module is a standard Python GUI (Graphical User Interface) toolkit, customtkinter is a custom extension of the tkinter module, and sqlite3 is a module used for working with SQLite databases.
```
from tkinter import *
import tkinter as tk
import customtkinter
import sqlite3
```

The **connected()** function closes the current window (root) and imports and opens the **signup** module.This function is called when the user clicks the **Sign Up** button.
```
def connected():
  root.destroy()
  import signup
```

The **have_account()** function also closes the current window (root) but imports and opens the **main** module instead. This function is called when the user clicks the "Create One" button.
```
def have_account():
    root.destroy()
    import main
```
These two lines of code establish a connection to the SQLite database named **"users.db"** using the connect method of the sqlite3 module and create a cursor object for executing SQL statements on the database using the cursor method of the connection object. The **cursor** object is used to **execute** the SQL statements and fetch the results.
```
conn = sqlite3.connect('users.db')
cursor = conn.cursor()
```
The above code defines a function named "enter_data" which retrieves the data from the "user_data" table of the "users.db" database. It then checks if the username and password entered in the "username_input" and "password_input" fields match with any of the credentials retrieved from the database. If a match is found, the function calls the "have_account()" function, which redirects the user to the main page of the application. If no match is found, it displays an error message on the screen indicating that the username or password entered is incorrect.
```
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
```
This code initializes a new instance of the Tkinter Tk class and sets the window size to 700x600 pixels with the title "Location de Voiture - Login". The resizable method is used to prevent the user from being able to resize the window. The code then loads a favicon image from the "resources" folder and sets it as the icon for the window using the iconphoto method. Finally, it loads a background image from the "resources" folder and creates a new label widget limg to display the image in the window using the pack method.
```
root = tk.Tk()
root.resizable(False,False)
root.geometry("700x600")
root.title("Location de Voiture - Login")
favicon = PhotoImage(file = "resources/favicon.png")
root.iconphoto(False, favicon)
bgimg= tk.PhotoImage(file = "resources/bground.png")
limg= Label(root, i=bgimg)
limg.pack()
```
The code above defines the layout and widgets of the login page for a rental car application. It includes a title label ("Login"), two entry fields for the user to input their username and password, a login button that triggers the enter_data() function when clicked, a label with a prompt for users who don't have an account, and a button to redirect to the signup page when clicked. The widgets are placed using the place() method with relative coordinates.
```
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
```
This line of code is used to run the main event loop of the tkinter GUI. It continuously listens to user inputs and updates the graphical interface of the application accordingly until the user closes the window.
```
root.mainloop()
```



## SignUp File
This is a Python code that imports the required libraries for a desktop GUI application. The tkinter library is used for building the GUI, customtkinter is a custom module for tkinter widgets, and sqlite3 is used to handle the database for the application.
```
import tkinter as tk
import customtkinter
import sqlite3
```
The **have_account()** function closes the current window (root) but imports and opens the **main** module instead. This function is called when the user clicks the "Create One" button.
```
def have_account():
    root.destroy()
    import main
```
This is a function named **check_pass()** that takes no arguments. It first retrieves the password entered in the password input field. It then checks if the password has a length less than 8 characters, contains at least one digit, at least one uppercase letter, and at least one lowercase letter. If any of these conditions are not met, it returns False, indicating that the password is not strong enough. If all conditions are met, it returns True, indicating that the password is strong enough.
```
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
```
The function enter_data() is called when the user clicks the "Sign Up" button. It retrieves the user input from the GUI entry fields for first name, last name, username, email, and password. Then, it checks the password to ensure it meets certain requirements: it must be at least 8 characters long, contain at least one digit, one uppercase letter, and one lowercase letter. If the password doesn't meet these requirements, an error message is displayed on the GUI.
```
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
```
This code creates a new Tkinter window with a fixed size of 700x600 pixels and a title "Location de Voiture - Sign Up". It sets a favicon image for the window and a background image using PhotoImage objects. The background image is then displayed using a label. Finally, a label is created with the text "Sign Up" in a green background with a bold font and positioned at the center top of the window.
```
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
```
The code creates a graphical user interface for a sign-up form using the Tkinter module. It includes several input fields for the user's first name, last name, username, email, and password. The form also has a "Sign Up" button that calls a function named "enter_data" when clicked, as well as a link to a login page for users who already have an account. The layout is designed using relative positioning using the "relx" and "rely" attributes, and a background image is used to enhance the appearance of the form.
```
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
```
This line of code is used to run the main event loop of the tkinter GUI. It continuously listens to user inputs and updates the graphical interface of the application accordingly until the user closes the window.
```
root.mainloop()
```


## Main File
This is a Python code that imports necessary modules and libraries for creating a graphical user interface (GUI) using the Tkinter library. It also imports a customtkinter module and the SQLite3 library for database management. The GUI will have various widgets such as labels, buttons, and input fields, and will be used for a sign-up form for a car rental application.
```
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import customtkinter as ctk
import sqlite3
```

This is a Python class called "Car" that represents a car object. It has several attributes such as car ID, brand, model, image, fuel type, number of seats, transmission type, availability status, and rental price. The class also has a method called "isDisponible" that takes an ID as input and checks if the car with that ID is available for rent. It does this by connecting to a SQLite database and retrieving the availability status of the car with the given ID. If the car is available (disponibility == 'Disponible'), the method returns True; otherwise, it returns False.
```
class Car:
    def __init__(self, car_id, marque, modele, image, image_bg ,carburant, places, transmission, disponibility, price):
        self.id = car_id
        self.marque = marque
        self.modele = modele
        self.image = image
        self.image_bg = image_bg
        self.type_carburant = carburant
        self.nombre_places = places
        self.transmission = transmission
        self.disponibilite = disponibility
        self.prix_location = price
    def isDisponible(self, id):
        # Connect to the database
        conn = sqlite3.connect('location_voitures.db')
        c = conn.cursor()
        
        # Retrieve the disponibility of the car with the given ID from the database
        c.execute('SELECT disponibilite FROM voitures WHERE id=?', (id,))
        disponibility = c.fetchone()[0]
        
        # Close the database connection
        conn.close()
        
        # Check if the car is available (disponibility == 'Disponible')
        if disponibility == 'Disponible':
            return True
        else:
            return False
```
The code creates a Tkinter GUI window named "Location de Voiture - Dashboard" with a fixed size of 1280x700 and disables the ability to resize the window. The background color of the window is set to "#E0F2F1". A frame named "menu" is created and added to the window, filling the entire space and expanding as needed.
```
root = tk.Tk()
root.title("Location de Voiture - Dashboard")
root.resizable(False,False)
root.geometry("1280x700")
root.configure(bg="#E0F2F1")
menu = tk.Frame(root, bg="#E0F2F1")
menu.pack(fill="both", expand=True)
```
This code connects to a SQLite database named "location_voitures.db" and retrieves data from a table named "voitures". It then creates instances of a class named "Car" for each row in the database, and adds them to a list named "car_objects". The code also uses dynamic variable creation to create a variable for each car object using the lowercased combination of the car's make and model as the variable name.
```
conn = sqlite3.connect('location_voitures.db')
c = conn.cursor()
c.execute('SELECT * FROM voitures')
cars_data = c.fetchall()
conn.close()
car_objects = []
for car in cars_data:
    id, marque, modele, image, image_bg, carburant, places, transmission, disponibility, price = car
    obj_name = marque.lower() + "_" + modele.lower()
    obj = Car(id, marque, modele, image, image_bg, carburant, places, transmission, disponibility, price)
    car_objects.append(obj)
    locals()[obj_name] = obj
```
This code connects to a SQLite database named 'location_voitures.db' and retrieves the total number of rows in the 'voitures' table using a SELECT COUNT(*) query. Then, it retrieves all the 'image' column values from the 'voitures' table using a SELECT query and stores them in the 'images' variable. Next, it iterates over the images and creates a variable name for each image using the prefix "image_var" followed by the index of the image. It then creates a Tkinter PhotoImage object for each image and assigns it to the dynamically created variable using the globals() function. The purpose of this code is to load all the car images from the database and store them as PhotoImage objects that can be used later in the GUI application.
```
conn = sqlite3.connect('location_voitures.db')
cursor = conn.cursor()
cursor.execute('SELECT COUNT(*) FROM voitures')
num_rows = cursor.fetchone()[0]
cursor.execute('SELECT image FROM voitures')
images = cursor.fetchall()
for i in range(len(images)):
    # Create a variable name using a prefix and the index of the image
    var_name = f"image_var{i}"
    # Assign the PhotoImage object to the variable
    globals()[var_name] = tk.PhotoImage(file=images[i][0])
```

This is a function named clear_root_frame(). It loops through all the children widgets of the root frame (except the menu widget) and destroys them, effectively clearing the frame.
```
def clear_root_frame():
    for widget in root.winfo_children():
        if widget != menu:
            widget.destroy()
```
These are two functions that create a "go back" button on the GUI. The first function, "goback_cars_edit", creates a button with the image "goBack" and places it at a specific location on the root frame, and it calls the function "gobackEdit" when the button is clicked. The second function, "goback_cars", is similar but it calls the function "goback" instead. Both functions are used to navigate back to the previous page or menu in the GUI.
```
def goback_cars_edit():
    button = tk.Button(master=root,command=gobackEdit , image=goBack, bg='#E0F2F1', borderwidth=0, cursor='hand2',activebackground='#E0F2F1')
    button.place(relx=0.27, rely=0.1)
def goback_cars():
    button = tk.Button(master=root,command=goback , image=goBack, bg='#E0F2F1', borderwidth=0, cursor='hand2',activebackground='#E0F2F1')
    button.place(relx=0.27, rely=0.1)
```
The showCarInfo() function displays information about a car with a given index on the GUI. It first clears the root frame and adds a button to go back to the previous screen. It then connects to a SQLite database and executes a SELECT statement with a WHERE clause to retrieve the information for the specified car. The retrieved values are then stored in variables. The function creates a label to display the image of the car, and labels to display the other information about the car such as brand, model, fuel type, number of seats, transmission type, availability, and price. The availability label is colored green if the car is available, and red if it is not. The function uses global variables to store the image objects for each car to prevent them from being garbage collected. Finally, the function closes the database connection.
```
def showCarInfo(index):
    clear_root_frame()
    goback_cars()
    conn = sqlite3.connect('location_voitures.db')
    cursor = conn.cursor()
    # Define the image path to match
    # Execute the SELECT statement with the WHERE clause
    cursor.execute("SELECT marque, modele, type_carburant, nombre_places, transmission, disponibilite, prix_location FROM voitures WHERE id = ?", (index+1,))
    row = cursor.fetchone()
    # Store the retrieved values in variables
    marque = row[0]
    modele = row[1]
    type_carburant = row[2]
    nombre_places = row[3]
    transmission = row[4]
    disponibilite = row[5]
    prix_location = row[6]
    image_var_name = f"image_var{index}"
    globals()[image_var_name] = tk.PhotoImage(file=dbBigImages[index])
    # Close the database connection
    conn.close()
    if disponibilite=="Disponible":
        color = 'green'
    if disponibilite=="Indisponible":
        color='red'
    toyotaCorolla_label = tk.Label(root, image=globals()[image_var_name], bg='#E0F2F1')
    toyotaCorolla_label.place(relx=0.25, rely=0.27)

    marque_label = tk.Label(root, text="Marque: ", bg='#E0F2F1', font=('Ariel 18 bold'), fg='#263339')
    marque_label.place(relx=0.6, rely=0.27)
    marque = tk.Label(root, text=marque, bg='#E0F2F1', font=('Ariel 15'), fg='#728F9E')
    marque.place(relx=0.7, rely=0.274)

    modele_label = tk.Label(root, text="Modele: ", bg='#E0F2F1', font=('Ariel 18 bold'), fg='#263339')
    modele_label.place(relx=0.6, rely=0.35)
    modele = tk.Label(root, text=modele, bg='#E0F2F1', font=('Ariel 15'), fg='#728F9E')
    modele.place(relx=0.7, rely=0.354)

    carburant_label = tk.Label(root, text="Type de Carburant: ", bg='#E0F2F1', font=('Ariel 18 bold'), fg='#263339')
    carburant_label.place(relx=0.6, rely=0.43)
    carburant = tk.Label(root, text=type_carburant, bg='#E0F2F1', font=('Ariel 15'), fg='#728F9E')
    carburant.place(relx=0.797, rely=0.434)

    places_label = tk.Label(root, text="Nombre de Places: ", bg='#E0F2F1', font=('Ariel 18 bold'), fg='#263339')
    places_label.place(relx=0.6, rely=0.51)
    places = tk.Label(root, text=nombre_places, bg='#E0F2F1', font=('Ariel 15'), fg='#728F9E')
    places.place(relx=0.795, rely=0.514)

    transmission_label = tk.Label(root, text="Transmission: ", bg='#E0F2F1', font=('Ariel 18 bold'), fg='#263339')
    transmission_label.place(relx=0.6, rely=0.59)
    transmission = tk.Label(root, text=transmission, bg='#E0F2F1', font=('Ariel 15'), fg='#728F9E')
    transmission.place(relx=0.752, rely=0.594)

    disponibility_label = tk.Label(root, text="Disponibilité: ", bg='#E0F2F1', font=('Ariel 18 bold'), fg='#263339')
    disponibility_label.place(relx=0.6, rely=0.67)
    disponibility = tk.Label(root, text=disponibilite, bg='#E0F2F1', font=('Ariel 15 bold'), fg=color)
    disponibility.place(relx=0.75, rely=0.674)

    price_label = tk.Label(root, text="Prix de location: ", bg='#E0F2F1', font=('Ariel 18 bold'), fg='#263339')
    price_label.place(relx=0.6, rely=0.75)
    price = tk.Label(root, text=f"{prix_location} DH", bg='#E0F2F1', font=('Ariel 15 '), fg='#728F9E')
    price.place(relx=0.77, rely=0.754)
```
The searchBar() function creates a search bar widget using the CTkEntry class from the ctk module. This search bar has a default text "Search by Name, Modele, Place Numbers, Price, Transmission" and is placed on the tkinter window.
```
def searchBar():
    searchBar = ctk.CTkEntry(master= root, text_color="#E0F2F1",font=('Ariel 10 bold'), corner_radius=15, fg_color='#E0F2F1', width=400, height=30)
    searchBar.insert(0, "Search by Name, Modele, Place Numbers, Price, Transmission")
    searchBar.place(relx=0.43, rely=0.1)
```
These are Python functions that retrieve images from a SQLite database.
- The getBigImages function retrieves the image_bg column from a table named table_name in a SQLite database named database_name. The function first counts the number of rows in the table and then retrieves the images in batches of three columns and several rows. The retrieved images are then returned as a list.
- The getSmallImages function retrieves the image column from the same table and database as getBigImages. It also retrieves the images in batches of three columns and several rows and returns them as a list.

After defining the two functions, the code calls both functions with the appropriate database and table names to retrieve two lists of images: dbBigImages and dbSmallImages.
```
def getBigImages(database_name, table_name):
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()
    cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
    num_rows = cursor.fetchone()[0]
    cursor.execute(f"SELECT image_bg FROM {table_name}")
    images = cursor.fetchall()
    num_buttons = len(images)
    num_cols = 3
    num_rows = num_buttons // num_cols
    dbimages = []
    for i in range(num_rows):
        for j in range(num_cols):
            # Calculate the index of the current button
            index = i * num_cols + j
            dbimages.append(images[index][0])         
    return dbimages
def getSmallImages(database_name, table_name):
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()
    cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
    num_rows = cursor.fetchone()[0]
    cursor.execute(f"SELECT image FROM {table_name}")
    images = cursor.fetchall()
    num_buttons = len(images)
    num_cols = 3
    num_rows = num_buttons // num_cols
    dbimages = []
    for i in range(num_rows):
        for j in range(num_cols):
            # Calculate the index of the current button
            index = i * num_cols + j
            dbimages.append(images[index][0])         
    return dbimages
dbBigImages = getBigImages('location_voitures.db', 'voitures')
dbSmallImages = getSmallImages('location_voitures.db', 'voitures')
```
This is a Python function that creates a grid of buttons from rows in a database table.

1. First, the function connects to a specified SQLite database and retrieves the number of rows in a specified table, as well as the image and availability for each row.

2. The function then calculates the number of rows and columns needed based on the number of buttons, and creates a list of buttons based on the number of rows and columns.

3. For each button, the function calculates its position on the grid based on its row and column, sets its image based on the corresponding row in the database, and sets its command to a function called showCarInfo with an argument of the button's index.

4. Finally, the function creates a colored circle next to each button to represent the availability of the corresponding row in the database. The color is green if the availability is "Disponible", red if it is "Indisponible", and black otherwise.

Overall, this function is used to display a grid of buttons representing cars available for rent, with information about each car displayed when its corresponding button is clicked.
```
def create_buttons_from_database_rows(database_name, table_name):
    # Connect to the database
    conn = sqlite3.connect(database_name)

    # Get the number of rows in the database and the images for each row
    cursor = conn.cursor()
    cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
    num_rows = cursor.fetchone()[0]
    cursor.execute(f"SELECT image FROM {table_name}")
    images = cursor.fetchall()
    cursor.execute(f"SELECT disponibilite FROM {table_name}")
    disponibility = cursor.fetchall()

    # Calculate the number of rows and columns needed based on the number of buttons
    num_buttons = len(images)
    num_cols = 3
    num_rows = num_buttons // num_cols
    # Create a list of buttons based on the number of rows and columns
    buttons = []
    for i in range(num_rows):
        for j in range(num_cols):
            # Calculate the index of the current button
            index = i * num_cols + j
            if index >= num_buttons:
                break

            # Calculate the x position of the button based on the button's column
            if j == 0:
                relx = 0.3
            elif j == 1:
                relx = 0.55
            else:
                relx = 0.8

            # Calculate the y position of the button based on the button's row
            rely = 0.2 + i * 0.35
            color = 'black'
            if disponibility[index][0]=="Disponible":
                color = 'green'
            if disponibility[index][0]=="Indisponible":
                color='red'
            image_var_name = f"image_var{index}"
            globals()[image_var_name] = tk.PhotoImage(file=dbSmallImages[index])
 

            # Create a new button with the specified image and command
            button = tk.Button(master=root, command=lambda index=index: showCarInfo(index), image=globals()[image_var_name], height=180,
                               bg='#E0F2F1', borderwidth=0, cursor='hand2',
                               activebackground='#E0F2F1')
            button.place(relx=relx, rely=rely)
            canvas_width = 15
            canvas_height = 15

            # create the canvas widget
            canvas = tk.Canvas(root, width=canvas_width, height=canvas_height,bg='#E0F2F1')

            # draw the circle on the canvas
            x = y = canvas_width // 2
            r = 5
            canvas.create_oval(x-r, y-r, x+r, y+r,outline=color, fill=color)
            canvas.place(relx=relx+0.1, rely=rely+0.231)
            buttons.append(button)
```
This is a Python function that creates a grid of buttons representing cars stored in a SQLite database. The function takes a single argument condition which is used to determine whether or not to include a search bar above the grid of buttons. If condition is equal to 1, then the function calls the searchBar() function to create a search bar widget. Otherwise, the function skips creating the search bar.

The create_buttons_from_database_rows() function is then called to create the grid of buttons representing the cars stored in the database. The function takes the database name and table name as arguments, retrieves the images and availability status of each car from the database, and creates a button widget for each car. The buttons are placed on a Tkinter canvas using the place() method and assigned a callback function to display more information about the car when clicked.

Overall, this function creates a graphical user interface for browsing and searching through a database of cars.
```
def show_grid(condition):
    clear_root_frame()
    def searchBar():
        searchBar = ctk.CTkEntry(master= root, text_color="#728F9E",font=('Ariel 10 bold'), corner_radius=15, fg_color='#D0EBEA', width=500, height=30)
        searchBar.insert(0, "Search by Name, Modele, Place Numbers, Price, Transmission")
        searchBar.place(relx=0.43, rely=0.1)
    #Search Bar
    if condition == 1:
        searchBar()
    #Cars Grid
    create_buttons_from_database_rows('location_voitures.db', 'voitures')

```
The goback() function is used to go back to the grid view with the search bar. The logout() function is used to log out the user and destroy the root window, and it also imports the login module.
```
def goback():
    show_grid(1)    
#Lougout Button 
def logout():
    root.destroy()
    import login
```
This code is a GUI for adding a car to a database. The user interface has various labels, input fields, and buttons. The user inputs the details of the car such as marque, modele, type of carburant, number of places, transmission, availability, and price of the car. When the user clicks on the save button, the details of the car are inserted into the SQLite database 'location_voitures.db'. The save_car_data function retrieves the data from the input fields and inserts it into the database. The add_car_to_db function creates a connection to the database, inserts the data into the voitures table, and closes the connection. If the insertion is successful, a message box pops up with the message "Car added successfully!".
```
def add_car_to_db():
    conn = sqlite3.connect('location_voitures.db')
    c = conn.cursor()
    c.execute('INSERT INTO voitures (marque, modele, type_carburant, nombre_places, transmission, disponibilite, prix_location) VALUES (?, ?, ?, ?, ?, ?, ?)', 
              (marque, modele, carburant, places, transmission, disponibility, price))
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Car added successfully!")
def addCar():
    clear_root_frame()
    goback_cars()
    toyotaCorolla_label = tk.Label(root, image=uploadImageb, bg='#E0F2F1')
    toyotaCorolla_label.place(relx=0.25, rely=0.27)

    marque_label = tk.Label(root, text="Marque: ", bg='#E0F2F1', font=('Ariel 18 bold'), fg='#263339')
    marque_label.place(relx=0.6, rely=0.27)
    marque_input = ctk.CTkEntry(master= root,  text_color="#728F9E",font=('Ariel 10 bold'), corner_radius=8, fg_color='white', width=150, height=30)
    marque_input.place(relx=0.7, rely=0.274)
    

    modele_label = tk.Label(root, text="Modele: ", bg='#E0F2F1', font=('Ariel 18 bold'), fg='#263339')
    modele_label.place(relx=0.6, rely=0.35)
    modele_input = ctk.CTkEntry(master= root, text_color="#728F9E",font=('Ariel 10 bold'), corner_radius=8, fg_color='white', width=150, height=30)
    modele_input.place(relx=0.7, rely=0.354)

    carburant_label = tk.Label(root, text="Type de Carburant: ", bg='#E0F2F1', font=('Ariel 18 bold'), fg='#263339')
    carburant_label.place(relx=0.6, rely=0.43)
    carburant_input = ttk.Combobox(root, values=["Essence", "Gazoile", "Hybride", "Électrique"], height=100)
    carburant_input.current(0)
    carburant_input.place(relx=0.797, rely=0.438)

    places_label = tk.Label(root, text="Nombre de Places: ", bg='#E0F2F1', font=('Ariel 18 bold'), fg='#263339')
    places_label.place(relx=0.6, rely=0.51)
    places_input = tk.Spinbox(root, from_=2, to=10,width= 10, font=('Ariel 10'), fg='#728F9E', textvariable='5')
    places_input.place(relx=0.795, rely=0.518)

    transmission_label = tk.Label(root, text="Transmission: ", bg='#E0F2F1', font=('Ariel 18 bold'), fg='#263339')
    transmission_label.place(relx=0.6, rely=0.59)
    transmission_input = ttk.Combobox(root, values=["Automatique", "Manuelle"], height=100)
    transmission_input.current(0)
    transmission_input.place(relx=0.752, rely=0.594)

    disponibility_label = tk.Label(root, text="Disponibilité: ", bg='#E0F2F1', font=('Ariel 18 bold'), fg='#263339')
    disponibility_label.place(relx=0.6, rely=0.67)
    disponibility_input = ttk.Combobox(root, values=["Disponible", "Indisponible"], height=100)
    disponibility_input.current(0)
    disponibility_input.place(relx=0.75, rely=0.674)

    price_label = tk.Label(root, text="Prix de location: ", bg='#E0F2F1', font=('Ariel 18 bold'), fg='#263339')
    price_label.place(relx=0.6, rely=0.75)
    price_input = ctk.CTkEntry(master= root, text_color="#728F9E",font=('Ariel 10 bold'), corner_radius=8, fg_color='white', width=150, height=30)
    price_input.place(relx=0.77, rely=0.754)

    def save_car_data():
        global marque
        marque = marque_input.get()
        global modele
        modele = modele_input.get()
        global carburant
        carburant = carburant_input.get()
        global places
        places = places_input.get()
        global transmission
        transmission = transmission_input.get()
        global disponibility
        disponibility = disponibility_input.get()
        global price
        price = price_input.get()
        add_car_to_db()


    save_button = tk.Button(master=root,command= save_car_data,image=saveChanges, bg='#E0F2F1', borderwidth=0, cursor='hand2',activebackground='#E0F2F1')
    save_button.place(relx=0.62, rely=0.85)

    cancel_button = tk.Button(master=root, image=cancelChanges,command=goback, bg='#E0F2F1', borderwidth=0, cursor='hand2',activebackground='#E0F2F1')
    cancel_button.place(relx=0.8, rely=0.85)
```
This code defines several functions related to editing car information in a database.

- The create_buttons_from_database_rows_edit function connects to a SQLite database and retrieves images of cars stored in a table. It then calculates the number of rows and columns needed to display the images and creates a list of buttons, each with a specific image and command to edit the car's information.

- The show_grid_edit function displays the list of buttons in a grid format on a GUI.

- The edit_carInfo_to_db function connects to the database and updates the car's information based on the input parameters and the car's index in the database table. It then shows a message box indicating the success of the update.

- The gobackEdit function is called when the user wants to go back to the previous screen for editing cars.
```
def gobackEdit():
    editCar()
def create_buttons_from_database_rows_edit(database_name, table_name):
    # Connect to the database
    conn = sqlite3.connect(database_name)

    # Get the number of rows in the database and the images for each row
    cursor = conn.cursor()
    cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
    num_rows = cursor.fetchone()[0]
    cursor.execute(f"SELECT image FROM {table_name}")
    images = cursor.fetchall()
    

    # Calculate the number of rows and columns needed based on the number of buttons
    num_buttons = len(images)
    num_cols = 3
    num_rows = num_buttons // num_cols
    # Create a list of buttons based on the number of rows and columns
    buttons = []
    for i in range(num_rows):
        for j in range(num_cols):
            # Calculate the index of the current button
            index = i * num_cols + j
            if index >= num_buttons:
                break

            # Calculate the x position of the button based on the button's column
            if j == 0:
                relx = 0.3
            elif j == 1:
                relx = 0.55
            else:
                relx = 0.8

            # Calculate the y position of the button based on the button's row
            rely = 0.2 + i * 0.35
                
            image_var_name = f"image_var{index}"
            globals()[image_var_name] = tk.PhotoImage(file=dbSmallImages[index])
 

            # Create a new button with the specified image and command
            button = tk.Button(master=root, command=lambda index=index: edit_car_info(index), image=globals()[image_var_name], height=180,
                               bg='#E0F2F1', borderwidth=0, cursor='hand2',
                               activebackground='#E0F2F1')
            button.place(relx=relx, rely=rely)
            buttons.append(button)     
def show_grid_edit(condition):
    chooseCar(0)
    clear_root_frame()
    create_buttons_from_database_rows_edit('location_voitures.db', 'voitures')
def edit_carInfo_to_db(index):
    conn = sqlite3.connect('location_voitures.db')
    c = conn.cursor()
    c.execute('UPDATE voitures SET marque=?, modele=?, type_carburant=?, nombre_places=?, transmission=?, disponibilite=?, prix_location=? WHERE id=?', 
              (marque, modele, carburant, places, transmission, disponibility, price, index+1))
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Car information updated successfully!")
```
This function edit_car_info(index) edits a car's information stored in an SQLite database. The function clears the frame where the car information is displayed, connects to the database, and fetches the car's data by executing a SELECT statement with the WHERE clause that matches the car's id. It stores the fetched data in variables and displays them on the tkinter GUI along with entry widgets, spinboxes, and comboboxes to allow the user to update the information. Finally, the function inserts the updated data into the database.
```
def edit_car_info(index):
    clear_root_frame()
    goback_cars_edit()
    conn = sqlite3.connect('location_voitures.db')
    cursor = conn.cursor()

    # Define the image path to match


    # Execute the SELECT statement with the WHERE clause
    cursor.execute("SELECT marque, modele, type_carburant, nombre_places, transmission, disponibilite, prix_location FROM voitures WHERE id = ?", (index+1,))
    row = cursor.fetchone()

    # Store the retrieved values in variables
    marque = row[0]
    modele = row[1]
    type_carburant = row[2]
    nombre_places = row[3]
    transmission = row[4]
    disponibilite = row[5]
    prix_location = row[6]
    image_var_name = f"image_var{index}"
    globals()[image_var_name] = tk.PhotoImage(file=dbBigImages[index])

    toyotaCorolla_label = tk.Label(root, image=globals()[image_var_name], bg='#E0F2F1')
    toyotaCorolla_label.place(relx=0.25, rely=0.27)

    marque_label = tk.Label(root, text="Marque: ", bg='#E0F2F1', font=('Ariel 18 bold'), fg='#263339')
    marque_label.place(relx=0.6, rely=0.27)
    marque_input = ctk.CTkEntry(master= root,  text_color="#728F9E",font=('Ariel 10 bold'), corner_radius=8, fg_color='white', width=150, height=30)
    marque_input.insert("0", marque)
    marque_input.place(relx=0.7, rely=0.274)
    

    modele_label = tk.Label(root, text="Modele: ", bg='#E0F2F1', font=('Ariel 18 bold'), fg='#263339')
    modele_label.place(relx=0.6, rely=0.35)
    modele_input = ctk.CTkEntry(master= root, text_color="#728F9E",font=('Ariel 10 bold'), corner_radius=8, fg_color='white', width=150, height=30)
    modele_input.insert("0", modele)
    modele_input.place(relx=0.7, rely=0.354)

    carburant_label = tk.Label(root, text="Type de Carburant: ", bg='#E0F2F1', font=('Ariel 18 bold'), fg='#263339')
    carburant_label.place(relx=0.6, rely=0.43)
    carburant_input = ttk.Combobox(root, values=["Essence", "Gazoile", "Hybride", "Électrique"], height=100)
    if type_carburant == "Essence":
        choice = 0
    if type_carburant == "Gazoile":
        choice = 1
    if type_carburant == "Hybride":
        choice = 2
    if type_carburant == "Électrique":
        choice = 3
    carburant_input.current(choice)
    carburant_input.place(relx=0.797, rely=0.438)

    places_label = tk.Label(root, text="Nombre de Places: ", bg='#E0F2F1', font=('Ariel 18 bold'), fg='#263339')
    places_label.place(relx=0.6, rely=0.51)
    nbr_places = tk.StringVar()
    places_input = tk.Spinbox(root, from_=2, to=10,width= 10, font=('Ariel 10'), fg='#728F9E', textvariable=nbr_places)
    places_input.place(relx=0.795, rely=0.518)
    nbr_places.set(nombre_places)

    transmission_label = tk.Label(root, text="Transmission: ", bg='#E0F2F1', font=('Ariel 18 bold'), fg='#263339')
    transmission_label.place(relx=0.6, rely=0.59)
    transmission_input = ttk.Combobox(root, values=["Automatique", "Manuelle"], height=100)
    if transmission == "Automatique":
        choice = 0
    if transmission == "Manuelle":
        choice = 1
    transmission_input.current(choice)
    transmission_input.place(relx=0.752, rely=0.594)

    disponibility_label = tk.Label(root, text="Disponibilité: ", bg='#E0F2F1', font=('Ariel 18 bold'), fg='#263339')
    disponibility_label.place(relx=0.6, rely=0.67)
    disponibility_input = ttk.Combobox(root, values=["Disponible", "Indisponible"], height=100)
    if disponibilite == "Disponible":
        choice = 0
    if disponibilite == "Indisponible":
        choice = 1
    disponibility_input.current(choice)
    disponibility_input.place(relx=0.75, rely=0.674)

    price_label = tk.Label(root, text="Prix de location: ", bg='#E0F2F1', font=('Ariel 18 bold'), fg='#263339')
    price_label.place(relx=0.6, rely=0.75)
    price_input = ctk.CTkEntry(master= root, text_color="#728F9E",font=('Ariel 10 bold'), corner_radius=8, fg_color='white', width=150, height=30)
    price_input.insert("0", prix_location)
    price_input.place(relx=0.77, rely=0.754)

    def save_car_data():
        global marque
        marque = marque_input.get()
        global modele
        modele = modele_input.get()
        global carburant
        carburant = carburant_input.get()
        global places
        places = places_input.get()
        global transmission
        transmission = transmission_input.get()
        global disponibility
        disponibility = disponibility_input.get()
        global price
        price = price_input.get()
        edit_carInfo_to_db(index)


    save_button = tk.Button(master=root,command= save_car_data,image=saveChanges, bg='#E0F2F1', borderwidth=0, cursor='hand2',activebackground='#E0F2F1')
    save_button.place(relx=0.62, rely=0.85)

    cancel_button = tk.Button(master=root, image=cancelChanges,command=gobackEdit, bg='#E0F2F1', borderwidth=0, cursor='hand2',activebackground='#E0F2F1')
    cancel_button.place(relx=0.8, rely=0.85)
```
The code defines two functions: chooseCar() and editCar().

- The chooseCar() function takes one argument choice, which is either 0 or 1. Depending on the value of choice, it displays a label with the text "Choose a Car to Edit" or "Choose a Car to Delete", respectively. The label is placed on the Tkinter root window at a specific position.

- The editCar() function first clears the root window frame and then calls the show_grid_edit() function with an argument of 1. It then calls the chooseCar() function with an argument of 0 to display the label "Choose a Car to Edit". Finally, it calls the goback_cars() function to display a "Go Back" button.
```
def editCar():
    clear_root_frame()
    show_grid_edit(1)
    chooseCar(0)
    goback_cars()
#############################################
def chooseCar(choice):
    edit = 'Choose a Car to Edit'
    delete = 'Choose a Car to Delete'
    if choice == 0:
        chooseCar = tk.Label(root, text= edit,font=('Ariel 15 bold'),  fg='#728F9E', bg='#E0F2F1')
        chooseCar.place(relx=0.525, rely=0.13)
    else:
        chooseCar = tk.Label(root, text= delete,font=('Ariel 15 bold'),  fg='#728F9E', bg='#E0F2F1')
        chooseCar.place(relx=0.520, rely=0.13)
```
The create_buttons_from_database_rows_delete function connects to the database and retrieves images and row count from a specified table. It then creates a list of buttons, with each button showing an image and having a command to delete the corresponding row in the database. The show_grid_delete function clears the root frame and calls the create_buttons_from_database_rows_delete function. The delete_car_info function deletes the selected car's information from the database, after confirming with a message box. Finally, the deleteCar function clears the root frame, calls show_grid_delete, and calls other functions to navigate back to the previous page.
```
def create_buttons_from_database_rows_delete(database_name, table_name):
    # Connect to the database
    conn = sqlite3.connect(database_name)

    # Get the number of rows in the database and the images for each row
    cursor = conn.cursor()
    cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
    num_rows = cursor.fetchone()[0]
    cursor.execute(f"SELECT image FROM {table_name}")
    images = cursor.fetchall()
    

    # Calculate the number of rows and columns needed based on the number of buttons
    num_buttons = len(images)
    num_cols = 3
    num_rows = num_buttons // num_cols
    # Create a list of buttons based on the number of rows and columns
    buttons = []
    for i in range(num_rows):
        for j in range(num_cols):
            # Calculate the index of the current button
            index = i * num_cols + j
            if index >= num_buttons:
                break

            # Calculate the x position of the button based on the button's column
            if j == 0:
                relx = 0.3
            elif j == 1:
                relx = 0.55
            else:
                relx = 0.8

            # Calculate the y position of the button based on the button's row
            rely = 0.2 + i * 0.35
                
            image_var_name = f"image_var{index}"
            globals()[image_var_name] = tk.PhotoImage(file=dbSmallImages[index])
 

            # Create a new button with the specified image and command
            button = tk.Button(master=root, command=lambda index=index: delete_car_info(index), image=globals()[image_var_name], height=180,
                               bg='#E0F2F1', borderwidth=0, cursor='hand2',
                               activebackground='#E0F2F1')
            button.place(relx=relx, rely=rely)
            buttons.append(button)
def show_grid_delete(condition):
    clear_root_frame()
    create_buttons_from_database_rows_delete('location_voitures.db', 'voitures')
def delete_car_info(index):
    conn = sqlite3.connect('location_voitures.db')
    c = conn.cursor()
    c.execute('DELETE FROM voitures WHERE id=?', (index+1,))
    conn.commit()
    conn.close()
    messagebox.askquestion("Confirmation", "Are you sure you want to delete this Car?")
    messagebox.showinfo("Success", "Car Deleted successfully!")
def deleteCar():
    clear_root_frame()
    show_grid_delete(0)
    goback_cars()
    chooseCar(1)
```
These lines of code define four variables as images using Tkinter's PhotoImage class. The first two images are for save and cancel buttons, the third image is for an "upload image" button, and the fourth image is for a "go back" button. The images are loaded from files located in the "resources" folder.
```
saveChanges = tk.PhotoImage(file="resources\saveChanges.png")
cancelChanges = tk.PhotoImage(file="resources\cancelChanges.png")
uploadImageb = tk.PhotoImage(file="resources/bigImages/uploadImageb.png")
goBack = tk.PhotoImage(file="resources/goback.png" )
```
The code first connects to a SQLite database called "users.db" and fetches the first and last name of a user to display a personalized greeting on the menu. The menu contains buttons to add a new car, edit a car, delete a car, and log out. Each button has an associated image and label. The images are stored in the "resources" folder, and the labels are created using the tk.Label and tk.Button functions. The place() function is used to position the labels and buttons on the menu. Overall, this code creates a simple menu interface, with buttons that allow the user to perform various actions on the cars in the system.
```
show_grid(1)
#Connect to the database and Get the First & Last Name and show it
conn = sqlite3.connect("users.db")
cur = conn.cursor()
cur.execute("SELECT firstname, lastname FROM user_data")
result = cur.fetchone()
first_name = result[0]
last_name = result[1]

greetings_label = tk.Label(menu, text=f"Hi, {first_name}{last_name}", bg='#E0F2F1', font=('Ariel 12 bold'), fg='#263339')
greetings_label.place(relx=0.075, rely=0.18)

user_admin = tk.Label(menu, text="Admin", bg='#E0F2F1', font=('Ariel 10 bold'), fg='#728F9E')
user_admin.place(relx=0.09, rely=0.215)

#Menu 
userIcon = tk.PhotoImage(file="resources/user.png", )
userIcon_label = tk.Label(menu, image=userIcon, bg='#E0F2F1')
userIcon_label.place(relx=0.09, rely=0.09)

addcar = tk.PhotoImage(file="resources/addCar.png")
button = tk.Button(master=menu,command=addCar, image=addcar, bg='#E0F2F1', borderwidth=0, cursor='hand2',activebackground='#E0F2F1')
button.place(relx=0.03, rely=0.36)

addcar_label_button = tk.Button(master=menu,command=addCar,  text='Add a new car', bg='#E0F2F1', borderwidth=0,  font=('Ariel 12 '), fg='#728F9E', cursor='hand2',  activebackground='#E0F2F1')
addcar_label_button.place(relx=0.07, rely=0.374)

editcar = tk.PhotoImage(file="resources\editCar.png")
button = tk.Button(master=menu,command=editCar, image=editcar, bg='#E0F2F1', borderwidth=0, cursor='hand2',activebackground='#E0F2F1')
button.place(relx=0.03, rely=0.47)

editcar_label_button = tk.Button(master=menu,command=editCar, text='Edit a car', bg='#E0F2F1', borderwidth=0,  font=('Ariel 12 '), fg='#728F9E', cursor='hand2',  activebackground='#E0F2F1')
editcar_label_button.place(relx=0.07, rely=0.484)

deletecar = tk.PhotoImage(file="resources\deleteCar.png")
button = tk.Button(master=menu,command=deleteCar , image=deletecar, bg='#E0F2F1', borderwidth=0, cursor='hand2',activebackground='#E0F2F1')
button.place(relx=0.03, rely=0.58)

deletecar_label_button = tk.Button(master=menu,command=deleteCar , text='Delete a car', bg='#E0F2F1', borderwidth=0, font=('Ariel 12 '), fg='#728F9E', cursor='hand2',  activebackground='#E0F2F1')
deletecar_label_button.place(relx=0.07, rely=0.594)

logout_image = tk.PhotoImage(file="resources\logout.png")
button = tk.Button(master=menu, image=logout_image, bg='#E0F2F1', borderwidth=0, cursor='hand2',activebackground='#E0F2F1')
button.place(relx=0.05, rely=0.806)

logout_label_button = tk.Button(master=menu,command= logout, text='Log Out', bg='#E0F2F1', borderwidth=0, font=('Ariel 13 bold'), fg='#728F9E', cursor='hand2',  activebackground='#E0F2F1')
logout_label_button.place(relx=0.08, rely=0.82)

line = tk.PhotoImage(file="resources\line.png", )
line_label = tk.Label(menu, image=line, bg='#E0F2F1')
line_label.place(relx=0.2, rely=-0.075)
```
This line of code is used to run the main event loop of the tkinter GUI. It continuously listens to user inputs and updates the graphical interface of the application accordingly until the user closes the window.
```
root.mainloop()
```
