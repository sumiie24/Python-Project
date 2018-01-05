import os
from Tkinter import *
root=Tk()
root.title("Cinema")
root.geometry('1367x768')
root.configure(background='Tan')

#===============Functions=============================================
def thor():
    os.startfile("thor.py")
    root.quit()

def golmaal():
    os.startfile("golmaal.py")
    root.quit()

def fast():
    os.startfile("fast.py")
    root.quit()
    
def back():
    os.startfile("Project.py")
    root.quit()


#===============Labels and Buttons================================
Label(root,text="CINEMA",font="Georgia 30 bold",bg="Purple",fg="MistyRose",width=50,bd=20).grid(row=0,column=0)
Label(root,text="Trending Movies",font="cambria 25 bold",bg="tomato").grid(row=1,column=0,pady=30)
Label(root,text="Click on Movie which you want to watch:-",font="cambria 20 bold",bg="lightblue").grid(row=2,column=0,sticky=W,pady=10)

Button(root,text="1.Thor",font="cambria 20 bold",relief=SUNKEN,bd=10,bg="Orange",fg="Navy",command=thor).grid(row=3,column=0,columnspan=1,sticky='W',padx=60,pady=10)
Button(root,text="2.Golmaal Again",font="cambria 20 bold",relief=SUNKEN,bd=10,bg="Orange",fg="Navy",command=golmaal).grid(row=4,column=0,columnspan=1,sticky='W',padx=60,pady=10)
Button(root,text="3.Fast and Furious 9",font="cambria 20 bold",relief=SUNKEN,bg="Orange",fg="Navy",bd=10,command=fast).grid(row=5,column=0,columnspan=1,sticky='W',padx=60,pady=10)


Button(root,text="Back",font="times 20 bold",relief=SUNKEN,bg="black",fg="white",command=back,bd=10).grid(row=6,column=0,sticky='W',padx=60,pady=30)

root.mainloop()
