from tkinter import *
import pyrebase

from finalGui import Gui

firebaseConfig = {
  "use your own firebase configurations  "
}

#initialize the firebase configration
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()






# defining login function
def login():
    # getting form data
    uname = username.get()
    pwd = password.get()
    # applying empty validation
    if uname == '' or pwd == '':
         message.set("fill the empty field!!!")

    else:
            try:
                user = auth.sign_in_with_email_and_password(uname,pwd)
                x.destroy()
                Gui()

            except:


                message.set("wrong password or email")


# defining loginform function
class LoginUI:
    def Loginform(self):
        global login_screen
        login_screen = Tk()
        # Setting title of screen
        login_screen.title("YU attendance ")
        # setting height and width of screen
        login_screen.geometry("600x400")
        login_screen["bg"] = "#1C2833"
        # declaring variable
        global message;
        global username
        global password
        username = StringVar()
        password = StringVar()
        message = StringVar()
        # Creating layout of login form
        Label(login_screen, width="300", text="Login", bg="#0E6655",
              fg="white", font=("Arial", 12, "bold")).pack()
        # Username Label
        Label(login_screen, text="Username * ", bg="#1C2833", fg="white",
              font=("Arial", 12, "bold")).place(x=70, y=90)
        # Username textbox
        Entry(login_screen, textvariable=username, bg="#1C2833", fg="white", width=25,
              highlightbackground="#0E6655",
              highlightcolor="#ffffff", highlightthickness=2, font=("Arial", 15, "bold")).place(x=200, y=90)
        # Password Label
        Label(login_screen, text="Password * ", bg="#1C2833", fg="white",
              font=("Arial", 12, "bold")).place(x=70, y=160)
        # Password textbox
        Entry(login_screen, textvariable=password, show="*", bg="#1C2833", width=25,
              highlightcolor="#ffffff", highlightthickness=2, highlightbackground="#0E6655",
              fg="white", font=("Arial", 15, "bold")).place(x=200, y=160)
        # Label for displaying login status[success/failed]
        Label(login_screen, text="", textvariable=message, bg="#1C2833", fg="white",
              font=("Arial", 12, "bold")).place(x=220, y=210)
        # Login button
        Button(login_screen, text="Login", width=10, height=1, command=login, bg="#0E6655", fg="white",
               font=("Arial", 12, "bold")).place(x=240, y=240)

        login_screen.mainloop()


    def destroy(self):
        login_screen.destroy()









# calling function Loginform
x = LoginUI()
x.Loginform()