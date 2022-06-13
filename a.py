from tkinter import *

window=Tk()
window.title("Welcome to app")
window.geometry('350x200')
def click():
    print("Welcome to app")
window.configure(background='green')
button1=Button(window,text="Click Me",height=5,width=20, command=click)
button2=Button(window,text="Click Me",height=5,width=20, command=click)
button1.grid(column=0,row=0)
button2.grid(column=1,row=0)
window.mainloop()