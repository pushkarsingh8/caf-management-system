from tkinter import*
from tkinter import messagebox
import sys
import subprocess
from prettytable import PrettyTable


order_time = Tk()
order_time.title("Order Page")
order_time.geometry("445x450")
total1 = []
listt = {}


def item_sum(name,price):
    global total1,tt11,listt,customer_name,charges,reduce
    
    if len(total1)!=5:   
        listt[name] = price
        e1.insert(END,f"{name}, ")
        total1.append(int(price))
        tt11 = sum(total1)
        t11.config(text = f"{tt11} Rs")
        
        
        
    else:
    
        messagebox.showerror("Exceed","You can't\nadd items 5 Limit")
        
        
def clearr():
    e1.delete(0,END)
    t11.config(text="")
    total1.clear()
    listt.clear()
    
    

if len(sys.argv) >1 and len(sys.argv)>1:
    customer_name = sys.argv[1]
    charges = sys.argv[2]
    print(customer_name)
    if charges == "Yes":
        reduce = 2
        
    else:
        reduce = 0
        
        

    
    
    
def pay():
    order_time.destroy()
    table = PrettyTable()
    payment_window = Tk()
    payment_window.title("Payment-Page")
    payment_window.geometry("400x400")

    

    total_price = sum(int(price) for price in listt.values())
    

    
    if reduce>1:
        margin_price = int((4/5)*total_price)
        reduced_price_var = StringVar()
        reduced_price_var.set(f"{margin_price} Rs\n*Reduced Price 20%\n for Daily customer")
    else:
        reduced_price_var = StringVar()
        reduced_price_var.set(f"{total_price} Rs")
        


    #table-part-------------------------
    table.field_names = ["Items","Prices"]
    for name,value in listt.items():    
        table.add_row([name,value])
    table.add_autoindex("S_no")
    


    namee = Label(text=f"Thanks For Order,{customer_name}",font=14)
    namee.place(x=85,y=12)
    
    table_str = table.get_string()
    description = Label(payment_window, text=table_str, justify=LEFT, font=("Courier", 10))
    description.place(x=70, y=100)

    total = Label(payment_window,text="Total =")
    total.place(x=90,y=300)

    total_m = Label(payment_window,textvariable=reduced_price_var)
    total_m.place(x=150,y=300)

        
            
    

    
    
#------------------Order-window-label------------------------------------------#   

    
    
t1 = Label(order_time,text=f"Weclome {customer_name}",font=("bold",20),fg="green")
t1.place(x=120,y=4)

    
e1 = Entry(order_time,font=("bold",10),bg='red',width=61)
e1.place(x=6,y=40,height=30)

b1_image = PhotoImage(file="coffee.png",)
b1_size = b1_image.subsample(8,8)
b1 = Button(order_time,image=b1_size,font=20,height=80,width=80,command=lambda:item_sum("Coffee","80"))
b1.place(x=1,y=120)

l1 = Label(order_time,text="Coffee.Rs 50")
l1.place(x=8,y=210)

b2_image = PhotoImage(file="soft-drink.png")
b2_size = b2_image.subsample(8,8)
b2 = Button(order_time,image=b2_size,font=20,height=80,width=80,command=lambda:item_sum("Soft-drink","60"))
b2.place(x=90,y=120)

l2 = Label(order_time,text="Drink.Rs 60")
l2.place(x=95,y=210)


b3_image = PhotoImage(file="ramen.png")
b3_size = b3_image.subsample(8,8)
b3 = Button(order_time,image=b3_size,font=20,height=80,width=80,command=lambda:item_sum("Noodles","110"))
b3.place(x=175,y=120)

l3 = Label(order_time,text="Noodles.Rs 110")
l3.place(x=175,y=210)



b4_image = PhotoImage(file="french-fries.png")
b4_size = b4_image.subsample(8,8)
b4 = Button(order_time,image=b4_size,font=20,height=80,width=80,command=lambda:item_sum("French-fries","130"))
b4.place(x=265,y=120)

l4 = Label(order_time,text="fr-fries.Rs 130")
l4.place(x=269,y=210)



b5_image = PhotoImage(file="pizza.png")
b5_size = b5_image.subsample(8,8)
b5 = Button(order_time,image=b5_size,font=20,height=80,width=80,command=lambda:item_sum("Pizza","200"))
b5.place(x=355,y=120)

l5 = Label(order_time,text="Pizza.Rs 200")
l5.place(x=363,y=210)


b6_image = PhotoImage(file="birthday-cake.png")
b6_size = b6_image.subsample(8,8)
b6 = Button(order_time,image=b6_size,font=20,height=80,width=80,command=lambda:item_sum("Cake","150"))
b6.place(x=1,y=240)

l6 = Label(order_time,text="Cake.Rs 150")
l6.place(x=8,y=330)


b7_image = PhotoImage(file="tea-cup.png")
b7_size = b7_image.subsample(8,8)
b7 = Button(order_time,image=b7_size,font=20,height=80,width=80,command=lambda:item_sum("Tea-cup","50"))
b7.place(x=90,y=240)

l7 = Label(order_time,text="Tea-Cup.Rs 20")
l7.place(x=90,y=330)


b8_image = PhotoImage(file="burger.png")
b8_size = b8_image.subsample(8,8)
b8 = Button(order_time,image=b8_size,font=20,height=80,width=80,command=lambda:item_sum("Burger","80"))
b8.place(x=175,y=240)

l8 = Label(order_time,text="Burger.Rs 80")
l8.place(x=175,y=330)



b9_image = PhotoImage(file="chole-bhature.png")
b9_size = b9_image.subsample(8,8)
b9 = Button(order_time,image=b9_size,font=20,height=80,width=80,command=lambda:item_sum("Chole-bhature","150"))
b9.place(x=265,y=240)

l9 = Label(order_time,text="chole-bhat.Rs 150")
l9.place(x=255,y=330)



b10_image = PhotoImage(file="sweets.png")
b10_size = b10_image.subsample(1,1)
b10= Button(order_time,image=b10_size,font=20,height=80,width=80,command=lambda:item_sum("Sweets","200"))
b10.place(x=355,y=240)

l10 = Label(order_time,text="Sweets.Rs 200")
l10.place(x=355,y=330)


#buttons---------------------------------------------------------------------------
collection = Button(text="Pay",font="bold",command=pay)
collection.place(x=250,y=400)

clear = Button(text="Clear",font="bold",command=clearr)
clear.place(x=135,y=400)

t11 = Label(text="0 Rs",font="bold")
t11.place(x=20,y=405)

order_time.mainloop()



