import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
import sqlite3

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
        conn = sqlite3.connect("library_users.db")
        cursor = conn.cursor()
        
        cursor.execute("SELECT security_question, security_answer FROM users WHERE username = ?", (username,))
        result = cursor.fetchone()
        
        if result:
            self.user_data = {
                "security_question": result[0],
                "security_answer": result[1]
            }
            self.security_question_label.configure(text=f"Security Question: {self.user_data['security_question']}")
        else:
            messagebox.showerror("Error", "Username not found")
        
        conn.close()

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
        reset_window.lift()  # Bring the window to the front

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
        conn = sqlite3.connect("library_users.db")
        cursor = conn.cursor()
        
        cursor.execute("UPDATE users SET password = ? WHERE username = ?", (new_password, username))
        conn.commit()
        conn.close()