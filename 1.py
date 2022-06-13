from tkinter import *

window = Tk()
window.title("Title")
window.geometry("500x500")
img = PhotoImage(file="./2.jpg")
l1=Label(window,
text="Hello World",
font=("Arial Bold",20,"underline"),
image=img,
)
l1.pack()

window.mainloop()