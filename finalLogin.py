from tkinter import *
from customtkinter import *
from PIL import Image, ImageTk

win = CTk()
win.iconbitmap("logo.png")
win.geometry("1920x1080")  # Set a smaller window size

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
loginView.add("User")
loginView.add("Librarian")
loginView.place(relx = 0.6, rely = 0.2)

# details = CTkLabel(master = loginView.tab("User"),
#                    text = "Enter your login details",
#                    text_color="#d74e3c",
#                    font = ("Georgia Bold",18))
# details.place(relx = 0.2, rely = 0.08)


#Creating username entities

usernameLabel = CTkLabel(master=loginView.tab("User"), 
                         text = "Username:", text_color="black",
                         font=("Helvatica",20),
                         width = 30, height = 30,
                         )
usernameLabel.place(relx = 0.12, rely = 0.06)

# Creating entry box for username:

username = CTkEntry(master=loginView.tab("User"),
                    border_color="black",
                    corner_radius=7,
                    placeholder_text="Enter your username",
                    fg_color="#ffffff",
                    text_color="black",
                    height = 40, width = 300)
username.place(relx=0.12, rely=0.156)

#to change border-color when clicked, (focus on):

# username.bind("<focusIn>")

#Creating password entities

passwordLabel = CTkLabel(master = loginView.tab("User"), 
                         text = "Password:", text_color="black",
                         font=("Helvatica",20),
                         width = 30, height = 30,
                         )
passwordLabel.place(relx = 0.12, rely = 0.3)

# Creating entry box for username:

password = CTkEntry(master=loginView.tab("User"),
                    corner_radius=7,
                    placeholder_text="Enter your password",
                    height = 40,
                    fg_color="#ffffff",
                    text_color="black",
                    width = 300)
password.place(relx=0.12, rely=0.4)

login_button = CTkButton(master=loginView.tab("User"),
                        text = "Log in",
                        font=("Calibri",20),
                        corner_radius=15,
                        fg_color="green",
                        height=40, width = 300)
login_button.place(x = 50, y = 200)

#Forgot password? label:

forgot_label = Label(loginView.tab("User"),
                        text = "Forgot password?",
                        fg="black",
                        bg="#dfd8ee",
                        height=50,
                        width = 30,
                        font = ("Calibri",10,"underline"))
# forgot_label.place(relx = 0.12, rely = 0.78)


forgot_label = CTkLabel(master=loginView.tab("User"),
                        text = "Forgot Password?",
                        fg_color = "blue",
                        bg_color = "#dfd8ee"
                        )



##############################librariannnn##########################


details= CTkLabel(master = loginView.tab("Librarian"),
                   text = "Enter your login details",
                   text_color="#d74e3c",
                   font = ("Georgia Bold",18))
details.place(relx = 0.2, rely = 0.08)



usernameLabel = CTkLabel(master=loginView.tab("Librarian"), 
                         text = "Username:", text_color="black",
                         font=("Helvatica",20),
                         width = 30, height = 30,
                         )
usernameLabel.place(relx = 0.12, rely = 0.2)

# Creating entry box for username:

username = CTkEntry(master=loginView.tab("Librarian"),
                    border_color="black",
                    corner_radius=7,
                    placeholder_text="Enter your username",
                    fg_color="#ffffff",
                    text_color="black",
                    height = 40, width = 250)
username.place(relx=0.12, rely=0.3)

#to change border-color when clicked, (focus on):

# username.bind("<focusIn>")

#Creating password entities

passwordLabel = CTkLabel(master = loginView.tab("Librarian"), 
                         text = "Password:", text_color="black",
                         font=("Helvatica",20),
                         width = 30, height = 30,
                         )
passwordLabel.place(relx = 0.12, rely = 0.45)

# Creating entry box for username:

password = CTkEntry(master=loginView.tab("Librarian"),
                    corner_radius=7,
                    placeholder_text="Enter your password",
                    height = 40,
                    fg_color="#ffffff",
                    text_color="black",
                    width = 250)
password.place(relx=0.12, rely=0.55)

login_button = CTkButton(master=loginView.tab("Librarian"),
                        text = "Log in",
                        font=("Calibri",20),
                        corner_radius=15,
                        fg_color="green",
                        height=30, width = 70)
login_button.place(relx=0.36,rely=0.8)

# logo = Image.open("logo.png")
# logo=logo.resize((50,50))
# logoF = ImageTk.PhotoImage(logo)

# logo_label = CTkLabel(master=outerFrame, image=logoF, text="")
# logo_label.place(relx = 0.91,rely=0.1)
# logo_label.lift()
## command = event()
win.mainloop()  # Make the window visible

