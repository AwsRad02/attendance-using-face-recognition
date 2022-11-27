import tkinter
from PIL import Image, ImageTk
import cv2
import os
import pyrebase
from main2 import attendance
from tkinter import messagebox
import numpy as np
from rescaleFactor import Factor
#import smtplib, ssl
from firebase_admin import storage as strg

import face_recognition
import requests






cascPath=os.path.dirname(cv2.__file__)+"/data/haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)
"""
findencodings = findEncodingsImage()
classNames = findencodings.get_classNames()
encodeListKnown = findencodings.get_encoded()
"""



class Gui :


    #creatimg global variable to use inside the class


    #to initilize the UI when calling the class
    def __init__(self):
        #declare empty list to append attendance
        self.attendanceList = []



        self.cap = cv2.VideoCapture(0)
        #setting the video resulotion
        self.cap.set(3,1080)        # the width
        self.cap.set(4,720)         #the height


        #creating instance of tkinter
        self.pro=tkinter.Tk()

        #adjust the size of the window by getting the height and width
        width, height = self.pro.winfo_screenwidth(), self.pro.winfo_screenheight()

        self.pro.geometry( f'{width}x{height}')
        #open in full screen mode
        self.pro.attributes('-fullscreen', True)

        #self.pro.eval('tk::PlaceWindow . center')

        #setting the background color of the window
        self.pro["bg"] = "#1C2833"
        self.pro.title("Yu Attendance ")
        self.pro.resizable(False, False)

        #defining the variables types
        self.sectionName =tkinter.StringVar()
        self.sectionId =tkinter.StringVar()
        self.sectionNumber = tkinter.StringVar()
        self.studentId = tkinter.IntVar()

        #the start label in the window
        tkinter.Label(self.pro, width="300", text="Start", bg="#0E6655",
              fg="white", font=("Arial", 15, "bold")).pack()
        # ---------------------

        #creating the entries
        tkinter.Label(self.pro, text="section Name*", bg="#1C2833", fg="white",
              font=("Arial", 12, "bold")).place(x=20, y=55)

        tkinter.Entry(self.pro, textvariable=self.sectionName, bg="#1C2833", fg="white", width=12,
              highlightbackground="#0E6655",
              highlightcolor="#ffffff", highlightthickness=2, font=("Arial", 12, "bold")).place(x=155, y=55)

        # _---------------

        tkinter.Label(self.pro, text="section Id*", bg="#1C2833", fg="white",
              font=("Arial", 12, "bold")).place(x=20, y=105)

        tkinter.Entry(self.pro, textvariable=self.sectionId, bg="#1C2833", fg="white", width=12,
              highlightbackground="#0E6655",
              highlightcolor="#ffffff", highlightthickness=2, font=("Arial", 12, "bold")).place(x=155, y=105)
        # --------------------
        tkinter.Label(self.pro, text="section Number*", bg="#1C2833", fg="white",
              font=("Arial", 12, "bold")).place(x=20, y=155)

        tkinter.Entry(self.pro, textvariable=self.sectionNumber, bg="#1C2833", fg="white", width=12,
              highlightbackground="#0E6655",
              highlightcolor="#ffffff", highlightthickness=2, font=("Arial", 12, "bold")).place(x=155, y=155)

        # ______________

        tkinter.Button(self.pro, text="Start", width=24, height=1, bg="#0E6655", fg="white",
               font=("Arial", 12, "bold"),command=lambda : self.show_frames()).place(x=20, y=205)

        tkinter.Button(self.pro, text="Quit", width=24, height=1, bg="red", fg="white",
               font=("Arial", 12, "bold"),command=lambda : self.quit()).place(x=20, y=255)


        #creating entries for the check std absence

        tkinter.Label(self.pro, text="check student Absence ", bg="#1C2833", fg="white",
              font=("Arial", 12, "bold")).place(x=20, y=350)

        # --------------------------------------------------

        tkinter.Label(self.pro, text="section Name", bg="#1C2833", fg="white",
              font=("Arial", 12, "bold")).place(x=20, y=430)

        tkinter.Entry(self.pro, textvariable=self.sectionName, bg="#1C2833", fg="white", width=12,
              highlightbackground="#0E6655",
              highlightcolor="#ffffff", highlightthickness=2, font=("Arial", 12, "bold")).place(x=155, y=430)

        # _---------------

        tkinter.Label(self.pro, text="section Id", bg="#1C2833", fg="white",
              font=("Arial", 12, "bold")).place(x=20, y=480)

        tkinter.Entry(self.pro, textvariable=self.sectionId, bg="#1C2833", fg="white", width=12,
              highlightbackground="#0E6655",
              highlightcolor="#ffffff", highlightthickness=2, font=("Arial", 12, "bold")).place(x=155, y=480)
        # --------------------
        tkinter.Label(self.pro, text="section Number", bg="#1C2833", fg="white",
              font=("Arial", 12, "bold")).place(x=20, y=530)

        tkinter.Entry(self.pro, textvariable=self.sectionNumber, bg="#1C2833", fg="white", width=12,
              highlightbackground="#0E6655",
              highlightcolor="#ffffff", highlightthickness=2, font=("Arial", 12, "bold")).place(x=155, y=530)

        # -----------------------------------------------------------

        tkinter.Label(self.pro, text="section Number", bg="#1C2833", fg="white",
              font=("Arial", 12, "bold")).place(x=20, y=580)

        tkinter.Entry(self.pro, textvariable=self.studentId, bg="#1C2833", fg="white", width=12,
              highlightbackground="#0E6655",
              highlightcolor="#ffffff", highlightthickness=2, font=("Arial", 12, "bold")).place(x=155, y=580)


        tkinter.Button(self.pro, text="Check", width=24, height=1, bg="#0E6655", fg="white",
               font=("Arial", 12, "bold"),command=lambda : self.msg()).place(x=20, y=630)


        #creating entries to download excel sheet if not exist

        tkinter.Label(self.pro, text="download file from database", bg="#1C2833", fg="white",
                      font=("Arial", 12, "bold")).place(x=1270, y=55)

        # --------------------------------------------------

        tkinter.Label(self.pro, text="section Name *", bg="#1C2833", fg="white",
                      font=("Arial", 12, "bold")).place(x=1270, y=105)

        tkinter.Entry(self.pro, textvariable=self.sectionName, bg="#1C2833", fg="white", width=12,
                      highlightbackground="#0E6655",
                      highlightcolor="#ffffff", highlightthickness=2, font=("Arial", 12, "bold")).place(x=1410, y=105)

        # _---------------

        tkinter.Label(self.pro, text="section Id *", bg="#1C2833", fg="white",
                      font=("Arial", 12, "bold")).place(x=1270, y=155)

        tkinter.Entry(self.pro, textvariable=self.sectionId, bg="#1C2833", fg="white", width=12,
                      highlightbackground="#0E6655",
                      highlightcolor="#ffffff", highlightthickness=2, font=("Arial", 12, "bold")).place(x=1410, y=155)
        # --------------------
        tkinter.Label(self.pro, text="section Number *", bg="#1C2833", fg="white",
                      font=("Arial", 12, "bold")).place(x=1270, y=205)

        tkinter.Entry(self.pro, textvariable=self.sectionNumber, bg="#1C2833", fg="white", width=12,
                      highlightbackground="#0E6655",
                      highlightcolor="#ffffff", highlightthickness=2, font=("Arial", 12, "bold")).place(x=1410, y=205)

        tkinter.Button(self.pro, text="Download", width=24, height=1, bg="#0E6655", fg="white",
                       font=("Arial", 12, "bold"), command=lambda: self.download()).place(x=1270, y=255)

        # -----------------------------------------------------------

        tkinter.Label(self.pro, text="section Number", bg="#1C2833", fg="white",
                      font=("Arial", 12, "bold")).place(x=20, y=580)

        tkinter.Entry(self.pro, textvariable=self.studentId, bg="#1C2833", fg="white", width=12,
                      highlightbackground="#0E6655",
                      highlightcolor="#ffffff", highlightthickness=2, font=("Arial", 12, "bold")).place(x=155, y=580)

        tkinter.Button(self.pro, text="Check", width=24, height=1, bg="#0E6655", fg="white",
                       font=("Arial", 12, "bold"), command=lambda: self.msg()).place(x=20, y=630)


        self.frame=tkinter.Frame(self.pro,width=940,height=720 ,bg="#ffffff")
        self.frame.place(x=300,y=55)



        self.pro.mainloop()

    def show_frames(self):

        label = tkinter.Label(self.frame, bg="#ffffff")
        label.place(x=0, y=0)
        #print('name:',self.sectionName,'id',self.sectionId,self.sectionNumber)
        if (self.sectionName.get()) =='' or (self.sectionId.get()) =='' or (self.sectionNumber.get()) =='':
            messagebox.showerror("info","please fill all boxs ")


        else:
            ret, frame = self.cap.read()
            if ret:

                # convert to PIL image
                frame=cv2.cvtColor(Factor().faceFrame(img=frame),cv2.COLOR_BGR2RGB)
                img = Image.fromarray(frame)

                # convert to Tkinter image
                photo = ImageTk.PhotoImage(image=img)
                # solution for bug in `PhotoImage`
                label.photo = photo

                # replace image in label
                label.configure(image=photo)

                # run again after 20ms (0.02s)
                label.after(20,self.show_frames)




    def msg(self):
        obj=attendance(self.sectionName.get(),self.sectionId.get(),self.sectionNumber.get())
        theAbsc=str(obj.check_stdabsence(self.studentId.get()))

        messagebox.showinfo("info",theAbsc)


    def quit(self):
        askQ=tkinter.messagebox.askyesno(title="confirmation",message="Are you sure that you want to quit?")
        #if yes retrun true , else return false
        if askQ:

            obj = attendance(self.sectionName.get(),self.sectionId.get(),self.sectionNumber.get())
            self.pro.destroy()
            classNames=Factor().getClassNames()
            attendancenames=Factor().getAttendance()
            print("G atte",attendancenames)
            print("G class name ", classNames)
            for i in classNames:
                if i not in attendancenames:
                    obj.mark_attend(int(i))
        else:
            pass



    def download(self):
        firebaseConfig = {
            "use your own config"
        }


        firebase = pyrebase.initialize_app(firebaseConfig)
        storage = firebase.storage()

        if (self.sectionName.get()) =='' or (self.sectionId.get()) =='' or (self.sectionNumber.get()) =='':
            messagebox.showerror("error","please fill all boxs ")

        else:
            # Whether the file exists or not on the server

            try :
                    path_on_cloud = "sheets/" + str(self.sectionName.get()) + str(self.sectionId.get()) + str(
                    self.sectionNumber.get()) + ".xlsx"

                    storage.child(path_on_cloud).download(str(self.sectionName.get() + self.sectionId.get() + self.sectionNumber.get() + ".xlsx"))
                    messagebox.showinfo("info", "Downloaded successfully")
                    #url=storage.child(path_on_cloud).get_url(None)


            except :

                    messagebox.showerror("error","file not found")











