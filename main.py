import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import customtkinter as ctk
import sqlite3


#Building the class Car for each car of the database
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

# Retrieve the data of all cars from the database
#Building Tkinter Window---------------------------------------------------------------------------

root = tk.Tk()
root.title("Location de Voiture - Dashboard")
root.resizable(False,False)
root.geometry("1280x700")
root.configure(bg="#E0F2F1")


menu = tk.Frame(root, bg="#E0F2F1")
menu.pack(fill="both", expand=True)

conn = sqlite3.connect('location_voitures.db')
c = conn.cursor()
c.execute('SELECT * FROM voitures')
cars_data = c.fetchall()
conn.close()

# Create an object variable for each car and store them in a list
car_objects = []
for car in cars_data:
    id, marque, modele, image, image_bg, carburant, places, transmission, disponibility, price = car
    obj_name = marque.lower() + "_" + modele.lower()
    obj = Car(id, marque, modele, image, image_bg, carburant, places, transmission, disponibility, price)
    car_objects.append(obj)
    locals()[obj_name] = obj
######################################

######################################
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



#Fonctions-----------------------------------------------------------------------------------------
# destroy all widgets in menu_frame
def clear_root_frame():
    
    for widget in root.winfo_children():
        if widget != menu:
            widget.destroy()
#Goback to Show Cars
def goback_cars_edit():
    button = tk.Button(master=root,command=gobackEdit , image=goBack, bg='#E0F2F1', borderwidth=0, cursor='hand2',activebackground='#E0F2F1')
    button.place(relx=0.27, rely=0.1)
def goback_cars():
    button = tk.Button(master=root,command=goback , image=goBack, bg='#E0F2F1', borderwidth=0, cursor='hand2',activebackground='#E0F2F1')
    button.place(relx=0.27, rely=0.1)
#Show the Informations stored of every CAR
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
#Search Bar 
def searchBar():
    searchBar = ctk.CTkEntry(master= root, text_color="#E0F2F1",font=('Ariel 10 bold'), corner_radius=15, fg_color='#E0F2F1', width=400, height=30)
    searchBar.insert(0, "Search by Name, Modele, Place Numbers, Price, Transmission")
    searchBar.place(relx=0.43, rely=0.1)
#Show Grid
#Getting images from DB
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

    
#Lougout Button 
def logout():
    root.destroy()
    import login
#Go back Button
def goback():
    show_grid(1)
def gobackEdit():
    editCar()
   
#Menu Buttons-------------------------------------------------------------------------------------
####################Add Car#######################
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
####################################################Edit Car#####################################################
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
##############################################
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
##############Images Variables###############
saveChanges = tk.PhotoImage(file="resources\saveChanges.png")
cancelChanges = tk.PhotoImage(file="resources\cancelChanges.png")
uploadImageb = tk.PhotoImage(file="resources/bigImages/uploadImageb.png")
goBack = tk.PhotoImage(file="resources/goback.png" )
#############################
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





root.mainloop()