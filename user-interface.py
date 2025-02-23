import tkinter as tk
import customtkinter as ctk
from tkinter import ttk
from tkinter import messagebox

# Initialize the main window
root = ctk.CTk()
root.geometry("900x600")
root.title("E-Library Management System")

# List to hold the requested books
requested_books = []

# Main Content Frame
main_frame = ctk.CTkFrame(root)
main_frame.pack(side="top", expand=True, fill="both")

# Sidebar Navigation at the bottom
sidebar = ctk.CTkFrame(root, height=60, corner_radius=10)
sidebar.pack(side="bottom", fill="x")

# Function to switch frames dynamically
def show_frame(frame_func):
    for widget in main_frame.winfo_children():
        widget.destroy()
    frame_func()  # Call the function to display the new frame

# Load Books (dummy data)
def load_books():
    return [
        {"title": "The Hitchhiker's Guide to the Galaxy", "author": "Douglas Adams", "genre": "Science Fiction"},
        {"title": "Pride and Prejudice", "author": "Jane Austen", "genre": "Romance"},
        {"title": "To Kill a Mockingbird", "author": "Harper Lee", "genre": "Southern Gothic"},
        {"title": "1984", "author": "George Orwell", "genre": "Dystopian"},
        {"title": "The Lord of the Rings", "author": "J.R.R. Tolkien", "genre": "Fantasy"},
    ]

# Home Page
def home_page():
    label = ctk.CTkLabel(main_frame, text="Welcome to the E-Library", font=("Arial", 24, "bold"))
    label.pack(pady=20)
    desc = ctk.CTkLabel(main_frame, text="Your digital library for books and resources.", font=("Arial", 14))
    desc.pack(pady=10)

# Books Available Page with Search
def books_available():
    def search_books():
        query = search_entry.get().lower()
        filtered_books = [book for book in load_books() if query in book["title"].lower() or query in book["author"].lower()]

        # Update the book table with filtered results
        for item in book_table.get_children():
            book_table.delete(item)

        for book in filtered_books:
            book_table.insert("", "end", values=(book["title"], book["author"], book["genre"]))

    label = ctk.CTkLabel(main_frame, text="Books Available", font=("Arial", 24, "bold"))
    label.pack(pady=10)

    search_frame = ctk.CTkFrame(main_frame)
    search_frame.pack(pady=10, padx=20)

    search_label = ctk.CTkLabel(search_frame, text="Search Books:")
    search_label.grid(row=0, column=0, padx=10, pady=5)
    search_entry = ctk.CTkEntry(search_frame)
    search_entry.grid(row=0, column=1, padx=10, pady=5)
    search_button = ctk.CTkButton(search_frame, text="Search", command=search_books)
    search_button.grid(row=0, column=2, padx=10, pady=5)

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

# Request Book Page
def request_books():
    def submit_request():
        title = title_entry.get()
        author = author_entry.get()
        genre = genre_entry.get()
        date_needed = date_needed_entry.get()

        if title and author and genre and date_needed:
            # Add the request to the pending list
            requested_books.append({"title": title, "author": author, "genre": genre, "date_needed": date_needed})
            messagebox.showinfo("Request Submitted", "Your book request has been submitted!")

            # Update the pending section
            update_pending_requests()

        else:
            messagebox.showerror("Incomplete Form", "Please fill in all the fields.")

    def delete_request(index):
        requested_books.pop(index)
        update_pending_requests()

    def update_pending_requests():
        for widget in pending_frame.winfo_children():
            widget.destroy()

        if requested_books:
            label = ctk.CTkLabel(pending_frame, text="Pending Book Requests", font=("Arial", 20, "bold"))
            label.pack(pady=10)

            columns = ("Title", "Author", "Genre", "Date Needed", "Action")
            request_table = ttk.Treeview(pending_frame, columns=columns, show="headings", height=10)

            for col in columns:
                request_table.heading(col, text=col, anchor="center")
                request_table.column(col, width=150, anchor="center")

            request_table.pack(expand=True, fill="both")
            for idx, request in enumerate(requested_books):
                request_table.insert("", "end", values=(request["title"], request["author"], request["genre"], request["date_needed"], "Delete"))
                request_table.bind("<Double-1>", lambda event, index=idx: delete_request(index))

    label = ctk.CTkLabel(main_frame, text="Request a Book", font=("Arial", 24, "bold"))
    label.pack(pady=20)

    form_frame = ctk.CTkFrame(main_frame)
    form_frame.pack(pady=10)

    ctk.CTkLabel(form_frame, text="Title of the Book:").grid(row=0, column=0, padx=10, pady=5)
    title_entry = ctk.CTkEntry(form_frame)
    title_entry.grid(row=0, column=1, padx=10, pady=5)

    ctk.CTkLabel(form_frame, text="Author of the Book:").grid(row=1, column=0, padx=10, pady=5)
    author_entry = ctk.CTkEntry(form_frame)
    author_entry.grid(row=1, column=1, padx=10, pady=5)

    ctk.CTkLabel(form_frame, text="Genre of the Book:").grid(row=2, column=0, padx=10, pady=5)
    genre_entry = ctk.CTkEntry(form_frame)
    genre_entry.grid(row=2, column=1, padx=10, pady=5)

    ctk.CTkLabel(form_frame, text="Date Needed (DD/MM/YYYY):").grid(row=3, column=0, padx=10, pady=5)
    date_needed_entry = ctk.CTkEntry(form_frame)
    date_needed_entry.grid(row=3, column=1, padx=10, pady=5)

    ctk.CTkButton(main_frame, text="Submit Request", command=submit_request).pack(pady=10)

    # Pending Request Section
    pending_frame = ctk.CTkFrame(main_frame)
    pending_frame.pack(pady=10, expand=True, fill="both")

    update_pending_requests()

# Contact Us Page
def contact_us():
    label = ctk.CTkLabel(main_frame, text="Contact Us", font=("Arial", 24, "bold"))
    label.pack(pady=20)

    contact_info = ctk.CTkLabel(main_frame, text="Email: support@elibrary.com\nPhone: +1234567890", font=("Arial", 14))
    contact_info.pack(pady=10)

# About Page
def about():
    label = ctk.CTkLabel(main_frame, text="About Us", font=("Arial", 24, "bold"))
    label.pack(pady=20)

    about_info = ctk.CTkLabel(main_frame, text="We are an online platform offering a collection of books for readers around the world.\nOur mission is to make knowledge accessible to everyone.", font=("Arial", 14))
    about_info.pack(pady=10)

# Sidebar Buttons (now at the bottom)
buttons = [
    ("Home", home_page),
    ("Books Available", books_available),
    ("Request Books", request_books),
    ("Contact Us", contact_us),
    ("About", about),
]

for text, command in buttons:
    btn = ctk.CTkButton(sidebar, text=text, command=lambda cmd=command: show_frame(cmd), font=("Arial", 14), corner_radius=10)
    btn.pack(side="left", padx=10, pady=10)

# Exit Button at the end of the sidebar
def exit_program():
    root.quit()  # This will terminate the program

exit_button = ctk.CTkButton(sidebar, text="Exit", command=exit_program, font=("Arial", 14), corner_radius=10)
exit_button.pack(side="left", padx=10, pady=10)

# Show Home Page Initially
show_frame(home_page)

# Run the main loop
root.mainloop()
