menu = {
    'pizza':40,
    'pasta':50,
    'burger':70,
    'noodle':80,
    'french fries':90,
    'coffee':100,

}
#gread 
print("Hello!!! Welcome to our restorant :-)")
print("Pizza : 40\nPasta : 50\nBurger : 70\nNoodles : 80\nFrench Fries : 90\ncoffee : 100")
order_total =0
item_1=input("Which you want to order : ")
if item_1 in menu :
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added to your order ")
else:
    print("Please order somethin else or use menu ")
order= input("You want to order something else type YES/NO :")
if (order== "yes" or order == "YES"):
    item_2=input("Which you want to order next :")
    if item_2 in menu:
        order_total = menu[item_1] + menu[item_2]
        print(f"Your item {item_2} has been added to your order ")
    else:
        print("orded something else from menu :")
        

print("Your total bill is :",order_total)


