from tkinter import *
 
def addNumbers():
    res=int(e1.get())+int(e2.get())
    myText.set(res)
def subNumbers():
    res=int(e1.get())-int(e2.get())
    myText.set(res)
 
master = Tk()
myText=StringVar()
Label(master, text="First").grid(row=0, sticky=W)
Label(master, text="Second").grid(row=1, sticky=W)
Label(master, text="Result:").grid(row=3, sticky=W)
result=Label(master, text="", textvariable=myText).grid(row=3,column=1, sticky=W)
 
e1 = Entry(master)
e2 = Entry(master)
 
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
 
b = Button(master, text="SUM", command=addNumbers)
c = Button(master, text="SUB", command=subNumbers)
b.grid(row=0, column=2,columnspan=2, rowspan=2,sticky=W+E+N+S, padx=5, pady=5)
c.grid(row=2, column=2,columnspan=2, rowspan=2,sticky=W+E+N+S, padx=5, pady=5)
 
 
mainloop()