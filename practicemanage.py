import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
import json
import os

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Library Management System")
        self.geometry("400x400")

        self.current_page = None
        self.show_login_page()

    def show_login_page(self):
        self.clear_window()
        LoginPage(self)

    def show_signup_page(self):
        self.clear_window()
        SignupPage(self)

    def show_forget_password_page(self):
        self.clear_window()
        ForgetPasswordPage(self)

    def show_main_page(self):
        self.clear_window()
        MainPage(self)

    def clear_window(self):
        for widget in self.winfo_children():
            widget.destroy()

class LoginPage:
    def __init__(self, master):
        self.master = master

        self.frame = ctk.CTkFrame(master)
        self.frame.pack(pady=20, padx=20, fill="both", expand=True)

        self.label = ctk.CTkLabel(self.frame, text="Login to Library System")
        self.label.pack(pady=12, padx=10)

        self.username_entry = ctk.CTkEntry(self.frame, placeholder_text="Username")
        self.username_entry.pack(pady=12, padx=10)

        self.password_entry = ctk.CTkEntry(self.frame, placeholder_text="Password", show="*")
        self.password_entry.pack(pady=12, padx=10)

        self.login_button = ctk.CTkButton(self.frame, text="Login", command=self.login)
        self.login_button.pack(pady=12, padx=10)

        self.signup_button = ctk.CTkButton(self.frame, text="Sign Up", command=self.master.show_signup_page)
        self.signup_button.pack(pady=12, padx=10)

        self.forget_password_button = ctk.CTkButton(self.frame, text="Forget Password", command=self.master.show_forget_password_page)
        self.forget_password_button.pack(pady=12, padx=10)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if self.check_credentials(username, password):
            messagebox.showinfo("Success", "Login successful!")
            self.master.show_main_page()
        else:
            messagebox.showerror("Error", "Invalid username or password")

    def check_credentials(self, username, password):
        if os.path.exists("users.json"):
            with open("users.json", "r") as f:
                users = json.load(f)
                if username in users and users[username]["password"] == password:
                    return True
        return False

class SignupPage:
    def __init__(self, master):
        self.master = master

        self.frame = ctk.CTkFrame(master)
        self.frame.pack(pady=20, padx=20, fill="both", expand=True)

        self.label = ctk.CTkLabel(self.frame, text="Sign Up for Library System")
        self.label.pack(pady=12, padx=10)

        self.username_entry = ctk.CTkEntry(self.frame, placeholder_text="Username")
        self.username_entry.pack(pady=12, padx=10)

        self.password_entry = ctk.CTkEntry(self.frame, placeholder_text="Password", show="*")
        self.password_entry.pack(pady=12, padx=10)

        self.security_question_entry = ctk.CTkEntry(self.frame, placeholder_text="Security Question")
        self.security_question_entry.pack(pady=12, padx=10)

        self.security_answer_entry = ctk.CTkEntry(self.frame, placeholder_text="Security Answer")
        self.security_answer_entry.pack(pady=12, padx=10)

        self.signup_button = ctk.CTkButton(self.frame, text="Sign Up", command=self.signup)
        self.signup_button.pack(pady=12, padx=10)

        self.back_button = ctk.CTkButton(self.frame, text="Back to Login", command=self.master.show_login_page)
        self.back_button.pack(pady=12, padx=10)

    def signup(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        security_question = self.security_question_entry.get()
        security_answer = self.security_answer_entry.get()

        if username and password and security_question and security_answer:
            if self.save_user(username, password, security_question, security_answer):
                messagebox.showinfo("Success", "Account created successfully!")
                self.master.show_login_page()
            else:
                messagebox.showerror("Error", "Username already exists")
        else:
            messagebox.showerror("Error", "Please fill in all fields")

    def save_user(self, username, password, security_question, security_answer):
        users = {}
        if os.path.exists("users.json"):
            with open("users.json", "r") as f:
                users = json.load(f)

        if username in users:
            return False

        users[username] = {
            "password": password,
            "security_question": security_question,
            "security_answer": security_answer
        }

        with open("users.json", "w") as f:
            json.dump(users, f)

        return True

class ForgetPasswordPage:
    def __init__(self, master):
        self.master = master

        self.frame = ctk.CTkFrame(master)
        self.frame.pack(pady=20, padx=20, fill="both", expand=True)

        self.label = ctk.CTkLabel(self.frame, text="Forget Password")
        self.label.pack(pady=12, padx=10)

        # Username Entry
        self.username_entry = ctk.CTkEntry(self.frame, placeholder_text="Username")
        self.username_entry.pack(pady=12, padx=10)

        # Check Username Button
        self.check_button = ctk.CTkButton(self.frame, text="Check Username", command=self.check_username)
        self.check_button.pack(pady=12, padx=10)

        # Security Question Label
        self.security_question_label = ctk.CTkLabel(self.frame, text="")
        self.security_question_label.pack(pady=12, padx=10)

        # Security Answer Entry
        self.security_answer_entry = ctk.CTkEntry(self.frame, placeholder_text="Security Answer")
        self.security_answer_entry.pack(pady=12, padx=10)

        # Verify Answer Button
        self.verify_button = ctk.CTkButton(self.frame, text="Verify Answer", command=self.verify_answer)
        self.verify_button.pack(pady=12, padx=10)

        # Back to Login Button
        self.back_button = ctk.CTkButton(self.frame, text="Back to Login", command=self.master.show_login_page)
        self.back_button.pack(pady=12, padx=10)

        # Store user data temporarily
        self.user_data = None

    def check_username(self):
        username = self.username_entry.get()
        if os.path.exists("users.json"):
            with open("users.json", "r") as f:
                users = json.load(f)
                if username in users:
                    self.user_data = users[username]
                    self.security_question_label.configure(text=f"Security Question: {self.user_data['security_question']}")
                    return
        messagebox.showerror("Error", "Username not found")

    def verify_answer(self):
        if not self.user_data:
            messagebox.showerror("Error", "Please check username first")
            return

        answer = self.security_answer_entry.get()
        if answer == self.user_data["security_answer"]:
            # Close the current forget password window
            self.master.withdraw()  # Hide the current window
            self.open_reset_password_window()
        else:
            messagebox.showerror("Error", "Incorrect security answer")

    def open_reset_password_window(self):
        # Create a new top-level window
        reset_window = ctk.CTkToplevel(self.master)
        reset_window.title("Reset Password")
        reset_window.geometry("400x300")

        # New Password Frame
        new_password_frame = ctk.CTkFrame(reset_window)
        new_password_frame.pack(pady=20, padx=20, fill="both", expand=True)

        # New Password Entry
        self.new_password_entry = ctk.CTkEntry(new_password_frame, placeholder_text="New Password", show="*")
        self.new_password_entry.pack(pady=12, padx=10)

        # Show/Hide Password Button
        self.show_password_button = ctk.CTkButton(new_password_frame, text="Show", width=60, command=lambda: self.toggle_password_visibility(self.new_password_entry, self.show_password_button))
        self.show_password_button.pack(pady=12, padx=10)

        # Confirm Password Entry
        self.confirm_password_entry = ctk.CTkEntry(new_password_frame, placeholder_text="Confirm New Password", show="*")
        self.confirm_password_entry.pack(pady=12, padx=10)

        # Show/Hide Confirm Password Button
        self.show_confirm_password_button = ctk.CTkButton(new_password_frame, text="Show", width=60, command=lambda: self.toggle_password_visibility(self.confirm_password_entry, self.show_confirm_password_button))
        self.show_confirm_password_button.pack(pady=12, padx=10)

        # Reset Password Button
        reset_button = ctk.CTkButton(new_password_frame, text="Reset Password", command=lambda: self.reset_password(reset_window))
        reset_button.pack(pady=12, padx=10)

    def toggle_password_visibility(self, entry_widget, button_widget):
        if entry_widget.cget("show") == "":
            entry_widget.configure(show="*")
            button_widget.configure(text="Show")
        else:
            entry_widget.configure(show="")
            button_widget.configure(text="Hide")

    def reset_password(self, reset_window):
        new_password = self.new_password_entry.get()
        confirm_password = self.confirm_password_entry.get()

        if new_password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match")
            return

        if len(new_password) < 6:
            messagebox.showerror("Error", "Password must be at least 6 characters long")
            return

        self.update_password(self.username_entry.get(), new_password)
        messagebox.showinfo("Success", "Password has been reset successfully")
        reset_window.destroy()  # Close the reset password window
        self.master.show_homepage()  # Redirect to homepage

    def update_password(self, username, new_password):
        with open("users.json", "r") as f:
            users = json.load(f)
        
        users[username]["password"] = new_password

        with open("users.json", "w") as f:
            json.dump(users, f)

class MainPage:
    def __init__(self, master):
        self.master = master

        self.frame = ctk.CTkFrame(master)
        self.frame.pack(pady=20, padx=20, fill="both", expand=True)

        self.label = ctk.CTkLabel(self.frame, text="Library Management System")
        self.label.pack(pady=12, padx=10)

        self.add_book_button = ctk.CTkButton(self.frame, text="Add Book", command=self.add_book)
        self.add_book_button.pack(pady=12, padx=10)

        self.view_books_button = ctk.CTkButton(self.frame, text="View Books", command=self.view_books)
        self.view_books_button.pack(pady=12, padx=10)

        self.issue_book_button = ctk.CTkButton(self.frame, text="Issue Book", command=self.issue_book)
        self.issue_book_button.pack(pady=12, padx=10)

        self.return_book_button = ctk.CTkButton(self.frame, text="Return Book", command=self.return_book)
        self.return_book_button.pack(pady=12, padx=10)

        self.logout_button = ctk.CTkButton(self.frame, text="Logout", command=self.master.show_login_page)
        self.logout_button.pack(pady=12, padx=10)

    def add_book(self):
        messagebox.showinfo("Info", "Add Book functionality to be implemented")

    def view_books(self):
        messagebox.showinfo("Info", "View Books functionality to be implemented")

    def issue_book(self):
        messagebox.showinfo("Info", "Issue Book functionality to be implemented")

    def return_book(self):
        messagebox.showinfo("Info", "Return Book functionality to be implemented")

if __name__ == "__main__":
    app = App()
    app.mainloop()

