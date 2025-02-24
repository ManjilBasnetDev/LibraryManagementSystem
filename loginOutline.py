from tkinter import *
from customtkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
from tkcalendar import DateEntry
import sqlite3
import os  # Added for file existence check
import user_Home  # Import the home page module
import librarian  # Import the librarian module
import forgot  # Import the forgot password module

Librarian_ID = "0956"

# ==================== SQLite3 Backend Code ====================

def initialize_db():
    """
    Initializes the database and creates the 'users' table if it doesn't exist.
    """
    conn = sqlite3.connect("library_users.db")
    cursor = conn.cursor()
    
    # Create the users table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            role TEXT NOT NULL CHECK(role IN ('user', 'librarian')),
            security_question TEXT,
            security_answer TEXT
        )
    ''')
    
    # Check if the security_question column exists, and if not, add it
    cursor.execute("PRAGMA table_info(users)")
    columns = cursor.fetchall()
    column_names = [column[1] for column in columns]
    
    if 'security_question' not in column_names:
        cursor.execute("ALTER TABLE users ADD COLUMN security_question TEXT")
    
    if 'security_answer' not in column_names:
        cursor.execute("ALTER TABLE users ADD COLUMN security_answer TEXT")
    
    conn.commit()
    conn.close()

def register_user(username, password, role, security_question, security_answer):
    """
    Registers a new user or librarian in the database.

    Args:
        username (str): The username of the user.
        password (str): The password of the user.
        role (str): The role of the user ('user' or 'librarian').
        security_question (str): The security question for password recovery.
        security_answer (str): The answer to the security question.

    Returns:
        bool: True if registration is successful, False otherwise.
    """
    conn = None  # Initialize conn to avoid NameError in finally block
    try:
        conn = sqlite3.connect("library_users.db")
        cursor = conn.cursor()

        # Insert the new user into the database
        cursor.execute("INSERT INTO users (username, password, role, security_question, security_answer) VALUES (?, ?, ?, ?, ?)",
                      (username, password, role, security_question, security_answer))
        conn.commit()  # Commit the transaction
        return True  # Registration successful

    except sqlite3.IntegrityError:
        # Handle duplicate username error
        print("Error: Username already exists.")
        return False

    except sqlite3.OperationalError as e:
        # Handle database operational errors (e.g., table doesn't exist, database locked)
        print(f"Database error: {e}")
        return False

    except sqlite3.Error as e:
        # Handle any other SQLite errors
        print(f"An error occurred: {e}")
        return False

    finally:
        # Ensure the database connection is closed
        if conn:
            conn.close()

def check_login(username, password):
    """
    Checks the login credentials and returns the role of the user.

    Args:
        username (str): The username of the user.
        password (str): The password of the user.

    Returns:
        str: The role of the user ('user' or 'librarian') if credentials are valid, otherwise None.
    """
    conn = None
    try:
        conn = sqlite3.connect("library_users.db")
        cursor = conn.cursor()
        
        cursor.execute("SELECT role FROM users WHERE username = ? AND password = ?", (username, password))
        result = cursor.fetchone()
        
        if result:
            return result[0]  # Return the role (user or librarian)
        else:
            return None  # Invalid credentials

    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return None

    finally:
        if conn:
            conn.close()

# Initialize the database when the script is run
initialize_db()

# ==================== End of SQLite3 Backend Code ====================

# ==================== GUI Setup ====================

win = CTk()
win.geometry("1920x1080")

# Function to handle user registration (GUI logic)
def register_user_gui():
    username = Create_username_Entry.get()
    password = Create_password_Entry.get()
    role = "user" if user_or_librarian.get() == "1" else "librarian"
    
    if not username or not password or not user_or_librarian.get():
        messagebox.showerror("Error", "All fields are required!")
        return
    
    # Open a new window for security question and answer
    security_window = CTkToplevel(win)
    security_window.title("Security Question")
    security_window.geometry("400x300")

    # Security Question Label
    security_question_label = CTkLabel(security_window, text="What is your favorite color?", font=("Helvetica", 16))
    security_question_label.pack(pady=20)

    # Security Answer Entry
    security_answer_entry = CTkEntry(security_window, placeholder_text="Enter your favorite color", width=300)
    security_answer_entry.pack(pady=10)

    # Submit Button
    def submit_security():
        security_answer = security_answer_entry.get()
        if not security_answer:
            messagebox.showerror("Error", "Security answer is required!")
            return
        
        # Call the backend function to register the user
        if register_user(username, password, role, "What is your favorite color?", security_answer):
            messagebox.showinfo("Success", "Account created successfully. Please log in.")
            Create_username_Entry.delete(0, END)
            Create_password_Entry.delete(0, END)
            security_window.destroy()  # Close the security window
        else:
            messagebox.showerror("Error", "Username already exists!")

    submit_button = CTkButton(security_window, text="Submit", command=submit_security)
    submit_button.pack(pady=20)

# Function to check login credentials (GUI logic)
def check_login_gui():
    username = Login_username_Entry.get()
    password = Login_password_Entry.get()
    
    if not username or not password:
        messagebox.showerror("Error", "All fields are required!")
        return
    
    role = check_login(username, password)
    
    if role == "user":
        messagebox.showinfo("Success", "User Login Successful")
        
        # Close the login window
        win.destroy()
        
        # Open the home page
        user_Home.main()  # Call the main function of the home page
    
    elif role == "librarian":
        messagebox.showinfo("Success", "Librarian Login Successful")
        
        # Close the login window
        win.destroy()
        
        # Open the librarian dashboard
        librarian.main()  # Call the main function of the librarian module
    
    else:
        messagebox.showerror("Error", "Invalid credentials!")

# Function to open the forgot password window
def open_forgot_password():
    forgot_window = CTkToplevel(win)
    forgot_window.title("Forgot Password")
    forgot_window.geometry("400x400")
    forgot.ForgetPasswordPage(forgot_window)  # Open the forgot password page

# GUI Elements Setup
bg_frame = CTkFrame(master=win, fg_color="#dfd8ee", corner_radius=0)
bg_frame.pack(fill="both", expand=True)

outerFrame = CTkFrame(master=bg_frame, fg_color="#ffffff", height=1000, width=1700, corner_radius=2)
outerFrame.pack(anchor=CENTER, padx=65, pady=65)

photoInnerFrame = CTkFrame(master=outerFrame, height=1000, width=600, corner_radius=0)
photoInnerFrame.place(x=0, y=0)

# Ensure image exists before loading
image_path = "loginPhoto.jpg"
if os.path.exists(image_path):
    image = Image.open(image_path).resize((800, 1000))
    photo = ImageTk.PhotoImage(image)  # Store the image in a global variable
    img_label = CTkLabel(master=photoInnerFrame, image=photo, text="")
    img_label.pack()
else:
    messagebox.showerror("Error", "Image file 'loginPhoto.jpg' not found!")

welcome = CTkLabel(master=outerFrame, text="Feel free to read whatever you like!", text_color="#d74e3c", font=("Georgia Bold", 30))
welcome.place(relx=0.53, rely=0.1)

loginView = CTkTabview(master=outerFrame, height=400, width=400, fg_color="#dfd8ee")
loginView.add("Login")
loginView.add("Create New")
loginView.place(relx=0.6, rely=0.2)

# Login Section
CTkLabel(master=loginView.tab("Login"), text="Username:", text_color="black", font=("Helvetica", 20)).place(relx=0.12, rely=0.06)
Login_username_Entry = CTkEntry(master=loginView.tab("Login"), placeholder_text="Enter your username", fg_color="#ffffff", text_color="black", height=40, width=300)
Login_username_Entry.place(relx=0.12, rely=0.156)

CTkLabel(master=loginView.tab("Login"), text="Password:", text_color="black", font=("Helvetica", 20)).place(relx=0.12, rely=0.3)
Login_password_Entry = CTkEntry(master=loginView.tab("Login"), placeholder_text="Enter your password", height=40, fg_color="#ffffff", text_color="black", width=300, show="*")
Login_password_Entry.place(relx=0.12, rely=0.4)

# Forgot Password Label
forgot_password_label = CTkLabel(master=loginView.tab("Login"), text="Forgot Password?", text_color="black", font=("Helvetica", 20, "underline"), cursor="hand2")
forgot_password_label.place(relx=0.285, rely=0.75)
forgot_password_label.bind("<Button-1>", lambda e: open_forgot_password())

CTkButton(master=loginView.tab("Login"), text="Log in", font=("Calibri", 20), corner_radius=15, fg_color="green", height=40, width=300, command=check_login_gui).place(x=50, y=200)

# Registration Section
CTkLabel(master=loginView.tab("Create New"), text="Username:", text_color="black", font=("Helvetica", 20)).place(relx=0.12, rely=0.06)
Create_username_Entry = CTkEntry(master=loginView.tab("Create New"), placeholder_text="Enter your username", fg_color="#ffffff", text_color="black", height=40, width=300)
Create_username_Entry.place(relx=0.12, rely=0.156)

CTkLabel(master=loginView.tab("Create New"), text="Password:", text_color="black", font=("Helvetica", 20)).place(relx=0.12, rely=0.3)
Create_password_Entry = CTkEntry(master=loginView.tab("Create New"), placeholder_text="Enter your password", height=40, fg_color="#ffffff", text_color="black", width=300, show="*")
Create_password_Entry.place(relx=0.12, rely=0.4)

user_or_librarian = StringVar()
CTkRadioButton(master=loginView.tab("Create New"), text="User", variable=user_or_librarian, value="1", text_color="black").place(x=90, y=210)
CTkRadioButton(master=loginView.tab("Create New"), text="Librarian", variable=user_or_librarian, value="2", text_color="black").place(x=210, y=210)

CTkButton(master=loginView.tab("Create New"), text="Create Account", font=("Calibri", 20), corner_radius=15, fg_color="green", height=40, width=300, command=register_user_gui).place(x=50, y=260)

win.mainloop()  # Make the window visible