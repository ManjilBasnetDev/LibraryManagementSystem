import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import messagebox
import webbrowser
import sqlite3
from tkcalendar import DateEntry

# Initialize the main window for login
login_win = ctk.CTk()
login_win.iconbitmap("D:\TestProject\LibraryManagementSystem\logo.png")
login_win.geometry("1920x1080")  # Set a smaller window size

# Create the background frame with a custom color
bg_frame = ctk.CTkFrame(master=login_win, fg_color="#dfd8ee", corner_radius=0)
bg_frame.pack(fill="both", expand=True)

# Create the outer frame with a blue color
outerFrame = ctk.CTkFrame(master=bg_frame, fg_color="#ffffff", height=1000, width=1700, corner_radius=2)
outerFrame.pack(anchor=tk.CENTER, padx=65, pady=65)

# Creating the inner frame for image
photoInnerFrame = ctk.CTkFrame(master=outerFrame, height=1000, width=600, corner_radius=0)
photoInnerFrame.place(x=0, y=0)

# Loading the image with Image.open
image = Image.open("loginPhoto.jpg")
image = image.resize((800, 1000))
photo = ImageTk.PhotoImage(image)

image_Label = ctk.CTkLabel(master=photoInnerFrame, image=photo, text="")
image_Label.pack()

# Welcome Button
welcome = ctk.CTkLabel(master=outerFrame, text="Feel free to read whatever you like!",
                       text_color="#d74e3c",
                       font=("Georgia Bold", 30))
welcome.place(relx=0.53, rely=0.1)

loginView = ctk.CTkTabview(master=outerFrame,
                           height=400, width=400,
                           fg_color="#dfd8ee")
loginView.add("Login")
loginView.add("Create New")
loginView.place(relx=0.6, rely=0.2)

# Login Functionality
def checkLogin():
    username = Login_username_Entry.get()
    password = Login_password_Entry.get()
    if username == '' or password == '':
        messagebox.showerror("Invalid Credentials", "All fields are mandatory")
    elif (username == 'Manjil' and password == 'Basnet') or (username == 'UserC' and password == 'PasswordC'):
        messagebox.showinfo('Done', "User Successful")
        login_win.destroy()  # Close the login window
        open_dashboard()  # Open the dashboard
    elif (username == 'Librarian' and password == '12345') or (username == 'LibrarianC' and password == 'password123'):
        messagebox.showinfo('Done', "Librarian Successful")
        login_win.destroy()  # Close the login window
        open_dashboard()  # Open the dashboard
    else:
        messagebox.showerror('Error', 'Invalid Details')

# Creating username entities
Login_usernameLabel = ctk.CTkLabel(master=loginView.tab("Login"),
                                   text="Username:", text_color="black",
                                   font=("Helvatica", 20),
                                   width=30, height=30,
                                   )
Login_usernameLabel.place(relx=0.12, rely=0.06)

# Creating entry box for username:
Login_username_Entry = ctk.CTkEntry(master=loginView.tab("Login"),
                                    border_color="black",
                                    corner_radius=7,
                                    placeholder_text="Enter your username",
                                    fg_color="#ffffff",
                                    text_color="black",
                                    height=40, width=300)
Login_username_Entry.place(relx=0.12, rely=0.156)

# Creating password entities
Login_passwordLabel = ctk.CTkLabel(master=loginView.tab("Login"),
                                   text="Password:", text_color="black",
                                   font=("Helvatica", 20),
                                   width=30, height=30,
                                   )
Login_passwordLabel.place(relx=0.12, rely=0.3)

# Creating entry box for password:
Login_password_Entry = ctk.CTkEntry(master=loginView.tab("Login"),
                                    corner_radius=7,
                                    placeholder_text="Enter your password",
                                    height=40,
                                    fg_color="#ffffff",
                                    text_color="black",
                                    width=300)
Login_password_Entry.place(relx=0.12, rely=0.4)

login_button = ctk.CTkButton(master=loginView.tab("Login"),
                             text="Log in",
                             font=("Calibri", 20),
                             corner_radius=15,
                             fg_color="green",
                             height=40, width=300,
                             command=checkLogin)
login_button.place(x=50, y=200)

# Function to open the dashboard
def open_dashboard():
    # Initialize the main window for the dashboard
    dashboard_win = ctk.CTk()
    dashboard_win.geometry("900x600")
    dashboard_win.title("E-Library Management System")

    # Function to switch frames dynamically
    def show_frame(frame):
        for widget in main_frame.winfo_children():
            widget.destroy()
        frame()

    # Home Page
    def home_page():
        label = ctk.CTkLabel(main_frame, text="Welcome to the E-Library", font=("Arial", 24, "bold"))
        label.pack(pady=20)

        desc = ctk.CTkLabel(main_frame, text="Your digital library for books and resources.", font=("Arial", 14))
        desc.pack(pady=10)

    # Books Available Page
    def books_available():
        label = ctk.CTkLabel(main_frame, text="Books Available", font=("Arial", 24, "bold"))
        label.pack(pady=10)

        table_frame = ttk.Frame(main_frame, borderwidth=2, relief="solid")
        table_frame.pack(pady=20, padx=30, expand=True, fill="both")

        columns = ("Title", "Author", "Genre")
        book_table = ttk.Treeview(table_frame, columns=columns, show="headings", height=10)

        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Arial", 26, "bold"))  # Font size for headings
        style.configure("Treeview", font=("Arial", 18), rowheight=50)  # Increased row height for more spacing

        column_widths = {"Title": 600, "Author": 500, "Genre": 450}  # Further increased column widths

        for col in columns:
            book_table.heading(col, text=col, anchor="center")
            book_table.column(col, width=column_widths[col], anchor="center")

        vsb = ttk.Scrollbar(table_frame, orient="vertical", command=book_table.yview)
        vsb.pack(side="right", fill="y")
        book_table.configure(yscrollcommand=vsb.set)
        book_table.pack(expand=True, fill="both", pady=10)

        for book in load_books():
            book_table.insert("", "end", values=(book["title"], book["author"], book["genre"]))

        # Open ManyBooks when a book is double-clicked
        def open_manybooks(event):
            webbrowser.open("https://manybooks.net/", new=1)

        book_table.bind("<Double-1>", open_manybooks)

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

        ctk.CTkLabel(main_frame, text="Our team\n1.Aryan Shrestha\n2.ManjilBasnet\n3.Abhishekhatiwada\n4.Arbaz rain",
                     font=("Arial", 14)).pack(pady=10)

    # Sidebar Navigation
    sidebar = ctk.CTkFrame(dashboard_win, width=200, corner_radius=10, fg_color='#dfd8ee')
    sidebar.pack(side="left", fill="y")

    buttons = [
        ("Home", home_page),
        ("Books Available", books_available),
        ("Buy", buy_books),
        ("Contact Us", contact_us),
        ("About Us", about_us)
    ]

    for text, command in buttons:
        btn = ctk.CTkButton(sidebar, text=text, command=lambda cmd=command: show_frame(cmd), font=("Arial", 14),
                            corner_radius=10)
        btn.pack(pady=20, padx=15)

    # Main Content Area
    main_frame = ctk.CTkFrame(dashboard_win, fg_color="#dfd8ee")
    main_frame.pack(side="right", expand=True, fill="both")

    # Show Home Page Initially
    show_frame(home_page)

    dashboard_win.mainloop()

# Run the login window
login_win.mainloop()