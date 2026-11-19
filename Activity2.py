from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Virus Detector")
root.geometry("200x200")

def msg():
    messagebox.showwarning("Alert", "Stop! Virus Detected!")
button1 = Button(root, text = "Scan for Virus", command= msg)
button1.place(x=40, y=80)
root.mainloop()