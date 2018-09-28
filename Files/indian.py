import os
from Tkinter import *
from tkMessageBox import *
root=Tk()
root.title("Indian Restaurant")
root.geometry('1367x768')
root.configure(background='Thistle')


v1=IntVar()
v2=IntVar()
v3=IntVar()
v4=IntVar()
v5=IntVar()
v6=IntVar()
v7=IntVar()
v8=IntVar()
v9=IntVar()
v10=IntVar()


#===============Functions=============================================

def check():
     if v1.get()+v2.get()+v3.get()+v4.get()+v5.get()+v6.get()+v7.get()+v8.get()+v9.get()+v10.get()== 0:
         showerror('Error','No item is Selected')
     else:
         Label(root,text="Rs.",font="cambria 20 bold").grid(row=10,column=1,sticky=W,padx=40) 
         Label(root,text=v1.get()+v2.get()+v3.get()+v4.get()+v5.get()+v6.get()+v7.get()+v8.get()+v9.get()+v10.get(),font="times 20 bold").grid(row=10,column=1)


def order():
     if v1.get()+v2.get()+v3.get()+v4.get()+v5.get()+v6.get()+v7.get()+v8.get()+v9.get()+v10.get() == 0:
         showerror('Error','No item is Selected')
     else:
         showinfo('Success','Order is Booked')
    
def pay():
    if v1.get()+v2.get()+v3.get()+v4.get()+v5.get()+v6.get()+v7.get()+v8.get()+v9.get()+v10.get() == 0:
        showerror('Error','No item is Selected')
    else:
        showinfo('Success','Transaction is Completed. Thank You. Visit Again! :)')
   
def back():
    os.startfile("restaurant.py")
    root.quit()

#===============Labels and Buttons================================
    
Label(root,text="||  Indian Foods  ||",font="Georgia 30 bold",bg="SeaGreen",fg="Gold",width=50,bd=20).grid(row=0,column=0,columnspan=4)
Label(root,text="Select your Food you want to eat?",font="cambria 20 bold",bg="lightblue").grid(row=1,column=0,pady=30,padx=0)

Label(root,text="North India:",font="cambria 20 bold",bg="OrangeRed").grid(row=2,column=0,sticky=W)
Checkbutton(root,text='Kadai Paneer(150)',font="cambria 20 bold",bg="Thistle",variable=v1,onvalue=150).grid(row=3,column=0,sticky='W')
Checkbutton(root,text='Mix Veg(150)',font="cambria 20 bold",bg="Thistle",variable=v2,onvalue=150).grid(row=4,column=0,sticky='W')
Checkbutton(root,text='Butter Panner Masala(200)',font="cambria 20 bold",bg="Thistle",variable=v3,onvalue=200).grid(row=5,column=0,sticky='W')
Checkbutton(root,text='Dum  Aloo(100)',font="cambria 20 bold",bg="Thistle",variable=v4,onvalue=100).grid(row=6,column=0,sticky='W')
Checkbutton(root,text='Butter Roti(10)',font="cambria 20 bold",bg="Thistle",variable=v5,onvalue=10).grid(row=7,column=0,sticky='W')

Label(root,text="South India:",font="times 20 bold",bg="OrangeRed").grid(row=2,column=2,sticky=W)
Checkbutton(root,text='Idli & Sambhar(50)',font="cambria 20 bold",bg="Thistle",variable=v6,onvalue=50).grid(row=3,column=2,sticky='W')
Checkbutton(root,text='Uttapam(60)',font="cambria 20 bold",bg="Thistle",variable=v7,onvalue=60).grid(row=4,column=2,sticky='W')
Checkbutton(root,text='Dosa(70)',font="cambria 20 bold",bg="Thistle",variable=v8,onvalue=70).grid(row=5,column=2,sticky='W')
Checkbutton(root,text='Pongal(80)',font="cambria 20 bold",bg="Thistle",variable=v9,onvalue=80).grid(row=6,column=2,sticky='W')
Checkbutton(root,text='Vada(30)',font="cambria 20 bold",bg="Thistle",variable=v10,onvalue=30).grid(row=7,column=2,sticky='W')
                                                                                             
Button(root,text="Check Rs.",font="times 20 bold",relief=SUNKEN,bg="black",fg="white",command=check,bd=10).grid(row=9,column=1,sticky=W,pady=30)
Button(root,text="Back",font="times 20 bold",relief=SUNKEN,bg="black",fg="white",command=back,bd=10).grid(row=9,column=0,sticky='W',padx=60,pady=30)
Button(root,text="Order",font="times 20 bold",relief=SUNKEN,bg="black",fg="white",command=order,bd=10).grid(row=9,column=2,sticky='W',pady=30)
Button(root,text="Pay",font="times 20 bold",relief=SUNKEN,bg="black",fg="white",command=pay,bd=10).grid(row=9,column=3,sticky='W',pady=30)

Label(root,text="Total Amount of Indian Food:",font="times 20 bold").grid(row=10,column=0,columnspan=1)
         
root.mainloop()
