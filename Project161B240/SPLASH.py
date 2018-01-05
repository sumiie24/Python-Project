import os
from Tkinter import *
root=Tk()
root.title("Splash Screen")
root.geometry('1367x768')
root.configure(background='black')

#===============Functions=============================================

def fun():
     os.startfile("details.py")
     root.destroy()
         
#===============Labels and Buttons================================

a=PhotoImage(file="logob.gif")
lb=Label(root,image=a)

lb.after(5000,fun)
lb.grid(row=5,column=1,padx=450,pady=250)

root.mainloop()
