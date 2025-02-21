<<<<<<< HEAD
import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import messagebox
import webbrowser
import json




# Helloo

#Bye

# Test Final
#Aryan Comment



# Initialize the main window
root = ctk.CTk()
root.geometry("900x600")
root.title("E-Library Management System")

# Function to switch frames dynamically
def show_frame(frame):
    for widget in main_frame.winfo_children():
        widget.destroy()
    frame()

# Load images dynamically and resize to fit the screen
def load_image(image_path, size):
    try:
        img = Image.open(image_path)
        img = img.resize(size, Image.LANCZOS)
        return ImageTk.PhotoImage(img)
    except Exception as e:
        print(f"Error loading image {image_path}: {e}")
        return None

# Load background image to fit the screen dynamically
def load_background_image():
    try:
        img = Image.open("D:\TestProject\LibraryManagementSystem\library123.jpg")
        img = img.resize((2000,1000), Image.LANCZOS)
        return ImageTk.PhotoImage(img)
    except Exception as e:
        print(f"Error loading background image: {e}")
        return None

# Home Page
def home_page():
    label = ctk.CTkLabel(main_frame, text="Welcome to the E-Library", font=("Arial", 24, "bold"))
    label.pack(pady=20)
    
    desc = ctk.CTkLabel(main_frame, text="Your digital library for books and resources.", font=("Arial", 14))
    desc.pack(pady=10)
    
    img = load_background_image()
    if img:
        img_label = tk.Label(main_frame, image=img)
        img_label.image = img  # Keep a reference
        img_label.pack(expand=True, fill="both")

# Adjust book images to fit dynamically in the available space
def books_available():
    label = ctk.CTkLabel(main_frame, text="Books Available", font=("Arial", 24, "bold"))
    label.pack(pady=10)
    
    table_frame = ttk.Frame(main_frame, borderwidth=5, relief="solid")
    table_frame.pack(pady=10, padx=20, expand=True, fill="both")
    
    columns = ("Title", "Author", "Genre")
    book_table = ttk.Treeview(table_frame, columns=columns, show="headings", height=15)
    
    
    for col in columns:
        book_table.heading(col, text=col, anchor="center")
        book_table.column(col, width=400, anchor="center")
    
    vsb = ttk.Scrollbar(table_frame, orient="vertical", command=book_table.yview)
    vsb.pack(side="right", fill="y")
    book_table.configure(yscrollcommand=vsb.set)
    book_table.pack(expand=True, fill="both")
    
    for book in load_books():
        book_table.insert("", "end", values=(book["title"], book["author"], book["genre"]))

# Load book list
def load_books():
    return [
        {"title": "The Hitchhiker's Guide to the Galaxy", "author": "Douglas Adams", "genre": "Science Fiction"},
        {"title": "Pride and Prejudice", "author": "Jane Austen", "genre": "Romance"},
        {"title": "To Kill a Mockingbird", "author": "Harper Lee", "genre": "Southern Gothic"},
        {"title": "1984", "author": "George Orwell", "genre": "Dystopian"},
        {"title": "The Lord of the Rings", "author": "J.R.R. Tolkien", "genre": "Fantasy"},
        {"title": "1984", "author": "George Orwell", "genre": "Dystopian"},
        {"title": "To Kill a Mockingbird", "author": "Harper Lee", "genre": "Southern Gothic"},
        {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "genre": "Tragedy"},
        {"title": "And Then There Were None", "author": "Agatha Christie", "genre": "Mystery"},
        {"title": "The Hitchhiker's Guide to the Galaxy", "author": "Douglas Adams", "genre": "Science Fiction"},
        {"title": "Jane Eyre", "author": "Charlotte Brontë", "genre": "Gothic Romance"},
        {"title": "Moby-Dick", "author": "Herman Melville", "genre": "Adventure"},
        {"title": "Little Women", "author": "Louisa May Alcott", "genre": "Coming-of-age"},
        {"title": "One Hundred Years of Solitude", "author": "Gabriel García Márquez", "genre": "Magical Realism"},
        {"title": "Beloved", "author": "Toni Morrison", "genre": "Historical Fiction"},
        {"title": "love", "author": "AryanShrestha", "genre": "Social"}
    ]

# Buy Books Page
def buy_books():
    label = ctk.CTkLabel(main_frame, text="Buy Books", font=("Arial", 24, "bold"))
    label.pack(pady=20)
    
    ctk.CTkLabel(main_frame, text="Select a book to buy:", font=("Arial", 14)).pack(pady=5)
    ctk.CTkButton(main_frame, text="Purchase Now", command=lambda: show_frame(home_page)).pack(pady=10)


# Books Available Page
def books_available():
    label = ctk.CTkLabel(main_frame, text="Books Available", font=("Arial", 24, "bold"))
    label.pack(pady=10)

    table_frame = ttk.Frame(main_frame, borderwidth=2, relief="solid")
    table_frame.pack(pady=10, padx=20, expand=True, fill="both")

    columns = ("Title", "Author", "Genre")
    book_table = ttk.Treeview(table_frame, columns=columns, show="headings", height=10)

    for col in columns:
        book_table.heading(col, text=col, anchor="center")
        book_table.column(col, width=200, anchor="center")

    vsb = ttk.Scrollbar(table_frame, orient="vertical", command=book_table.yview)
    vsb.pack(side="right", fill="y")
    book_table.configure(yscrollcommand=vsb.set)
    book_table.pack(expand=True, fill="both")

    for book in load_books():
        book_table.insert("", "end", values=(book["title"], book["author"], book["genre"]))

    # Open ManyBooks when a book is double-clicked
    def open_manybooks(event):
        webbrowser.open("https://manybooks.net/", new=1)

    book_table.bind("<Double-1>", open_manybooks)
# Buy Books Page with book selection and bill display
def buy_books():
    def generate_bill():
        selected_item = book_table.selection()
        if not selected_item:
            messagebox.showerror("Error", "Please select a book to generate the bill.")
            return
        
        book_info = book_table.item(selected_item, "values")

        # Create a new window for the bill
        bill_window = ctk.CTkToplevel(main_frame)
        bill_window.title("Book Purchase")
        bill_window.geometry("350x400")

        # Display book details
        ctk.CTkLabel(bill_window, text="Book Details", font=("Arial", 20, "bold")).pack(pady=10)
        details = f"Title: {book_info[0]}\nAuthor: {book_info[1]}\nGenre: {book_info[2]}\nPrice per book: $20"
        ctk.CTkLabel(bill_window, text=details, font=("Arial", 14)).pack(pady=5)

        # Quantity selection
        ctk.CTkLabel(bill_window, text="Select Quantity:", font=("Arial", 14)).pack(pady=5)
        quantity_var = tk.IntVar(value=1)
        quantity_menu = ttk.Combobox(bill_window, values=[str(i) for i in range(1, 11)], textvariable=quantity_var)
        quantity_menu.pack(pady=5)

        # Total price label
        total_price_label = ctk.CTkLabel(bill_window, text="Total Price: $20", font=("Arial", 16, "bold"))
        total_price_label.pack(pady=5)

        # Update total price dynamically
        def update_total_price(*args):
            quantity = int(quantity_var.get())
            total_price_label.configure(text=f"Total Price: ${quantity * 20}")

        quantity_var.trace_add("write", update_total_price)

        # Function to print/save the bill
        def print_bill():
            quantity = int(quantity_var.get())
            total_price = quantity * 20
            bill_content = (
                f"Book: {book_info[0]}\n"
                f"Author: {book_info[1]}\n"
                f"Genre: {book_info[2]}\n"
                f"Quantity: {quantity}\n"
                f"Total Price: ${total_price}\n"
            )
            with open("bill.txt", "w") as file:
                file.write(bill_content)
                messagebox.showinfo("Bill Generated", f"Bill saved as 'bill.txt'\n\n{bill_content}")

        # Confirm Purchase function
        def confirm_purchase():
            messagebox.showinfo("Purchase Successful", f"You have purchased {quantity_var.get()} copies of '{book_info[0]}'!")

        # Buttons
        ctk.CTkButton(bill_window, text="Print Bill", command=print_bill).pack(pady=5)
        ctk.CTkButton(bill_window, text="Confirm Purchase", fg_color="green", command=confirm_purchase).pack(pady=5)

    # UI for book selection
    label = ctk.CTkLabel(main_frame, text="Buy Books", font=("Arial", 24, "bold"))
    label.pack(pady=10)

    table_frame = ttk.Frame(main_frame, borderwidth=2, relief="solid")
    table_frame.pack(pady=10, padx=20, expand=True, fill="both")

    columns = ("Title", "Author", "Genre")
    book_table = ttk.Treeview(table_frame, columns=columns, show="headings", height=10)
    for col in columns:
        book_table.heading(col, text=col, anchor="center")
        book_table.column(col, width=200, anchor="center")

    for book in load_books():
        book_table.insert("", "end", values=(book["title"], book["author"], book["genre"]))

    book_table.pack(expand=True, fill="both")

    ctk.CTkButton(main_frame, text="Generate Bill", command=generate_bill).pack(pady=10)
# Contact Us Page
def contact_us():
    label = ctk.CTkLabel(main_frame, text="Aryan Shrestha", font=("Arial", 24, "bold"))
    label.pack(pady=20)
    
    ctk.CTkLabel(main_frame, text="Email: support@elibrary.com\nPhone: +123456789", font=("Arial", 14)).pack(pady=10)

# About Us Page
def about_us():
    label = ctk.CTkLabel(main_frame, text="About Us", font=("Arial", 24, "bold"))
    label.pack(pady=20)
    
    ctk.CTkLabel(main_frame, text="Our team\n1.Aryan Shrestha\n2.MnajilBasnet\n3.Abhishekhatiwada\n4.Arbaz rain", font=("Arial", 14)).pack(pady=10)

# Sidebar Navigation
sidebar = ctk.CTkFrame(root, width=200, corner_radius=10)
sidebar.pack(side="left", fill="y")

buttons = [
    ("Home", home_page),
    ("Books Available", books_available),
    ("Buy", buy_books),
    ("Contact Us", contact_us),
    ("About Us", about_us)
]

for text, command in buttons:
    btn = ctk.CTkButton(sidebar, text=text, command=lambda cmd=command: show_frame(cmd), font=("Arial", 14), corner_radius=10)
    btn.pack(pady=15, padx=10)

# Main Content Area
main_frame = ctk.CTkFrame(root)
main_frame.pack(side="right", expand=True, fill="both")

# Show Home Page Initially
show_frame(home_page)

root.mainloop()
=======
from tkinter import *
from customtkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox

# Arbaz Comment

win = CTk()
win.iconbitmap("logo.png")
win.geometry("1920x1080")  # Set a smaller window size

Librarian_ID = "0956"

# Create the background frame with a custom color
bg_frame = CTkFrame(master=win, fg_color="#dfd8ee", corner_radius=0)
bg_frame.pack(fill="both", expand=True)

# Create the outer frame with a blue color
outerFrame = CTkFrame(master=bg_frame, fg_color="#ffffff", height=1000, width=1700, corner_radius=2)
outerFrame.pack(anchor = CENTER, padx=65, pady=65)

# Creating the inner frame for image
photoInnerFrame = CTkFrame(master=outerFrame, height=1000, width=600, corner_radius=0)
photoInnerFrame.place(x=0,y=0)

#Loading the image with Image.open
image = Image.open("loginPhoto.jpg")
image = image.resize((800,1000))
photo = ImageTk.PhotoImage(image)

image_Label = CTkLabel(master=photoInnerFrame, image=photo, text="")
image_Label.pack()

#Welcome Button

welcome = CTkLabel(master=outerFrame, text="Feel free to read whatever you like!", 
                   text_color="#d74e3c",
                   font = ("Georgia Bold",30))
welcome.place(relx = 0.53, rely = 0.1)

loginView = CTkTabview(master=outerFrame, 
                        height= 400, width = 400,
                        fg_color="#dfd8ee")
loginView.add("Login")
loginView.add("Create New")
loginView.place(relx = 0.6, rely = 0.2)


##############Loginnnnnnnnn#######

def checkLogin():
    if Login_password_Entry.get() == '' or Login_username_Entry.get() == '':
        messagebox.showerror("Invalid Credentials", "All fields are mandatory")
    else:
        pass
#Creating username entities

Login_usernameLabel = CTkLabel(master=loginView.tab("Login"), 
                         text = "Username:", text_color="black",
                         font=("Helvatica",20),
                         width = 30, height = 30,
                         )
Login_usernameLabel.place(relx = 0.12, rely = 0.06)

# Creating entry box for username:

Login_username_Entry = CTkEntry(master=loginView.tab("Login"),
                    border_color="black",
                    corner_radius=7,
                    placeholder_text="Enter your username",
                    fg_color="#ffffff",
                    text_color="black",
                    height = 40, width = 300)
Login_username_Entry.place(relx=0.12, rely=0.156)


#Creating password entities

Login_passwordLabel = CTkLabel(master = loginView.tab("Login"), 
                         text = "Password:", text_color="black",
                         font=("Helvatica",20),
                         width = 30, height = 30,
                         )
Login_passwordLabel.place(relx = 0.12, rely = 0.3)

# Creating entry box for username:

Login_password_Entry = CTkEntry(master=loginView.tab("Login"),
                    corner_radius=7,
                    placeholder_text="Enter your password",
                    height = 40,
                    fg_color="#ffffff",
                    text_color="black",
                    width = 300)
Login_password_Entry.place(relx=0.12, rely=0.4)

login_button = CTkButton(master=loginView.tab("Login"),
                        text = "Log in",
                        font=("Calibri",20),
                        corner_radius=15,
                        fg_color="green",
                        height=40, width = 300,
                        command = checkLogin)
login_button.place(x = 50, y = 200)


def open_new_window(event):
    forgot_win = Toplevel()
    forgot_win.geometry("300x200+200+100")  # Width x Height + x_offset + y_offset
    forgot_win.title("New Window")
    forgot_win.resizable(False, False)
    forgot_win.configure(bg="#ADD8E6")

    label = CTkLabel(master=forgot_win, text="This is a new window!", text_color="black")
    label.pack(pady=20)

    close_button = CTkButton(master=forgot_win, text="Close", command=forgot_win.destroy)
    close_button.pack(pady=20)
    forgot_win.pack()

#Forgot password? label:


# Label that opens a new window when clicked
forgot_label = Label(master = loginView.tab("Login"),
                        text = "Forgot password?",
                        fg="black",
                        bg="#dfd8ee",
                        font = ("Calibri",20,"underline"))

forgot_label.place(x = 145, y = 340 )
forgot_label.bind("<Button-1>", open_new_window)  











##############################Create New##########################



######## Creating Username Label for Create New Account

Create_usernameLabel = CTkLabel(master=loginView.tab("Create New"), 
                         text = "Username:", text_color="black",
                         font=("Helvatica",20),
                         width = 30, height = 30,
                         )
Create_usernameLabel.place(relx = 0.12, rely = 0.06)


# Creating Entrybox of username for Create New Account:

Create_username_Entry = CTkEntry(master=loginView.tab("Create New"),
                    border_color="black",
                    corner_radius=7,
                    placeholder_text="Enter your username",
                    fg_color="#ffffff",
                    text_color="black",
                    height = 40, width = 300)
Create_username_Entry.place(relx=0.12, rely=0.156)


#### Password Entrybox for Create New Account ########

Create_password_Entry = CTkEntry(master=loginView.tab("Create New"),
                    corner_radius=7,
                    placeholder_text="Enter your password",
                    height = 40,
                    fg_color="#ffffff",
                    text_color="black",
                    width = 300)
Create_password_Entry.place(relx=0.12, rely=0.4)



#Creating password entities for Create New Account

Create_passwordLabel = CTkLabel(master = loginView.tab("Create New"), 
                         text = "Password:", text_color="black",
                         font=("Helvatica",20),
                         width = 30, height = 30,
                         )
Create_passwordLabel.place(relx = 0.12, rely = 0.3)


######## Radio button : Choose user or librarian while creating a account 

user_or_librarian = StringVar()

# Radio buttons
radio_User = CTkRadioButton(master=loginView.tab("Create New"), text="User",
                            variable= user_or_librarian,
                            value="1",
                            text_color="black")
radio_User.place(x = 90, y = 210)

radio_Librarian = CTkRadioButton(master=loginView.tab("Create New"),
                                text="Librarian", 
                                variable= user_or_librarian, 
                                value="2", 
                                text_color="black")
radio_Librarian.place(x = 210, y = 210)

###### New windoww


def open_new_win_create():

    #Creating a new window for validation of librarian 

    new_win_Create = Toplevel()
    new_win_Create.geometry("450x400+1150+310")
    new_win_Create.title("Librarian Verification")
    new_win_Create.resizable(False,False)
    new_win_Create.attributes('-toolwindow', True)
    new_win_Create.configure(bg="#dfd8ee")  

    #Label asking ID

    Librarian_ID_Label = CTkLabel(master = new_win_Create,
                            text = "Enter your Librarian ID: ",
                            text_color="black",
                            font = ("Arial Bold", 22) )
    Librarian_ID_Label.place(relx = 0.1, rely = 0.25)

    #Entry box to put ID

    Librarian_ID_Entry = CTkEntry(master= new_win_Create,
                    corner_radius=7,
                    placeholder_text="Enter your password",
                    height = 40,
                    fg_color="#ffffff",
                    text_color="black",
                    width = 300)
    Librarian_ID_Entry.place(relx=0.1, rely=0.4)


    ###### Popup message for successful verification of Librarian when creating an account 

    def show_popup():
        messagebox.showinfo("Account Created", "Account Created Successfully, Please Login")


    ##########Verification of the ID
    
    def id_Check():
        if Librarian_ID_Entry.get() == "0956":
            Create_username_Entry.delete(0,END)
            Create_password_Entry.delete(0,END)
            show_popup()
            new_win_Create.destroy()
        else:
            incorrect_Label = CTkLabel(master = new_win_Create, text = "Incorrect! Please try again",text_color="red")
            incorrect_Label.place(x=105,y=250)


    #Submit button for the ID

    Librarian_ID_Submit = CTkButton(master = new_win_Create,
                                    text = "Submit",
                                    fg_color="green",
                                    font = ("Calibri",18),
                                    command= id_Check
                                    )
    Librarian_ID_Submit.place(x = 102, y = 185)


    new_win_Create.mainloop()
    new_win_Create.mainloop()


def checkRadio():
    if Create_password_Entry.get() == '' or Create_username_Entry.get() == '' or user_or_librarian.get() == '':
        messagebox.showerror("Invalid Credentials", "All fields are mandatory")
    elif user_or_librarian.get() == "2":
        open_new_win_create()
    elif user_or_librarian.get() == '1':
        Create_username_Entry.delete(0,END)
        Create_password_Entry.delete(0,END)
        messagebox.showinfo("User Account Created", "Done, Please Login")
    else:
        pass

##### Final Create Account Button #####

Create_button = CTkButton(master=loginView.tab("Create New"),
                        text = "Create Account",
                        font=("Calibri",20),
                        corner_radius=15,
                        fg_color="green",
                        height=40, width = 300, command= checkRadio)
Create_button.place(x = 50, y = 260)

win.mainloop()  # Make the window visible

>>>>>>> arbaz
