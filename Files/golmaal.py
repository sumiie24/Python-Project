import os
from Tkinter import *
from tkMessageBox import *
root=Tk()
root.title("Golmaal Movie")
root.geometry('1367x768')
root.configure(background='plum')

v=IntVar()
v1=IntVar()
v2=IntVar()

#===============Functions=============================================
def check():
    if v2.get()== 0 or v1.get()== 0 or v.get()== 0:
         showerror('Error','Seats or Price or Time is Not Selected')
    else:
        Label(root,text="Rs.",font="times 20 bold").grid(row=12,column=1,sticky=W)
        Label(root,text=v2.get()*v.get(),font="times 20 bold").grid(row=12,column=1)

def book():
     if v2.get()== 0 or v1.get()== 0 or v.get()== 0:
         showerror('Error','Seats or Price or Time is Not Selected')
     else:
         showinfo('Success','Ticket is Booked')
    
def pay():
    if v2.get()== 0 or v1.get()== 0 or v.get()== 0:
         showerror('Error','Seats or Price or Time is Not Selected')
    else:
        showinfo('Success','Transaction is Completed. Thank You. Visit Again! :)')
          
def back():
    os.startfile("cinema.py")
    root.quit()

#===============Labels and Buttons================================
Label(root,text="|| Golmaal  Again ||",font="Georgia 30 bold",bg="Purple",fg="MistyRose",width=50,bd=20).grid(row=0,column=0,columnspan=5)
Label(root,text="Select your Seats , Price and Show Time for Golmaal movie?",font="cambria 20 bold",bg="lightblue").grid(row=1,column=0,pady=30,padx=0)

Label(root,text="How Many Seats?",font="cambria 20 bold",bg="OrangeRed").grid(row=2,column=0,sticky=W)
Radiobutton(root,text='1',font="cambria 15 bold",bg="plum",variable=v,value=1).grid(row=3,column=0,sticky='W')
Radiobutton(root,text='2',font="cambria 15 bold",bg="plum",variable=v,value=2).grid(row=4,column=0,sticky='W')
Radiobutton(root,text='3',font="cambria 15 bold",bg="plum",variable=v,value=3).grid(row=5,column=0,sticky='W')
Radiobutton(root,text='4',font="cambria 15 bold",bg="plum",variable=v,value=4).grid(row=6,column=0,sticky='W')
Radiobutton(root,text='5',font="cambria 15 bold",bg="plum",variable=v,value=5).grid(row=7,column=0,sticky='W')
Radiobutton(root,text='6',font="cambria 15 bold",bg="plum",variable=v,value=6).grid(row=8,column=0,sticky='W')
Radiobutton(root,text='7',font="cambria 15 bold",bg="plum",variable=v,value=7).grid(row=9,column=0,sticky='W')
Radiobutton(root,text='8',font="cambria 15 bold",bg="plum",variable=v,value=8).grid(row=10,column=0,sticky='W')
Radiobutton(root,text='9',font="cambria 15 bold",bg="plum",variable=v,value=9).grid(row=11,column=0,sticky='W')
Radiobutton(root,text='10',font="cambria 15 bold",bg="plum",variable=v,value=10).grid(row=12,column=0,sticky='W')

Label(root,text="Show Time",font="cambria 20 bold",bg="OrangeRed").grid(row=2,column=1,sticky=W)
Radiobutton(root,text='12 Noon',font="cambria 15 bold",bg="plum",variable=v1,value=1).grid(row=3,column=1,sticky='W')
Radiobutton(root,text='3 PM',font="cambria 15 bold",bg="plum",variable=v1,value=2).grid(row=4,column=1,sticky='W')
Radiobutton(root,text='6 PM',font="cambria 15 bold",bg="plum",variable=v1,value=3).grid(row=5,column=1,sticky='W')

Label(root,text="Price",font="cambria 20 bold",bg="OrangeRed").grid(row=2,column=2,sticky=W)
Radiobutton(root,text='Platinum(200)',font="cambria 15 bold",bg="plum",variable=v2,value=200).grid(row=3,column=2,sticky='W')
Radiobutton(root,text='Gold(150)',font="cambria 15 bold",bg="plum",variable=v2,value=150).grid(row=4,column=2,sticky='W')
Radiobutton(root,text='Silver(100)',font="cambria 15 bold",bg="plum",variable=v2,value=100).grid(row=5,column=2,sticky='W')
                                                                                           
Button(root,text="Check Rs.",font="times 20 bold",relief=SUNKEN,bg="black",fg="white",command=check,bd=10).grid(row=13,column=1)
Button(root,text="Back",font="times 20 bold",relief=SUNKEN,bg="black",fg="white",command=back,bd=10).grid(row=13,column=0,sticky='W',padx=60,pady=30)
Button(root,text="Book",font="times 20 bold",relief=SUNKEN,bg="black",fg="white",command=book,bd=10).grid(row=13,column=2,sticky='W',padx=60,pady=30)
Button(root,text="Pay",font="times 20 bold",relief=SUNKEN,bg="black",fg="white",command=pay,bd=10).grid(row=13,column=3,sticky='W',padx=60,pady=30)

Label(root,text="Total Cost of Ticket :",font="times 20 bold").grid(row=12,column=0,columnspan=1)


root.mainloop()
