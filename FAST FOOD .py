#dictionary + conditional statements are used in this project
#Define the menu of restaurant:
menu = {
    'Pizza': 100,
    'Pasta': 500,
    'Burger': 150,
    'Coffee': 90
}

#Greet
print("Welcome to Python FOODS")
print("pizza: Rs100\nPasta: Rs500\nBurger: Rs150\nCoffee: Rs90")

#What to order
order_total = 0
#100 + 500 = 600

item_1 = input("Enter the name of item you want to order = ")
if item_1 in menu:
    order_total += menu[item_1]  #0 + 100 = 150
    print(f"Your item {item_1} has been added to your order")
else:
    print(f"Sorry! order some-thing that is available in {item_1}")

another_order = input("Do you want to order another item? (YES/NO) ")
if another_order == "YES":
    item_2 = input("Enter the name of second item!")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item {item_2} has been added to order")
    else:
        print(f"Sorry! order some-thing that is available in {item_2}")
        
print(f"THe total amount of items is {order_total}")
