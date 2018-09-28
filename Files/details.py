import os
from Tkinter import *
root=Tk()
root.title("Project Details")
root.geometry('1367x768')
root.configure(background='grey')

#===============Functions=============================================

def click():
    os.startfile("Project.py")
    root.quit()
    
 
#===============Labels and Buttons================================
    
a=PhotoImage(file="details.gif")
lb=Label(root,image=a)

lb.pack()

Label(root,text="||  PYTHON PROJECT  ||",font="Georgia 30 bold",width=50,bg="HoneyDew",fg="DarkMagenta").place(x=0)

b=PhotoImage(file="sumit.gif")
lb=Label(root,image=b)
lb.place(x=100,y=150)

Label(root,text="Student Name:-",font="cambria 20 bold",relief=FLAT,bg="black",fg="white").place(x=400,y=160)
Label(root,text="Sumit Yadav",font="cambria 20 bold",relief=FLAT,bg="wheat",fg="MidnightBlue").place(x=700,y=160)


Label(root,text="Enrollment  No.:-",font="cambria 20 bold",relief=FLAT,bg="black",fg="white").place(x=400,y=235)
Label(root,text="161B240",font="cambria 20 bold",relief=FLAT,bg="wheat",fg="MidnightBlue").place(x=700,y=235)


Label(root,text="Batch:-",font="cambria 20 bold",relief=FLAT,bg="black",fg="white").place(x=400,y=310)
Label(root,text="CSE-B8(BZ)",font="cambria 20 bold",relief=FLAT,bg="wheat",fg="MidnightBlue").place(x=700,y=310)


Label(root,text="Project Title:-",font="cambria 20 bold",relief=FLAT,bg="black",fg="white").place(x=400,y=385)
Label(root,text="SUMEXPLAZA",font="cambria 20 bold",relief=FLAT,bg="wheat",fg="MidnightBlue").place(x=700,y=385)

Button(root,text="Click Me to See The Project",font="cambria 20 bold",relief=SUNKEN,bg="sienna",fg="yellow",bd=10,command=click).place(x=900,y=500)

root.mainloop()

