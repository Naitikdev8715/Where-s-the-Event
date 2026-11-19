from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("askquestion() function")
root.geometry("600x500")
label = Label(root, text= "Delete files", fg="black", bg="white")
label.pack()
def msg():
    messagebox.askquestion("Move to Recycle Bin", "Do you want to delete this file?")
button = Button(root, text = "Delete File", fg= "white", bg="dodgerblue", command=msg)
button.place(x=200, y=200)
root.mainloop()