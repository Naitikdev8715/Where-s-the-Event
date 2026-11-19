from tkinter import *

root = Tk()
root.title("Event Handler")
root.geometry("100x100")

def handle_keypressed(event):
    print(event.char)
root.bind("<Key>", handle_keypressed)

def handle_clicked(event):
    print("\n The button was clicked!")
button1 = Button(text= "click Me!")

button1.pack()
button1.bind("<Button-1>", handle_clicked)

root.mainloop()