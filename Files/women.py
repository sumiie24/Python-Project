import os
from Tkinter import *
from tkMessageBox import *

root=Tk()
root.title("Women Shopping")
root.geometry('1367x768')
root.configure(background='Silver')

v1=IntVar()
v2=IntVar()
v3=IntVar()
v4=IntVar()
v5=IntVar()
v6=IntVar()
v7=IntVar()
v8=IntVar()
v9=IntVar()

#===============Functions=============================================

def check():
     if v1.get()+v2.get()+v3.get()+v4.get()+v5.get()+v6.get()+v7.get()+v8.get()+v9.get()== 0:
         showerror('Error','No item is Selected')
     else:
         Label(root,text="Rs.",font="times 20 bold").grid(row=9,column=1,sticky=W,padx=105)
         Label(root,text=v1.get()+v2.get()+v3.get()+v4.get()+v5.get()+v6.get()+v7.get()+v8.get()+v9.get(),font="times 20 bold").grid(row=9,column=1)

def order():
     if v1.get()+v2.get()+v3.get()+v4.get()+v5.get()+v6.get()+v7.get()+v8.get()+v9.get() == 0:
         showerror('Error','No item is Selected')
     else:
         showinfo('Success','Order is Booked')
    
def pay():
    if v1.get()+v2.get()+v3.get()+v4.get()+v5.get()+v6.get()+v7.get()+v8.get()+v9.get() == 0:
        showerror('Error','No item is Selected')
    else:
        showinfo('Success','Transaction is Completed. Thank You. Visit Again! :)')
    
def back():
    os.startfile("shopping.py")
    root.quit()

#===============Labels and Buttons================================
Label(root,text="||  Women's Shopping  ||",font="Georgia 30 bold",bg="khaki",fg="Indigo",width=50,bd=20).grid(row=0,column=0,columnspan=4,)
Label(root,text="Select your Clothes you want to Buy:",font="cambria 20 bold",bg="lightblue").grid(row=1,column=0,pady=40,padx=0)

Label(root,text="Ethnic Wear:",font="times 20 bold",bg="OrangeRed").grid(row=2,column=0,sticky=W,pady=20)
Checkbutton(root,text='Suit(800)',font="times 20 bold",bg="Silver",fg="Brown",variable=v1,onvalue=800,).grid(row=3,column=0,sticky='W',)
Checkbutton(root,text='Saree(500)',font="times 20 bold",bg="Silver",fg="Brown",variable=v2,onvalue=500).grid(row=4,column=0,sticky='W')
Checkbutton(root,text='Kurta(300)',font="times 20 bold",bg="Silver",fg="Brown",variable=v3,onvalue=300).grid(row=5,column=0,sticky='W')

Label(root,text="Clothes:",font="times 25 bold",bg="OrangeRed").grid(row=2,column=1,sticky=W)
Checkbutton(root,text='Trouser(300)',font="times 20 bold",bg="Silver",fg="Brown",variable=v4,onvalue=300).grid(row=3,column=1,sticky='W')
Checkbutton(root,text='Tops(300)',font="times 20 bold",bg="Silver",fg="Brown",variable=v5,onvalue=300).grid(row=4,column=1,sticky='W')
Checkbutton(root,text='Shirts(400)',font="times 20 bold",bg="Silver",fg="Brown",variable=v6,onvalue=400).grid(row=5,column=1,sticky='W')

Label(root,text="Accessories:",font="times 25 bold",bg="OrangeRed").grid(row=2,column=2,sticky=W)
Checkbutton(root,text='Handbags(300)',font="times 20 bold",bg="Silver",fg="Brown",variable=v7,onvalue=300).grid(row=3,column=2,sticky='W')
Checkbutton(root,text='Earings(100)',font="times 20 bold",bg="Silver",fg="Brown",variable=v8,onvalue=100).grid(row=4,column=2,sticky='W')
Checkbutton(root,text='Watches(600)',font="times 20 bold",bg="Silver",fg="Brown",variable=v9,onvalue=600).grid(row=5,column=2,sticky='W')

Button(root,text="Check Rs.",font="times 20 bold",relief=SUNKEN,bg="black",fg="white",command=check,bd=10).grid(row=7,column=1,sticky='W',pady=50)
Button(root,text="Back",font="times 20 bold",relief=SUNKEN,bg="black",fg="white",command=back,bd=10).grid(row=7,column=0,sticky='W',padx=60,pady=50)
Button(root,text="Order",font="times 20 bold",relief=SUNKEN,bg="black",fg="white",command=order,bd=10).grid(row=7,column=2,sticky='W',pady=50)
Button(root,text="Pay",font="times 20 bold",relief=SUNKEN,bg="black",fg="white",command=pay,bd=10).grid(row=7,column=3,sticky='W',pady=50)

Label(root,text="Total Amount of Women's Shopping:",font="times 20 bold").grid(row=9,column=0,columnspan=1)

root.mainloop()

