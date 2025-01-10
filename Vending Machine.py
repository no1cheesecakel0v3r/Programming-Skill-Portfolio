"""

Meow's Vending Meowchine!
( Vending Machine )
by Maria Angelica Gilleone Dy Rapsing

"""

def create_item(name, price, category, stock):  # this is a function that creates an item for the vending machine.
    return {                                    # this dictionary will be containing the name, price, category and -
        'name' : name,                          # stock of the item.
        'price': price,                         
        'category': category,
        'stock': stock
    }

def display_menu(items):                        # this function will be displaying the menu of the vending machine.
    categories = {}                             # this will also be showing each category the item is in.
    for code, item in items.items():
        if item['category'] not in categories:
            categories[item['category']] = []
        categories[item['category']].append((code, item))

    for category, items in categories.items(): # this code will basically show how the item will be presented -
        print(f"\n{category} Menu:")           # inside the vending machine.
        for code, item in items:
            print(f"{code}: ({item['name']} - {item['price']:.2f} DHS) ({item['stock']} in stock)")

def purchase_item(item):                       # this code will run each time the user selects an item to -
    if item['stock'] > 0:                      # purchase; when the user selects an item, the code will -
        item['stock'] -= 1                     # check if the item is in stock, and if it is, it will deduct -
        return True                            # the stock of the item by 1.
    return False

items = {                                      # this dictionary contains all the items in the vending machine.
    'A1': create_item('Biscuits', 2.00, 'Snacks', 10),
    'A2': create_item('Kitkat', 2.00, 'Snacks', 10),
    'A3': create_item('Twix', 2.00, 'Snacks', 10),
    'A4': create_item('Mars', 2.00, 'Snacks', 10),
    'A5': create_item('Lays Chips', 3.00, 'Snacks', 5),
    'B1': create_item('Cappuccino', 4.00, 'Hot Beverages', 4),
    'B2': create_item('Americano', 4.00, 'Hot Beverages', 4),
    'B3': create_item('Espresso', 4.00, 'Hot Beverages', 4),
    'B4': create_item('Green Tea', 3.00, 'Hot Beverages', 5),
    'B5': create_item('Karak', 3.00, 'Hot Beverages', 5),
    'C1': create_item('Chocolate Milk', 3.00, 'Cold Beverages', 4),
    'C2': create_item('Juice', 3.00, 'Cold Beverages', 4),
    'C3': create_item('Cold Water', 2.00, 'Cold Beverages', 10),
    'C4': create_item('Ice Tea', 3.00, 'Cold Beverages', 4),
    'C5': create_item('Ice Coffee', 3.00, 'Cold Beverages', 4)
}

current_money = 20.00                          # this shows how much money the user presently has.
total_cost = 0.00                              # this shows how much money the user has spent on the vending machine.
selected_items = []                            # this show the items that the user has selected in the machine.

print("\n")
print(                                         # this code prints out the welcoming message for the user before showing the menu.
    """                                          
    ╭──────────────────────────.★..───────╮

    Welcome to Meow's Vending Meowchine~! 
    What would you like to order~?

    ╰─────────────..★.────────────────────╯
    """                                         
)

print(f"You currently have: {current_money:.2f} DHS") # this prints out how much money the user has.

while True:
    display_menu(items)                         # this bundle of code displays the menu and then the selection line.
    print("\n")
    user_input = input("Please enter the code of the item you want to purrrchase~! orr 'exit' to quit!: ").upper()

    if user_input == 'EXIT':                    # this code will run when the user types 'exit' and will stop running.
        print("Thank you for using Meow's Vending Meowchine~!")
        break

    if user_input in items:
        item = items[user_input]
        if item['stock'] > 0:
            if total_cost + item['price'] <= current_money:   # this code will run if the user has enough money to purchase an item.
                selected_items.append(item)                   # this code will add an item to the already selected items.
                total_cost += item['price']                   # this code will be updating the total cost.
                purchase_item(item)                           # this code runs when purchasing the item/s selected.
                remaining_money = current_money - total_cost  # this will calculate your current money and the cost of the items.
                print(f"You have selected: {item['name']} for {item['price']:.2f}.") 
                print(f"Current total cost: {total_cost:.2f}")
                print(f"Remaining cash: {remaining_money:.2f} DHS")  # this will be displaying how much money you have left.

                more_items = input("Would you like to buy another item? (yes/no): ").lower() # this will ask the user if they want to buy more from the machine.
                if more_items != 'yes':                                 
                    print("You have selected the following items:")
                    for selected in selected_items:
                        print(f"- {selected['name']} for {selected['price']:.2f}")
                    print(f"Total amount due: {total_cost:.2f} DHS. Thank you for using Meow's Vending Meowchine~!") # this will show during the final check out.
                    break
            else:
                print("Sorry, you do not have enough money for this item.") # this code will only run if the user tries to buy something despite not having enough money left in their balance anymore.
                print("Redirecting to checkout...")  # this code redirects the user to the check out.
                print("You have selected the following items:")
                for selected in selected_items:
                    print(f"- {selected['name']} for {selected['price']:.2f}") 
                print(f"Total amount due: {total_cost:.2f} DHS. Thank you for using Meow's Vending Meowchine~!") # this code is a goodbye message to the user as well as a "receipt" for the user.
                break
        else:
            print(f"Sorry, {item['name']} is out of stock.") # this code will run when the item is out of stock
    else:
        print("Invalid selection. Please try again.") # this code will run when the user inputs something that isnt the code listed in the vending machine.