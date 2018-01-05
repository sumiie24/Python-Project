import os
import sqlite3
from Tkinter import *
from tkMessageBox import*

con=sqlite3.Connection("DataBase")
cur=con.cursor()

cur.execute("create table if not exists sumex(fname varchar(20),lname varchar(20),gender varchar(10),username varchar(20) primary key,emailadd varchar(40),mobile_no number, pass varchar(10),cpass varchar(10),dob varchar(10),loc varchar(20))")

root=Tk()
root.title("Sign Up")
root.geometry('1367x768')
root.configure(background='Lavender')

w=IntVar()

#===============Functions=============================================
def insert():
    us=[d.get()]
    cur.execute('select * from sumex where username=(?)',us)
    sh=cur.fetchall()
    if len(sh)>0:
        showerror('error','already exists')
    else:
        x=[(a.get(),b.get(),c.get(),d.get(),e.get(),f.get(),g.get(),h.get(),i.get(),j.get())]
        cur.executemany('insert into sumex values(?,?,?,?,?,?,?,?,?,?)',x)
        con.commit()
        showinfo("Success","Account Created")
        a.delete(0,END)
        b.delete(0,END)
        c.delete(0,END)
        d.delete(0,END)
        e.delete(0,END)
        f.delete(0,END)
        g.delete(0,END)
        h.delete(0,END)
        i.delete(0,END)
        j.delete(0,END)
    
def show():
    x=[d.get()]
    cur.execute('select * from sumex where username=(?)',x)
    z=cur.fetchall()
    showinfo("Account Information",z)
  
def showall():
    cur.execute('select * from sumex')
    y=cur.fetchall()
    showinfo("All Accounts Information",y)

def back():
    os.startfile("Project.py")
    root.quit()

def passw():
     if g.get() == h.get():
        check()
     else:
        showerror('Error','Password not matched')

def check():
     if(a.get()=='' or b.get()==''  or c.get()==''  or d.get()==''  or g.get()==''  or h.get()=='' ):
        showerror('Error','Field empty')
     else:
        insert()
        
#===============Labels and Buttons================================
Label(root,text="Create your SumexPlaza Account",font="Georgia 30 bold",bg="Maroon",fg="Orange").grid(row=0,column=0,sticky=W,columnspan=2)

Label(root,text ='*First Name:',font="times 15 bold",relief=SUNKEN,bg="Khaki",fg="DarkMagenta").grid(row=1,column=0,padx=90,pady=15,sticky=W)
a=Entry(root)
a.grid(row=1,column=1,sticky=W)

Label(root,text ='*Last Name',font="times 15 bold",relief=SUNKEN,bg="Khaki",fg="DarkMagenta").grid(row=2,column=0,padx=90,pady=10,sticky=W)
b=Entry(root)
b.grid(row=2,column=1,sticky=W)

Label(root,text ='*Gender',font="times 15 bold",relief=SUNKEN,bg="Khaki",fg="DarkMagenta").grid(row=3,column=0,padx=90,pady=10,sticky=W)
c=Entry(root)
c.grid(row=3,column=1,pady=10,sticky=W)

Label(root,text ='*Choose Username',font="times 15 bold",relief=SUNKEN,bg="Khaki",fg="DarkMagenta").grid(row=4,column=0,padx=90,pady=10,sticky=W)
d=Entry(root)
d.grid(row=4,column=1,pady=10,sticky=W)

Label(root,text ='Email Address',font="times 15 bold",relief=SUNKEN,bg="Khaki",fg="DarkMagenta").grid(row=5,column=0,padx=90,pady=10,sticky=W)
e=Entry(root)
e.grid(row=5,column=1,pady=10,sticky=W)

Label(root,text ='Mobile No.',font="times 15 bold",relief=SUNKEN,bg="Khaki",fg="DarkMagenta").grid(row=6,column=0,padx=90,pady=10,sticky=W)
f=Entry(root)
f.grid(row=6,column=1,pady=10,sticky=W)

Label(root,text ='*Choose Password',font="times 15 bold",relief=SUNKEN,bg="Khaki",fg="DarkMagenta").grid(row=7,column=0,padx=90,pady=10,sticky=W)
g=Entry(root)
g.grid(row=7,column=1,pady=10,sticky=W)

Label(root,text ='*Confirm Password',font="times 15 bold",relief=SUNKEN,bg="Khaki",fg="DarkMagenta").grid(row=8,column=0,padx=90,pady=10,sticky=W)
h=Entry(root)
h.grid(row=8,column=1,pady=10,sticky=W)

Label(root,text ='Date of Birth',font="times 15 bold",relief=SUNKEN,bg="Khaki",fg="DarkMagenta").grid(row=9,column=0,padx=90,pady=10,sticky=W)
i=Entry(root)
i.grid(row=9,column=1,pady=10,sticky=W)

Label(root,text ='Location',font="times 15 bold",relief=SUNKEN,bg="Khaki",fg="DarkMagenta").grid(row=10,column=0,padx=90,pady=20,sticky=W)
j=Entry(root,)
j.grid(row=10,column=1,pady=10,sticky=W)

Label(root,text =' asterik(*) fields must not be empty! ',font="cambria 15 bold",bg="red").grid(row=6,column=2,padx=10,columnspan=5)


Button(root,text='Submit',font="times 20 bold",relief=SUNKEN,bg="DarkSlateBlue",fg="white",bd=10,command=passw).grid(row=12,column=1,padx=30,)
Button(root,text='Show',font="times 20 bold",relief=SUNKEN,bg="DarkSlateBlue",fg="white",bd=10,command=show).grid(row=12,column=2,padx=30,)
Button(root,text='ShowAll',font="times 20 bold",relief=SUNKEN,bg="DarkSlateBlue",fg="white",bd=10,command=showall).grid(row=12,column=3,padx=30,)
Button(root,text="Back",font="times 20 bold",relief=SUNKEN,bg="black",fg="white",bd=10,command=back).grid(row=12,column=0,sticky='W',padx=90)


root.mainloop()
