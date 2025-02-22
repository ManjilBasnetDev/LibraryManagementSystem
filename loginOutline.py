from tkinter import *
from customtkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
from tkcalendar import DateEntry

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

def checkLogin():
    if Login_password_Entry.get() == '' or Login_username_Entry.get() == '':
        messagebox.showerror("Invalid Credentials", "All fields are mandatory")
    else:
        pass


#Creating username entities

Login_usernameLabel = CTkLabel(master=loginView.tab("Login"), 
                         text = "Username:", text_color="black",
                         font=("Helvatica",20),
                         width = 30, height = 30,
                         )
Login_usernameLabel.place(relx = 0.12, rely = 0.06)

# Creating entry box for username:

Login_username_Entry = CTkEntry(master=loginView.tab("Login"),
                    border_color="black",
                    corner_radius=7,
                    placeholder_text="Enter your username",
                    fg_color="#ffffff",
                    text_color="black",
                    height = 40, width = 300)
Login_username_Entry.place(relx=0.12, rely=0.156)


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
                        height=40, width = 300,
                        command = checkLogin)
login_button.place(x = 50, y = 200)

### FORGOTTTTT FUNCTIONNNNN

def open_new_window_forgot(event):
    forgot_win = Toplevel()
    forgot_win.geometry("500x500+400+300")  # Width x Height + x_offset + y_offset
    forgot_win.title("Forgot Password Window")
    forgot_win.resizable(False, False)
    forgot_win.configure(bg="#dfd8ee")


    ### Security Questions Label for Function 

    question_Label = CTkLabel(master = forgot_win,
                                    text  = "Security Questions",
                                    text_color= "black",
                                    font = ("Arial Bold", 20)
                                    )
    question_Label.pack(pady = 15)

    dob_Label = CTkLabel(forgot_win, text = "Select your DOB:", text_color="black", font = ("Calibri", 18))
    dob_Label.place(relx = 0.07, rely= 0.15)

    dob_select = DateEntry(forgot_win, background = "#dfd8ee", foreground = "black",
                               borderwidth = 2,
                                font=("Arial", 11), 
                                width=20,
                               )
    dob_select.place(relx = 0.4, rely = 0.16)

    ####### Function to retrieve the date ######

    def get_date():
            dob = dob_select.get()
            got_date_Label = CTkLabel(forgot_win, text = (f"You selected : {dob}"),
                                      text_color="black",
                                      font = ("Calibri",15)
                                      )
            got_date_Label.place(x = 170, rely =0.25)

    ######## Select Date Button ########

    select_date_button = CTkButton(master = forgot_win,
                                        text = "Select",
                                        text_color="white",
                                        font = ("Arial ",15),
                                        width = 115,
                                        fg_color="green", command = get_date )
    select_date_button.place(relx = 0.07, rely= 0.25)

    school_Label = CTkLabel(forgot_win, text = "Your first school :", text_color="black", font = ("Calibri", 18))
    school_Label.place(relx = 0.07, rely= 0.4)

    school_Entry = CTkEntry(master=forgot_win,
                    border_color="black",
                    corner_radius=7,
                    placeholder_text="School Name",
                    fg_color="#ffffff",
                    text_color="black",
                    height = 30, width = 200)

    school_Entry.place(relx = 0.4, rely= 0.4)

    def get_school():
            school = school_Entry.get()

            school_show = CTkLabel(forgot_win, text = school,
                                      text_color="black",
                                      font = ("Calibri",15)
                                      )
            school_show.place(x = 170, rely =0.5)
            school_show.focus()

    select_school_button = CTkButton(master = forgot_win,
                                        text = "Select",
                                        text_color="white",
                                        font = ("Arial ",15),
                                        width = 115,
                                        fg_color="green", command = get_school)
    select_school_button.place(relx = 0.07, rely= 0.5)

    def check_qsn():
        def empty():
            empty_School = CTkLabel(forgot_win, text = "All fields are mandatory!", text_color="red")
            empty_School.place(relx =0.32, rely = 0.82)
            
        if school_Entry.get() is None:
            empty()
            
        else:
            pass
    
    submit_qsn_button = CTkButton(master=forgot_win, text="Submit",
                                    fg_color="green",
                                    text_color="white",
                                    command = check_qsn
                                )
    submit_qsn_button.place(relx = 0.32, rely = 0.7)

#### FORGOT LABELLLLLLLLL
forgot_label = Label(master = loginView.tab("Login"),
                        text = "Forgot password?",
                        fg="black",
                        bg="#dfd8ee",
                        font = ("Calibri",20,"underline"),
                        cursor="hand2")

forgot_label.place(x = 145, y = 340 )
forgot_label.bind("<Button-1>", open_new_window_forgot)  


##############################Create New##########################


######## Creating Username Label for Create New Account

Create_usernameLabel = CTkLabel(master=loginView.tab("Create New"), 
                         text = "Username:", text_color="black",
                         font=("Helvatica",20),
                         width = 30, height = 30,
                         )
Create_usernameLabel.place(relx = 0.12, rely = 0.06)


# Creating Entrybox of username for Create New Account:

Create_username_Entry = CTkEntry(master=loginView.tab("Create New"),
                    border_color="black",
                    corner_radius=7,
                    placeholder_text="Enter your username",
                    fg_color="#ffffff",
                    text_color="black",
                    height = 40, width = 300)
Create_username_Entry.place(relx=0.12, rely=0.156)


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

user_or_librarian = StringVar()

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
            Create_username_Entry.delete(0,END)
            Create_password_Entry.delete(0,END)
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


def checkRadio():
    if Create_password_Entry.get() == '' or Create_username_Entry.get() == '' or user_or_librarian.get() == '':
        messagebox.showerror("Invalid Credentials", "All fields are mandatory")
    elif user_or_librarian.get() == "2":
        open_new_win_create()
    elif user_or_librarian.get() == '1':
        Create_username_Entry.delete(0,END)
        Create_password_Entry.delete(0,END)
        messagebox.showinfo("User Account Created", "Done, Please Login")
    else:
        pass

##### Final Create Account Button #####

Create_button = CTkButton(master=loginView.tab("Create New"),
                        text = "Create Account",
                        font=("Calibri",20),
                        corner_radius=15,
                        fg_color="green",
                        height=40, width = 300, command= checkRadio)
Create_button.place(x = 50, y = 260)

win.mainloop()  # Make the window visible

