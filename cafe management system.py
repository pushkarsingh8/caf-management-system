from prettytable import PrettyTable
import time


menu = {
    "Cake" : 50,
    "Coffee" : 80,
    "Tea"   :  20,
    "Burger" : 40,
    "Pizza" : 150,
    "Frenchfries" : 120,
    "Noodles" : 45,
    "Soft drink" : 60
}
cart = 0
name = input("Enter your name: ").capitalize()
print(f"\nWelcome {name} in Cafe ")
print("*"*24)

table = PrettyTable(["Food Items","Price"])
for item,price in menu.items():
    table.add_row([item,price])
    
table.add_autoindex("S.no")
table.title = "***Pushkar café***"
print(table)

#********************************************************************************

user = input("\ntell me what you want one food item: ").capitalize()
while True:
    if user in menu.keys():
        cart += menu[user]
        choice = input("\nyou want Add or items (yes/no): ").capitalize()
        if choice == "Yes":
            user = input("\ntell me next food items: ").capitalize()
    
            
        elif choice == "No":
            print("Wait....")
            time.sleep(3)
            print(f"\nThanks {name} for Order")
            print(f"Sir,\nYour Bill Amount is: {cart} Rs") 
            break
            
        else:
            print("you want order yes/no")
            choice = input(">").capitalize()
            
            if choice == "Yes":
                user = input("\nnext order sir,: ").capitalize()
            
            elif choice == "No":
                print("Wait....")
                time.sleep(3)
                print(f"\nThanks {name} for Order")
                print(f"Sir,\nYour Bill Amount is: {cart} Rs\n") 
                break
            
            else:
                print("Give me valid response")
                user = input("\ntell you want food items: ").capitalize()
                    
                                       
        
    elif user == "No":
        print(f"that's alright {name}\nSee you again...")
        break
        
    else:
        print(f"{name}sorry, this item not available in Menu Card")
        user = input("\ntell me order: ").capitalize()
        