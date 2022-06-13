from tkinter import *
import tkinter.messagebox as messagebox
import mysql.connector as mysql

def insert():
    id=e_id.get()
    name=e_name.get()
    phone=e_phone.get()
    if id=='' or name=='' or phone=='':
        messagebox.showinfo("Insert Status","Please fill all the fields")
    else:
        conn=mysql.connect(host='localhost',user='root',passwd='',database='python')
        cursor=conn.cursor()
        cursor.execute("insert into student values('%s','%s','%s')"%(id,name,phone))
        conn.commit()
        e_id.delete(0,END)
        e_name.delete(0,END)
        e_phone.delete(0,END)
        messagebox.showinfo("Insert Status","Inserted Successfully")
        cursor.close()
        conn.close()
def delete():
    id=e_id.get()
    if id=='':
        messagebox.showinfo("Delete Status","Please fill all the fields")
    else:
        conn=mysql.connect(host='localhost',user='root',passwd='',database='python')
        cursor=conn.cursor()
        cursor.execute("delete from student where id='%s'"%id)
        conn.commit()
        e_id.delete(0,END)
        messagebox.showinfo("Delete Status","Deleted Successfully")
        cursor.close()
        conn.close()
def update():
    id=e_id.get()
    name=e_name.get()
    phone=e_phone.get()
    if id=='' or name=='' or phone=='':
        messagebox.showinfo("Update Status","Please fill all the fields")
    else:
        conn=mysql.connect(host='localhost',user='root',passwd='',database='python')
        cursor=conn.cursor()
        cursor.execute("update student set name='%s',phone='%s' where id='%s'"%(name,phone,id))
        conn.commit()
        e_id.delete(0,END)
        e_name.delete(0,END)
        e_phone.delete(0,END)
        messagebox.showinfo("Update Status","Updated Successfully")
        cursor.close()
        conn.close()
def get():
    id=e_id.get()
    if id=='':
        messagebox.showinfo("Get Status","Please fill all the fields")
    else:
        conn=mysql.connect(host='localhost',user='root',passwd='',database='python')
        cursor=conn.cursor()
        cursor.execute("select * from student where id='%s'"%id)
        rows=cursor.fetchall()

        for row in rows:
            e_name.insert(0,row[1])
            e_phone.insert(0,row[2])
        cursor.close()

root = Tk()
root.title('Database')
root.geometry('300x300')

id=Label(root,text='ID',font=('Bold',12))
id.place(x=20,y=30)

name = Label(root,text='Name',font=('Bold',12))
name.place(x=20,y=60)

phone = Label(root,text='Phone',font=('Bold',12))
phone.place(x=20,y=90)

e_id = Entry()
e_id.place(x=100,y=30)

e_name = Entry()
e_name.place(x=100,y=60)

e_phone = Entry()
e_phone.place(x=100,y=90)

insert = Button(root,text='Insert',command=insert)
insert.place(x=20,y=120)
update = Button(root,text='Update', command=update)
update.place(x=90,y=120)
delete = Button(root,text='Delete',command=delete)
delete.place(x=170,y=120)
get = Button(root,text='Get',command=get)
get.place(x=250,y=120)
root.mainloop()


