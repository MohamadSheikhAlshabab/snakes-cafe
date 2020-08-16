from textwrap import dedent
def welcome():
    msg_wlc= """
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************
    """
    print(msg_wlc)
welcome()
menu={
    "Appetizers" :["Wings","Cookies","Spring Rolls"],
    "Entrees" :["Salmon","Steak","Meat Tornado","A Literal Garden"],
    "Desserts" :["Ice Cream","Cake","Pie"],
    "Drinks" :["Coffee","Tea","Unicorn Tears"],
}   
print("Appetizers")
print("----------")
print(menu["Appetizers"][0])
print(menu["Appetizers"][1])
print(menu["Appetizers"][2])
print("         ")
print("Entrees")
print("----------")
print(menu["Entrees"][0])
print(menu["Entrees"][1])
print(menu["Entrees"][2])
print(menu["Entrees"][3])
print("         ")
print("Desserts")
print("----------")
print(menu["Desserts"][0])
print(menu["Desserts"][1])
print(menu["Desserts"][2])
print("         ")
print("Drinks")
print("----------")
print(menu["Drinks"][0])
print(menu["Drinks"][1])
print(menu["Drinks"][2])
print("         ")
print("         ")

orders=[]
counter=0

def msg_orders():
    msg_order= """
***********************************
** What would you like to order? **
***********************************
    """
    print(msg_order)

def order_fun():    
    while True:
        order=input("> ")
        def Counter():
            if order in orders:
                return orders.count(order)
        def what_order():
            for item in menu:
                for one in range(0,3):
                    if order==menu[item][one]:
                        orders.append(order)
                        your_order="** {} order of {} have been added to your meal **"
                        print(your_order.format(Counter(),menu[item][one]))
        what_order()
        if order=="quit":
            break
            


msg_orders()
order_fun()