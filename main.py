from tkinter import *
import tkinter.messagebox
from tkinter import ttk
import random
import time
import datetime

def main():
    root = Tk()
    app = Window1(root)

class Window1:
    def __init__(self,master):
        self.master = master
        self.master.title("Pharmacy Management Systems")
        self.master.geometry('1350x750+0+0')
        self.frame = Frame(self.master)
        self.frame.pack()

        self.LabelTitile = Label(self.frame,text='Pharmacy Management System',font=('arial',50,'bold'),bd=20)
        self.LabelTitile.grid(row=0,column=0,columnspan=40,pady=40)

        self.LoginFrame = LabelFrame(self.frame,width=1010,height=600,font=('arial',20,'bold'),relief='ridge')
        self.LoginFrame.grid(row=1,column=0)

        self.LoginFrame2 = LabelFrame(self.frame, width=1010, height=600, font=('arial', 20, 'bold'), relief='ridge')
        self.LoginFrame2.grid(row=2, column=0)

        self.LoginFrame3 = LabelFrame(self.frame, width=1010, height=600, font=('arial', 20, 'bold'), relief='ridge')
        self.LoginFrame3.grid(row=3, column=0,pady=2)

        self.btnLogin = Button(self.LoginFrame2, text="Login",width=20,font=('arial',20,'bold'), command=self.Registration_window)
        self.btnLogin.grid(row=0, column=0)

        self.btnReset = Button(self.LoginFrame2, text="Reset",width=20,font=('arial',20,'bold'), command=self.Hospital_window)
        self.btnReset.grid(row=0, column=1)

        self.btnExit = Button(self.LoginFrame2, text="Exit", command=self.Hospital_window)
        self.btnExit.grid(row=0, column=2)

        self.btnRegistration = Button(self.frame,text = "Patient's Registration",command=self.Registration_window)
        self.btnRegistration.grid(row=0,column=0)

        self.btnHospital = Button(self.frame, text="Hospital Management", command=self.Hospital_window)
        self.btnHospital.grid(row=0, column=1)

    def Registration_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Window2(self.newWindow)

    def Hospital_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Window2(self.newWindow)

class Window2:
    def __init__(self,master):
        self.master = master
        self.master.title("Patient Registration Systems")
        self.master.geometry('1350x750+0+0')
        self.frame = Frame(self.master)
        self.frame.pack()

class Window3:
    def __init__(self,master):
        self.master = master
        self.master.title("Hospital Management Systems")
        self.master.geometry('1350x750+0+0')
        self.frame = Frame(self.master)
        self.frame.pack()



if __name__ == '__main__':
    main()
