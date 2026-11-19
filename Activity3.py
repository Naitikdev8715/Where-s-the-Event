from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Other widgets in Messagebox module")
window.geometry("500x500")
label = Label(window, text= "Scan for virus in your system", fg="white", bg= "#3040ef")
label.pack()
def msg():
    messagebox.showinfo("Please Close this window to stop virus attack!")
button = Button(window, text= "Scan System", command =msg)

button.place(x=100, y=90)
window.mainloop()

#showinfo(), askokcancel(), askyesno(), askretrycancel()