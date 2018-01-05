import os
from Tkinter import *
root=Tk()
root.title("SUMEXPLAZA")
root.geometry('1500x1500')
root.configure(background='Thistle')

#=============Functions========================================

def shop():
    os.startfile("shopping.py")
    root.quit()
def rest():
    os.startfile("restaurant.py")
    root.quit()
def cin():
    os.startfile("cinema.py")
    root.quit()
def sin():
    os.startfile("signin.py")
    root.quit()
def sup():
    os.startfile("signup.py")
    root.quit()
def back():
    os.startfile("details.py")
    root.quit()
    

#============Labels And Buttons====================
Label(root,text="||  WELCOME           To       SUMEXPLAZA  ||",font="Georgia 30 bold",relief=FLAT,bg="Cyan",fg="black",width=50).grid(row=0,column=0,columnspan=3)
Label(root,text="Where You Want to Go?",font="cambria 25 bold",relief=FLAT,bg="red",fg="black").grid(row=1,column=1,pady=40)

Button(root,text="Shopping",font="cambria 20 bold",relief=SUNKEN,bg="deepPink",fg="black",command=shop,bd=10).grid(row=2,column=0,sticky='W',padx=60,pady=20)
Button(root,text="Restaurant",font="cambria 20 bold",relief=SUNKEN,bg="deepPink",fg="black",command=rest,bd=10).grid(row=3,column=0,sticky='W',padx=60,pady=20)
Button(root,text="Cinema",font="cambria 20 bold",relief=SUNKEN,bg="deepPink",fg="black",command=cin,bd=10).grid(row=4,column=0,sticky='W',padx=60,pady=20)

Button(root,text="Sign Up(New to SumexPlaza)",font="candara 13 bold",relief=SUNKEN,bg="yellow",command=sup,bd=10).grid(row=2,column=2,sticky='W')
Button(root,text="Sign In(Already having an Account)",font="candara 13 bold",relief=SUNKEN,bg="yellow",command=sin,bd=10).grid(row=3,column=2,sticky='W')

Button(root,text="Back",font="cambria 20 bold",relief=SUNKEN,bg="black",fg="white",command=back,bd=10).grid(row=5,column=0,sticky='W',padx=60,pady=40)


root.mainloop()
