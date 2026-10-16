# Ellie Khoo
# AM
# Smart Shopping System

# import date and time module
import datetime
current_date = datetime.date.today()

# introduce user to the program
print()
print("Hello user!")
print("Welcome to the Smart Shopping System!")
print('We will keep track of all the things you buy and their prices.')
print("Checkout when you're finished!")
print()

# create store inventory using two lists with product and price at same index
products = ["Chips", "Soda", "Candy", "Cookies", "Water", "Sandwich"]
prices = [2.00, 2.50, 1.50, 3.00, 1.00, 5.00]

# create shopping cart as list to store customer's desired products
shopping_cart = []

# function to display the menu and get user's choice, also checks for invalid options
def display_menu():
    print("=============== SMART SHOPPING CART ===============")
    print("1. View Available Products")
    print("2. Add Product to Cart")
    print("3. Remove Product from Cart")
    print("4. View Shopping Cart")
    print("5. View Current Total")
    print("6. Checkout")
    print()

    # gets user's choice
    user_choice = int(input("Enter your choice: "))
    print()

    # check if customer entered invalid menu number, if so then goes back to menu
    while user_choice < 1 or user_choice > 6:
        print("Invalid input!")
        print("Please choose a number between 1 and 6.")
        print()
        user_choice = int(input("Enter your choice: "))
        print()
    
    return user_choice

user_choice = display_menu()
print()

# function for option 1 to display available products and their prices using loop
def display_products():
    print("=============== AVAILABLE PRODUCTS ===============")
    print()
    for i in range(6):
        print(f"#{(i + 1)}", products[i] + "     " + f"${prices[i]:.2f}")
    print()

# function for option 2 that asks user which product they want to purchase and adds it to their shopping list
def add_product():
    print("Which product would you like to add?")
    print()
    for i in range(6):
        print(f"#{(i + 1)}", products[i])
    print()

    # asks user for product 
    add_product = int(input("Enter product number: "))

    # checks whether product number is invalid, otherwise repeats asking until it is
    while add_product < 1 or add_product > 6:
        print("Invalid product!")
        print("Please choose a number between 1 and 6.")
        print()
        add_product = int(input("Enter product number: "))
        print()

    # adds validated product to cart list using index
    shopping_cart.append(products[add_product - 1])
    print(products[add_product - 1], "was added to your cart!")
    print()

# function for option 3 that displays shopping cart and allows removal of items
def remove_product():
    if len(shopping_cart) == 0:
        print("Your shopping cart is empty!")
        print("There is nothing to remove.")
        print()
    else:
        print("=============== YOUR SHOPPING CART ===============")
        print()
        for i in range(len(shopping_cart)):
            print(f"#{(i + 1)}", shopping_cart[i])
        print()

        # asks which item user wants to remove
        print("Which item would you like to remove?")
        item_removal = int(input("Enter item number: "))
        print()

        # validates whether item number 
        while item_removal < 1 or item_removal > len(shopping_cart):
            print("Invalid item!")

            if len(shopping_cart) == 1:
                print("You only have", len(shopping_cart), "item in your cart.")
                print()
            else:
                print("You only have", len(shopping_cart), "items in your cart.")
                print()

            item_removal = int(input("Enter item number: "))
            print()

        # removes item from list and displays which item was removed from user's cart 
        print(shopping_cart[item_removal - 1], "was removed from your cart!")
        shopping_cart.pop(item_removal - 1)
        print()

# function for option 4 that displays every product and its price in shopping cart
def display_cart():
    if len(shopping_cart) == 0:
        print("There is nothing currently in your shopping cart.")
        print()
    else:
        print("=============== YOUR SHOPPING CART ===============")
        print()

        # find price for each item in shopping cart using loops
        price = 0
        for i in range(len(shopping_cart)):
                
            #create a nested loop to get price by checking if shopping cart item = every item in products
            for a in range(len(products)):
                if shopping_cart[i] == products[a]:
                    price = prices[a]
                
            print(f"#{(i + 1)}", shopping_cart[i] + "     " + f"${price:.2f}")
        print()

        # display number of items in shopping cart using len
        print("Total Items:", len(shopping_cart))
        print()

# function for option 5 that displays current total and every product and its price in shopping cart, then calculates and displays subtotal
def calculate_subtotal():
    if len(shopping_cart) == 0:
        print("There is nothing currently in your shopping cart.")
        print()
    else:
        print("=============== CURRENT TOTAL ===============")
        print()

        # find price for each item in shopping cart using loops
        price = 0
        subtotal = 0
        for i in range(len(shopping_cart)):
                
            #create a nested loop to get price by checking if shopping cart item = every item in products
            for a in range(len(products)):
                if shopping_cart[i] == products[a]:
                    price = prices[a]
                
            subtotal += price
            print(f"#{(i + 1)}", shopping_cart[i] + "     " + f"${price:.2f}")
        print()

        print("Subtotal:", f"${subtotal:.2f}")
        print()

        return subtotal

# loop so that the menu continues until customer selects option 6 checkout
while user_choice != 6:

    # checks if user chose option 1, then calls displaying products function, afterwards returns back to menu
    if user_choice == 1:
        
        display_products()
        user_choice = display_menu()

    # checks if user chose option 2, then calls adding product function, afterwards returns back to menu
    elif user_choice == 2:
        
        add_product()
        user_choice = display_menu()

    # checks if user chose option 3, then calls removing product function, afterwards returns back to menu
    elif user_choice == 3:

        remove_product()
        user_choice = display_menu()

    # checks if user chose option 4, then calls display shopping cart function, afterwards returns back to menu
    elif user_choice == 4:
        
        display_cart()
        user_choice = display_menu()

    # checks if user chose option 5, then calls calculate subtotal function, afterwards returns back to menu
    elif user_choice == 5:
        
        calculate_subtotal()
        user_choice = display_menu()

if len(shopping_cart) == 0:
    print("You didn't buy anything today.")
    print("Come back next time!")
else: 
    # checkout system using conditionals to check discounts based on subtotal
    discount = 0
    subtotal = calculate_subtotal()
    if subtotal >= 40:
        discount = 0.15
    elif subtotal < 40 and subtotal >= 20:
        discount = 0.1
    elif subtotal < 20 and subtotal >= 10:
        discount = 0.05

    # display checkout info including amount saved, discount, and final total
    print()
    print("=============== CURRENT TOTAL ===============")
    print("Date:", current_date)
    print()
    print("Subtotal:", f"${subtotal:.2f}")
    print("Discount:", discount * 100, "percent")
    print(f"Amount Saved: ${subtotal * discount:.2f}")
    print()
    print("Final Total:", f"${subtotal - (subtotal * discount):.2f}")
    print()
    print("Thank you for shopping!")

