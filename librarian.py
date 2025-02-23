from tkinter import *
from customtkinter import *
from tkinter import ttk
from tkinter import messagebox

def main():
    # Initialize the main window
    root = CTk()
    root.geometry("900x600")
    root.title("E-Library Management System - Librarian Dashboard")

    # List to hold the requested books and available books
    requested_books = []
    available_books = [
        {"title": "The Hitchhiker's Guide to the Galaxy", "author": "Douglas Adams", "genre": "Science Fiction"},
        {"title": "Pride and Prejudice", "author": "Jane Austen", "genre": "Romance"},
        {"title": "To Kill a Mockingbird", "author": "Harper Lee", "genre": "Southern Gothic"},
        {"title": "1984", "author": "George Orwell", "genre": "Dystopian"},
        {"title": "The Lord of the Rings", "author": "J.R.R. Tolkien", "genre": "Fantasy"},
    ]

    # Main Content Frame
    main_frame = CTkFrame(root)
    main_frame.pack(side="top", expand=True, fill="both")

    # Sidebar Navigation at the bottom
    sidebar = CTkFrame(root, height=60, corner_radius=10)
    sidebar.pack(side="bottom", fill="x")

    # Function to switch frames dynamically
    def show_frame(frame_func):
        for widget in main_frame.winfo_children():
            widget.destroy()
        frame_func()  # Call the function to display the new frame

    # Home Page
    def home_page():
        label = CTkLabel(main_frame, text="Welcome to the Librarian Dashboard", font=("Arial", 24, "bold"))
        label.pack(pady=20)
        desc = CTkLabel(main_frame, text="Manage books and user requests here.", font=("Arial", 14))
        desc.pack(pady=10)

    # Books Available Page with Search
    def books_available():
        def search_books():
            query = search_entry.get().lower()
            filtered_books = [book for book in available_books if query in book["title"].lower() or query in book["author"].lower()]

            # Update the book table with filtered results
            for item in book_table.get_children():
                book_table.delete(item)

            for book in filtered_books:
                book_table.insert("", "end", values=(book["title"], book["author"], book["genre"]))

        label = CTkLabel(main_frame, text="Books Available", font=("Arial", 24, "bold"))
        label.pack(pady=10)

        search_frame = CTkFrame(main_frame)
        search_frame.pack(pady=10, padx=20)

        search_label = CTkLabel(search_frame, text="Search Books:")
        search_label.grid(row=0, column=0, padx=10, pady=5)
        search_entry = CTkEntry(search_frame)
        search_entry.grid(row=0, column=1, padx=10, pady=5)
        search_button = CTkButton(search_frame, text="Search", command=search_books)
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

        # Insert the dummy available books data
        for book in available_books:
            book_table.insert("", "end", values=(book["title"], book["author"], book["genre"]))

    # Requested Books Page
    def requested_books():
        def delete_request(index):
            requested_books.pop(index)
            update_requested_books()

        def move_to_available(index):
            book = requested_books.pop(index)
            available_books.append(book)  # Move to the available books list
            update_requested_books()
            update_books_available()  # Update the available books section

        def update_requested_books():
            for widget in requested_frame.winfo_children():
                widget.destroy()

            if requested_books:
                label = CTkLabel(requested_frame, text="Requested Books", font=("Arial", 20, "bold"))
                label.pack(pady=10)

                columns = ("Title", "Author", "Date Needed", "Action", "Arrived")
                request_table = ttk.Treeview(requested_frame, columns=columns, show="headings", height=10)

                for col in columns:
                    request_table.heading(col, text=col, anchor="center")
                    request_table.column(col, width=120, anchor="center")

                request_table.pack(expand=True, fill="both")
                for idx, request in enumerate(requested_books):
                    request_table.insert("", "end", values=(request["title"], request["author"], request["date_needed"], "Delete", "Arrived"))
                    # Correct lambda closure for delete and move to available
                    request_table.bind("<Double-1>", lambda event, index=idx: delete_request(index))
                    request_table.bind("<ButtonRelease-1>", lambda event, index=idx: move_to_available(index) if request_table.identify_region(event.x, event.y) == "cell" and event.widget.column("#5") == "Arrived" else None)

        # Requested Books Section
        requested_frame = CTkFrame(main_frame)
        requested_frame.pack(pady=10, expand=True, fill="both")

        update_requested_books()

    # Add Sidebar Navigation
    home_button = CTkButton(sidebar, text="Home", command=lambda: show_frame(home_page))
    home_button.pack(side="left", padx=10)

    books_button = CTkButton(sidebar, text="Books Available", command=lambda: show_frame(books_available))
    books_button.pack(side="left", padx=10)

    requested_button = CTkButton(sidebar, text="Requested Books", command=lambda: show_frame(requested_books))
    requested_button.pack(side="left", padx=10)

    # Exit Button to close the program
    def exit_program():
        root.quit()  # This will terminate the program

    exit_button = CTkButton(sidebar, text="Exit", command=exit_program, font=("Arial", 14), corner_radius=10)
    exit_button.pack(side="left", padx=10, pady=10)

    # Default View: Home Page
    show_frame(home_page)

    root.mainloop()