from tkinter import *
from customtkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox

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


#Creating username entities

Login_usernameLabel = CTkLabel(master=loginView.tab("Login"), 
                         text = "Username:", text_color="black",
                         font=("Helvatica",20),
                         width = 30, height = 30,
                         )
Login_usernameLabel.place(relx = 0.12, rely = 0.06)

# Creating entry box for username:

Login_username = CTkEntry(master=loginView.tab("Login"),
                    border_color="black",
                    corner_radius=7,
                    placeholder_text="Enter your username",
                    fg_color="#ffffff",
                    text_color="black",
                    height = 40, width = 300)
Login_username.place(relx=0.12, rely=0.156)


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
                        height=40, width = 300)
login_button.place(x = 50, y = 200)

#Forgot password? label:

forgot_label = Label(master = loginView.tab("Login"),
                        text = "Forgot password?",
                        fg="black",
                        bg="#dfd8ee",
                        font = ("Calibri",20,"underline"))

forgot_label.place(x = 145, y = 340 )



##############################Create New##########################



######## Creating Username Label for Create New Account

Create_usernameLabel = CTkLabel(master=loginView.tab("Create New"), 
                         text = "Username:", text_color="black",
                         font=("Helvatica",20),
                         width = 30, height = 30,
                         )
Create_usernameLabel.place(relx = 0.12, rely = 0.06)


# Creating Entrybox of username for Create New Account:

Create_username = CTkEntry(master=loginView.tab("Create New"),
                    border_color="black",
                    corner_radius=7,
                    placeholder_text="Enter your username",
                    fg_color="#ffffff",
                    text_color="black",
                    height = 40, width = 300)
Create_username.place(relx=0.12, rely=0.156)


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

user_or_librarian = StringVar(value="")

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


##### Final Create Account Button #####

Create_button = CTkButton(master=loginView.tab("Create New"),
                        text = "Create Account",
                        font=("Calibri",20),
                        corner_radius=15,
                        fg_color="green",
                        height=40, width = 300, command= open_new_win_create)
Create_button.place(x = 50, y = 260)

win.mainloop()  # Make the window visible

