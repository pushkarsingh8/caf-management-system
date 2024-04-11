#cafe MG System:-
from tkinter import*
from tkinter import messagebox
import subprocess

charges = ""
def order_window():
    global charges
    customer_name = name.get().capitalize()
    if len(customer_name) != 0:
        
        if dailon.get() == 1 and new.get() == 1:
            messagebox.showerror("warn","don't click both checkbox")
            
            
        elif dailon.get() == 1:
            
            window.destroy()
            charges = "Yes"
            subprocess.Popen(["Python","caffe_order_&_payment.py",customer_name,charges])
            
        elif new.get() == 1:
            
            window.destroy()
            charges = "No"
            subprocess.Popen(["Python","caffe_order_&_payment.py",customer_name,charges])
            

        else:
            messagebox.showerror("Error","please any checkbox\nfor further uses")
            
        
    
        
    else:
        messagebox.showerror("Empty-name","Please Enter Name\nEx:- pushkar")



window = Tk() 
window.title("café System")
window.geometry("350x260")


dailon = IntVar()
new = IntVar()

title = Label(window,text="My café",font=("Times New Roman ",22,"bold underline"))
title.place(x=120,y=10)


label_name = Label(window,text="Name:",font="bold")
label_name.place(x=60,y=70)

name = Entry(window)
name.place(x=120,y=73)

c1 = Checkbutton(window,text="dailon",font=15,variable=dailon)
c1.place(x=80,y=120)

c2 = Checkbutton(window,text="New Customer",font=15,variable=new)
c2.place(x=180,y=120)


go = Button(window,text="Go",font=("bold",15),borderwidth=14,fg="red",command=order_window)
go.place(x=140,y=180)







window.mainloop()



