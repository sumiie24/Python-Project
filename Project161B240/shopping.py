import os
from Tkinter import *
root=Tk()
root.title("Shopping")
root.geometry('1367x768')
root.configure(background='Salmon')

#===============Functions=============================================

def men():
    os.startfile("men.py")
    root.quit()
    
def women():
    os.startfile("women.py")
    root.quit()

def back():
    os.startfile("Project.py")
    root.quit()

#===============Labels and Buttons================================

Label(root,text="|| SHOPPING  ||",font="Georgia 30 bold",bg="khaki",fg="Indigo",width=50,bd=20).grid(row=0,column=0)
Label(root,text="Who You Are?",font="cambria 25 bold",relief=SUNKEN,bg="lightblue").grid(row=1,column=0,pady=40)

Button(root,text="Men",font="cambria 20 bold",relief=SUNKEN,bd=10,command=men,bg="LightGreen").grid(row=2,column=0,sticky='W',padx=60,pady=30)
Button(root,text="Women",font="cambria 20 bold",relief=SUNKEN,bd=10,command=women,bg="LightGreen").grid(row=3,column=0,sticky='W',padx=60,pady=30)

Button(root,text="Back",font="cambria 20 bold",relief=SUNKEN,bd=10,bg="black",fg="white",command=back).grid(row=6,column=0,sticky='W',padx=60,pady=30)

root.mainloop()
