import customtkinter as ctk

# Create the main window
root = ctk.CTk()
root.title("User and Librarian Buttons")
root.geometry("400x300")  # Adjust window size as needed

# Create a frame to hold the buttons and center them
frame = ctk.CTkFrame(root)
frame.pack(expand=True)  # Makes sure the frame expands and centers the content

# Create the "User" button
user_button = ctk.CTkButton(frame, text="User", width=200, height=50, 
                            font=("Arial", 16, "bold"), corner_radius=10, 
                            fg_color="#4CAF50", hover_color="#45a049")
user_button.grid(row=0, pady=20)  # Grid with vertical padding for spacing

# Create the "Librarian" button
librarian_button = ctk.CTkButton(frame, text="Librarian", width=200, height=50, 
                                 font=("Arial", 16, "bold"), corner_radius=10, 
                                 fg_color="#2196F3", hover_color="#1976D2")
librarian_button.grid(row=1)  # Placing the second button below the first one

# Run the application
root.mainloop()
