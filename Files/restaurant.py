import os
from Tkinter import *
root=Tk()
root.title("Restaurant")
root.geometry('1367x768')
root.configure(background='Thistle')

#===============Functions=============================================

def ind():
    os.startfile("indian.py")
    root.quit()

def chi():
    os.startfile("chinese.py")
    root.quit()

def eng():
    os.startfile("english.py")
    root.quit()

def back():
    os.startfile("Project.py")
    root.quit()


#===============Labels and Buttons================================

Label(root,text="||  RESTAURANTS  ||",font="Georgia 30 bold",bg="SeaGreen",fg="Gold",width=50,bd=20).grid(row=0,column=0)
Label(root,text="Select your Restaurant!",font="cambria 25 bold",bg="lightblue").grid(row=1,column=0,pady=30)

Button(root,text="Indian Restaurant",font="cambria 20 bold",bd=10,command=ind,bg="MediumOrchid",fg="Moccasin").grid(row=2,column=0,sticky='W',padx=60,pady=20)
Button(root,text="Chinese Restaurant",font="cambria 20 bold",bd=10,command=chi,bg="MediumOrchid",fg="Moccasin").grid(row=3,column=0,sticky='W',padx=60,pady=20)
Button(root,text="Western Restaurant",font="cambria 20 bold",bd=10,command=eng,bg="MediumOrchid",fg="Moccasin").grid(row=4,column=0,sticky='W',padx=60,pady=20)

Button(root,text="Back",font="times 20 bold",relief=SUNKEN,bg="black",fg="white",bd=10,command=back).grid(row=5,column=0,sticky='W',padx=60,pady=20)

root.mainloop()
