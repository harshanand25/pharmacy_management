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

        self.btnRegistration = Button(self.frame,text = "Patient's Registration",command=self.Registration_window)
        self.btnRegistration.grid(row=0,column=0)

        self.btnHospital = Button(self.frame, text="Hospital Management", command=self.Registration_window)
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
