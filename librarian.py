import tkinter as tk
import customtkinter as ctk
from tkinter import ttk
from tkinter import messagebox
import re
import json

def main():
        
    # Initialize the main window
    root = ctk.CTk()
    root.geometry("900x600")
    root.title("E-Library Management System")

    # Dummy data for requested books and available books
    requested_books = [
        {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "date_needed": "2025-03-01", "genre": "Classic"},
        {"title": "Moby Dick", "author": "Herman Melville", "date_needed": "2025-03-15", "genre": "Adventure"},
        {"title": "The Catcher in the Rye", "author": "J.D. Salinger", "date_needed": "2025-04-01", "genre": "Coming-of-age"},
    ]

    available_books = [
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
                {"title": "Handsome", "author": "Manjil Basnet", "genre": "Adventure"},
                {"title": "Little Women", "author": "Louisa May Alcott", "genre": "Coming-of-age"},
                {"title": "One Hundred Years of Solitude", "author": "Gabriel García Márquez", "genre": "Magical Realism"},
                {"title": "Beloved", "author": "Toni Morrison", "genre": "Historical Fiction"},
                {"title": "love", "author": "AryanShrestha", "genre": "Social"}
    ]

    # Main Content Frame
    main_frame = ctk.CTkFrame(root)
    main_frame.pack(side="top", expand=True, fill="both")

    # Sidebar Navigation at the bottom
    sidebar = ctk.CTkFrame(root, height=60, corner_radius=10)
    sidebar.pack(side="bottom", fill="x", pady=10, padx=10)

    # Function to switch frames dynamically
    def show_frame(frame_func):
        for widget in main_frame.winfo_children():
            widget.destroy()
        frame_func()  # Call the function to display the new frame

    # Home Page
    def home_page():
        label = ctk.CTkLabel(main_frame, text="Welcome to the E-Library", font=("Arial", 24, "bold"))
        label.pack(pady=20)
        desc = ctk.CTkLabel(main_frame, text="Your digital library for books and resources.", font=("Arial", 14))
        desc.pack(pady=10)

        # List of users with their details
        users = [
            {"name": "Manjiil", "book_borrowed": "-", "duration": "--"},
            {"name": "Alice Smith", "book_borrowed": "Pride and Prejudice", "duration": "3 weeks"},
            {"name": "Robert Brown", "book_borrowed": "To Kill a Mockingbird", "duration": "1 week"},
            {"name": "Emily White", "book_borrowed": "The Lord of the Rings", "duration": "4 weeks"},
            {"name": "Sophia Johnson", "book_borrowed": "Harry Potter and the Sorcerer's Stone", "duration": "5 weeks"},
        ]

        # Display the user list in a table-like format
        user_list_frame = ctk.CTkFrame(main_frame)
        user_list_frame.pack(pady=30, expand=True, fill="both")

        user_label = ctk.CTkLabel(user_list_frame, text="List of Users", font=("Arial", 20, "bold"))
        user_label.pack(pady=10)

        user_columns = ("Name", "Book Borrowed", "Duration")
        user_table = ttk.Treeview(user_list_frame, columns=user_columns, show="headings", height=5)

        for col in user_columns:
            user_table.heading(col, text=col, anchor="center")
            user_table.column(col, width=200, anchor="center")

        user_table.pack(expand=True, fill="both")

        for user in users:
            user_table.insert("", "end", values=(user["name"], user["book_borrowed"], user["duration"]))

    # Books Available Page with Search
    def books_available():
        def search_books():
            query = search_entry.get().lower()
            genre_filter = genre_var.get()
            filtered_books = [
                book for book in available_books
                if (query in book["title"].lower() or query in book["author"].lower()) and
                (genre_filter == "All" or book["genre"] == genre_filter)
            ]

            # Update the book table with filtered results
            for item in book_table.get_children():
                book_table.delete(item)

            for book in filtered_books:
                book_table.insert("", "end", values=(book["title"], book["author"], book["genre"]))

        def clear_search():
            search_entry.delete(0, "end")
            genre_var.set("All")
            for item in book_table.get_children():
                book_table.delete(item)
            for book in available_books:
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
        clear_button = ctk.CTkButton(search_frame, text="Clear Search", command=clear_search)
        clear_button.grid(row=0, column=3, padx=10, pady=5)
        request_button = ctk.CTkButton(search_frame, text="Request Book", command=request_book)
        request_button.grid(row=0, column=4, padx=10, pady=5)

        genres = list(set(book["genre"] for book in available_books))  # Get unique genres
        genre_label = ctk.CTkLabel(search_frame, text="Filter by Genre:")
        genre_label.grid(row=1, column=0, padx=10, pady=5)
        genre_var = ctk.StringVar(value="All")
        genre_dropdown = ctk.CTkOptionMenu(search_frame, values=["All"] + genres, variable=genre_var)
        genre_dropdown.grid(row=1, column=1, padx=10, pady=5)

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

        for book in available_books:
            book_table.insert("", "end", values=(book["title"], book["author"], book["genre"]))

        back_button = ctk.CTkButton(main_frame, text="Back to Home", command=lambda: show_frame(home_page))
        back_button.pack(pady=10)

    # Requested Books Page
    def show_requested_books():
        def delete_request(index):
            if messagebox.askyesno("Confirm", "Are you sure you want to delete this request?"):
                requested_books.pop(index)  # Use the global list
                update_requested_books()

        def move_to_available(index):
            if messagebox.askyesno("Confirm", "Are you sure you want to move this book to available books?"):
                book = requested_books.pop(index)  # Use the global list
                available_books.append(book)  # Move to the available books list
                update_requested_books()
                show_frame(books_available)  # Refresh the Books Available page

        def update_requested_books():
            # Clear the frame before updating
            for widget in requested_frame.winfo_children():
                widget.destroy()

            if requested_books:  # Use the global list
                label = ctk.CTkLabel(requested_frame, text="Requested Books", font=("Arial", 20, "bold"))
                label.pack(pady=10)

                # Create a table to display requested books
                columns = ("Title", "Author", "Genre", "Date Needed", "Action")
                request_table = ttk.Treeview(requested_frame, columns=columns, show="headings", height=10)

                for col in columns:
                    request_table.heading(col, text=col, anchor="center")
                    request_table.column(col, width=150, anchor="center")

                request_table.pack(expand=True, fill="both")

                # Insert requested books into the table
                for idx, request in enumerate(requested_books):  # Use the global list
                    request_table.insert("", "end", values=(
                        request["title"], 
                        request["author"], 
                        request.get("genre", ""), 
                        request["date_needed"], 
                        "Move to Available"
                    ))

                # Add button frame for each row
                def on_click(event):
                    region = request_table.identify_region(event.x, event.y)
                    if region == "cell":
                        selected_item = request_table.selection()[0]  # Get selected item
                        index = request_table.index(selected_item)  # Get index of the selected item
                        column = request_table.identify_column(event.x)
                        
                        # If clicked on the Action column (column #5)
                        if column == "#5":
                            move_to_available(index)

                # Bind the click action to the table
                request_table.bind("<ButtonRelease-1>", on_click)

        # Requested Books Section
        requested_frame = ctk.CTkFrame(main_frame)
        requested_frame.pack(pady=10, expand=True, fill="both")

        update_requested_books()

        back_button = ctk.CTkButton(main_frame, text="Back to Home", command=lambda: show_frame(home_page))
        back_button.pack(pady=10)

    # Request Book Form
    def request_book():
        def submit_request():
            title = title_entry.get()
            author = author_entry.get()
            date_needed = date_entry.get()
            genre = genre_entry.get()
            
            if title and author and date_needed:
                if re.match(r"\d{4}-\d{2}-\d{2}", date_needed):
                    requested_books.append({
                        "title": title, 
                        "author": author, 
                        "date_needed": date_needed,
                        "genre": genre
                    })
                    messagebox.showinfo("Success", "Book request submitted successfully!")
                    request_window.destroy()
                    show_frame(show_requested_books)  # Refresh the Requested Books page
                else:
                    messagebox.showwarning("Error", "Please enter the date in YYYY-MM-DD format.")
            else:
                messagebox.showwarning("Error", "Please fill in all required fields.")

        request_window = ctk.CTkToplevel(root)
        request_window.title("Request a Book")
        request_window.geometry("400x350")

        title_label = ctk.CTkLabel(request_window, text="Title:")
        title_label.pack(pady=5)
        title_entry = ctk.CTkEntry(request_window)
        title_entry.pack(pady=5)

        author_label = ctk.CTkLabel(request_window, text="Author:")
        author_label.pack(pady=5)
        author_entry = ctk.CTkEntry(request_window)
        author_entry.pack(pady=5)
        
        genre_label = ctk.CTkLabel(request_window, text="Genre:")
        genre_label.pack(pady=5)
        genre_entry = ctk.CTkEntry(request_window)
        genre_entry.pack(pady=5)

        date_label = ctk.CTkLabel(request_window, text="Date Needed (YYYY-MM-DD):")
        date_label.pack(pady=5)
        date_entry = ctk.CTkEntry(request_window)
        date_entry.pack(pady=5)

        submit_button = ctk.CTkButton(request_window, text="Submit", command=submit_request)
        submit_button.pack(pady=20)

    # Save and Load Data
    def save_data():
        try:
            with open("library_data.json", "w") as file:
                json.dump({"requested_books": requested_books, "available_books": available_books}, file)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save data: {e}")

    def load_data():
        try:
            with open("library_data.json", "r") as file:
                data = json.load(file)
                requested_books.extend(data.get("requested_books", []))
                available_books.extend(data.get("available_books", []))
        except FileNotFoundError:
            pass
        except json.JSONDecodeError:
            messagebox.showerror("Error", "Corrupted or invalid data file.")

    # Load data at the start
    load_data()

    # Add Sidebar Navigation
    home_button = ctk.CTkButton(sidebar, text="Home", command=lambda: show_frame(home_page))
    home_button.pack(side="left", padx=10)

    books_button = ctk.CTkButton(sidebar, text="Books Available", command=lambda: show_frame(books_available))
    books_button.pack(side="left", padx=10)

    requested_button = ctk.CTkButton(sidebar, text="Requested Books", command=lambda: show_frame(show_requested_books))
    requested_button.pack(side="left", padx=10)

    # Exit Button to close the program
    def exit_program():
        save_data()
        root.quit()

    exit_button = ctk.CTkButton(sidebar, text="Exit", command=exit_program, font=("Arial", 14), corner_radius=10)
    exit_button.pack(side="left", padx=10, pady=10)

    # Default View: Home Page
    show_frame(home_page)

    root.mainloop()