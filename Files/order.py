import os

from Tkinter import *
from tkMessageBox import *
root=Tk()

root.title("Order Finalize")
root.geometry('1366x768')


#===============Functions=============================================
'''def order():
     if men.check() + women.check() + indian.check() + chinese.check() + english.check() + thor.check() + golmaal.check() + fast.check() == 0:
        showerror('Error','No item is Booked')
     else:
         showinfo('Success','Order is Booked')
    
#def pay():
    if men.check() + women.check() + indian.check() + chinese.check() + english.check() + thor.check() + golmaal.check() + fast.check() == 0:
        showerror('Error','No item is Booked')
    else:
        showinfo('Success','Transaction is Completed. Thank You. Visit Again! :)')

#===============Labels and Buttons================================

Label(root,text="Order Finalize",font="times 30 bold",bg="green",).grid(row=0,column=0,columnspan=4,sticky='W')
#def a():
     if men.check() != 0:
         Label(root,text="Total amount of Men Shopping:",font="times 20 bold").grid(row=1,column=0,columnspan=1)
         Label(root,text=men.check,font="times 20 bold").grid(row=1,column=1)
     else:
         Label(root,text=" ").grid()

     if women.check() != 0:    
         Label(root,text="Total amount of Women Shopping:",font="times 20 bold").grid(row=3,column=0,columnspan=1)
         Label(root,text=women.check,font="times 20 bold").grid(row=3,column=1)
     else:
         Label(root,text=" ").grid()

     if chinese.check() != 0:
         Label(root,text="Total amount of Cinema Shopping:",font="times 20 bold").grid(row=5,column=0,columnspan=1)
         Label(root,text=chinese.check,font="times 20 bold").grid(row=5,column=1)
     else:
         Label(root,text=" ").grid()

     if indian.check() != 0:
         Label(root,text="Total amount of Cinema Shopping:",font="times 20 bold").grid(row=5,column=0,columnspan=1)
         Label(root,text=indian.check,font="times 20 bold").grid(row=5,column=1)
     else:
         Label(root,text=" ").grid()

if english.check() != 0:
    Label(root,text="Total amount of Cinema Shopping:",font="times 20 bold").grid(row=5,column=0,columnspan=1)
    Label(root,text=english.check,font="times 20 bold").grid(row=5,column=1)
else:
    Label(root,text=" ").grid()
    
if thor.check() != 0:
    Label(root,text="Total amount of Cinema Shopping:",font="times 20 bold").grid(row=5,column=0,columnspan=1)
    Label(root,text=thor.check,font="times 20 bold").grid(row=5,column=1)
else:
    Label(root,text=" ").grid()
    
if golmaal.check() != 0:
    Label(root,text="Total amount of Cinema Shopping:",font="times 20 bold").grid(row=5,column=0,columnspan=1)
    Label(root,text=golmaal.check,font="times 20 bold").grid(row=5,column=1)
else:
    Label(root,text=" ").grid()

if fast.check() != 0:
    Label(root,text="Total amount of Cinema Shopping:",font="times 20 bold").grid(row=5,column=0,columnspan=1)
    Label(root,text=fast.check,font="times 20 bold").grid(row=5,column=1)
else:
    Label(root,text=" ").grid()
'''
    
Button(root,text="1.Click Here For Finalize the Order",font="times 20 bold",relief=SUNKEN,bg="black",fg="white",).grid(row=6,column=1)

Button(root,text="2.Click Here For Payment",font="times 20 bold",relief=SUNKEN,bg="black",fg="white",).grid(row=7,column=0,sticky='W',padx=60,pady=30)


root.mainloop()
