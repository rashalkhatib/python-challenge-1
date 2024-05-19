# Menu dictionary
menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .66,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.99,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49

    }

}

# 1. Set up order list. Order list will store a list of dictionaries for
# menu item name, item price, and quantity ordered
orders = []

# Launch the store and present a greeting to the customer
print("Welcome to the variety food truck.")

# Customers may want to order multiple items, so let's create a continuous
# loop
place_order = True
while place_order:
    # Ask the customer from which menu category they want to order
    print("From which menu would you like to order? ")

    # Create a variable for the menu item number
    i = 1
    # Create a dictionary to store the menu for later retrieval
    menu_items = {}

    # Print the options to choose from menu headings (all the first level
    # dictionary items in menu).
    for key in menu.keys():
        print(f"{i}: {key}")
        # Store the menu category associated with its menu item number
        menu_items[i] = key
        # Add 1 to the menu item number
        i += 1

    # Get the customer's input
    menu_category = input("Type menu number: ")

    # Check if the customer's input is a number
    if menu_category.isdigit():
        # Check if the customer's input is a valid option
        if int(menu_category) in menu_items.keys():
            # menu_category_name = menu_items[int(menu_category)]

            # Save the menu category name to a variable
            menu_category_name = menu_items[int(menu_category)]
            # Print out the menu category name they selected
            print(f"You selected {menu_category_name}")

            # Print out the menu options from the menu_category_name
            print(f"What {menu_category_name} item would you like to order?")
            i = 1
            menu_items = {}
            print("Item # | Item name                | Price")
            print("-------|--------------------------|-------")
            for key, value in menu[menu_category_name].items():

                # Check if the menu item is a dictionary to handle differently
                if type(value) is dict:
                    for key2, value2 in value.items():
                        num_item_spaces = 24 - len(key + key2) - 3
                        item_spaces = " " * num_item_spaces
                        print(f"{i}      | {key} - {key2}{item_spaces} | ${value2}")
                        menu_items[i] = {
                            "Item name": key + " - " + key2,
                            "Price": value2
                        }
                        i += 1
                else:
                    num_item_spaces = 24 - len(key)
                    item_spaces = " " * num_item_spaces
                    print(f"{i}      | {key}{item_spaces} | ${value}")
                    menu_items[i] = {
                        "Item name": key,
                        "Price": value
                    }
                    i += 1

            # 2. Ask customer to input menu item number
            menu_item_number = input("Choose the item number you want to order: ")

                # 3. Check if the customer typed a number
            if menu_item_number.isdigit():
                    
            # Convert the menu selection to an integer
                    menu_item_number = int(menu_item_number)
            
            # 4. Check if the menu selection is in the menu items
            if menu_item_number in menu_items.keys():
                    
                    # Store the item name as a variable
                    selected_item = menu_items[menu_item_number]
                    item_name = selected_item["Item name"]
                    item_price = selected_item["Price"]
                    print(f"{item_name} for {item_price}")

                # Ask the customer for the quantity of the menu item
                    quantity = input(f"How many {item_name} would you like to order? ")

            # Check if the quantity is a number, default to 1 if not
                    if not quantity.isdigit():
                        quantity = 1
                    else:
                        quantity = int(quantity)
                    orders.append({
                        "Item name": item_name,
                        "Price": item_price,
                        "Quantity": quantity
                    })
                    print(f"Added {quantity} of {item_name} to your order.") 

            # What is the menu selection? is that in a variable somewhere? YES: menu_items
            else: 
            # Tell the customer they didn't select a menu option
                    print(f"{menu_item_number} is not a valid menu item.")
        else:
                # Tell the customer they didn't select a number
                print("You didn't select a valid number.")

            # Check if the menu_item_number appears in the menu_items (whatever that variable is)
            # How are the numbers stored in menu_items? INTEGERS; KEYS
            # How to check if an integer is a dictionary key?
            # if menu_item_number in menu_items:

                    # Store the item name as a variable
                    # What is the item? It's a meal item, like "sushi"
                    # Where is that? menu_items
            
                    # Ask the customer for the quantity of the menu item


                    # Check if the quantity is a number, default to 1 if not


                    # Add the item name, price, and quantity to the order list


                    # Tell the customer that their input isn't valid

 
                    # Tell the customer they didn't select a menu option

            #else:
            # Tell the customer they didn't select a menu option
       # print(f"{menu_category} was not a menu option.")
    # else:

    while True:
        # Ask the customer if they would like to order anything else
        keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o ").strip().lower()

        # 5. Check the customer's input
        # Keep ordering
        if keep_ordering == 'y':
            break

         # Exit the keep ordering question loop
        elif keep_ordering == 'n':
            place_order = False

            # Since the customer decided to stop ordering, thank them for
            # their order
            print("Thank you for your order!")
            break
            # Complete the order
            
        else:
            print("Please enter 'Y' for yes or 'N' for no")

                # Exit the keep ordering question loop

                # Keep ordering 
        if keep_ordering == 'N':
                place_order = False
                break
        else: place_order = True

# Print out the customer's order

print("Item name                 | Price  | Quantity")
print("--------------------------|--------|----------")

# 6. Loop through the items in the customer's order
for item in orders:
    item_name = item["Item name"]
    item_price = item["Price"]
    quantity = item["Quantity"]

    # 8. Calculate the number of spaces for formatted printing
    
    num_item_spaces = 25 - len(item_name)
    num_price_spaces = 5 - len(f"{item_price:.2f}")
    num_quantity_spaces = 7 - len(str(quantity))

    # 9. Create space strings
    item_spaces = " " * num_item_spaces
    price_spaces = " " * num_price_spaces
    quantity_spaces = " " * num_quantity_spaces

# 10. Print the item name, price, and quantity
    print(f"{item_name}{item_spaces} | ${item_price:.2f}{price_spaces} | {quantity}{quantity_spaces}")

# 11. Calculate the cost of the order using list comprehension
# Multiply the price by quantity for each item in the order list, then sum()
total_cost = sum(item["Price"] * item["Quantity"] for item in orders)

# Print the prices.
print(f"\nTotal cost: ${total_cost:.2f}")



