import os
import sqlite3
from Tkinter import *
from tkMessageBox import*

con=sqlite3.Connection("DataBase")
cur=con.cursor()

root=Tk()
root.title("Signin")
root.geometry('1367x768')
root.configure(background='Lavender')

#===============Functions=============================================

def back():
    os.startfile("Project.py")
    root.quit()

def show():
    x=[a.get()]
    cur.execute('select * from sumex where username=(?)',x)
    z=cur.fetchall()
    pasw = b.get()
    if z[0][7] == pasw:
        showinfo("Account Information",z)
        a.delete(0,END)
        b.delete(0,END)
    else:
        showinfo("Error","Username or Password is Incorrect")
        a.delete(0,END)
        b.delete(0,END)
#===============Labels and Buttons================================
Label(root,text="Signin to your SumexPlaza Account",font="Georgia 30 bold",bg="Maroon",fg="Orange").grid(row=0,column=1,sticky=W,columnspan=2)


Label(root,text ='Username',font="times 20 bold",bg="Khaki",fg="DarkMagenta").grid(row=1,column=0,padx=90,pady=30)
a=Entry(root)
a.grid(row=1,column=1)
print a
Label(root,text ='Password',font="times 20 bold",bg="Khaki",fg="DarkMagenta").grid(row=2,column=0,padx=90,pady=30)
b=Entry(root)
b.grid(row=2,column=1)

Button(root,text='Submit',font="times 20 bold",relief=SUNKEN,bg="DarkSlateBlue",fg="white",bd=10,command=show).grid(row=3,column=2,padx=30,pady=30)
Button(root,text="Back",font="times 20 bold",relief=SUNKEN,bg="DarkSlateBlue",fg="white",command=back,bd=10).grid(row=3,column=0,sticky='W',padx=90,pady=30)


root.mainloop()
