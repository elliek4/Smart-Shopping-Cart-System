# Ellie Khoo
# AM
# Smart Shopping System

# create store inventory using two lists with product and price at same index
products = ["Chips", "Soda", "Candy", "Cookies", "Water", "Sandwich"]
prices = [2.00, 2.50, 1.50, 3.00, 1.00, 5.00]

# create shopping cart as list to store customer's desired products
shopping_cart = []

# function to display the menu and get user's choice
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
    return int(input("Enter your choice: "))

user_choice = display_menu()
print()

# check if customer entered invalid menu number, if so then goes back to menu
while user_choice < 1 or user_choice > 6:
    print("Invalid input!")
    print("Please choose a number between 1 and 6.")
    print()
    user_choice = int(input("Enter your choice: "))
    print()

# loop so that the menu continues until customer selects checkout
while user_choice != 6:

    # checks if user chose option 1 and displays the products and prices if so, then goes back to menu
    if user_choice == 1:
        print("=============== AVAILABLE PRODUCTS ===============")
        for i in range(6):
            print(f"#{(i + 1)}", products[i] + "     " + f"${prices[i]}")
        print()
        user_choice = display_menu()

    # checks if user chose option 2 and asks which product they want to purchase, adds it to the cart list, then goes back to menu
    elif user_choice == 2:
            
        # displays products
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
        
        user_choice = display_menu()

    # checks if user chose option 3 and displays shopping cart to allow removal of items, then goes back to menu
    elif user_choice == 3:
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
            shopping_cart.remove(shopping_cart[item_removal - 1])
            print()

        user_choice = display_menu()

    # checks if user chose option 4 and displays every product and price in shopping cart, then goes back to menu
    elif user_choice == 4:
        if len(shopping_cart) == 0:
            print("There is nothing currently in your shopping cart.")
            print()
        else:
            print("=============== YOUR SHOPPING CART ===============")
            print()

            # find price for each item in shopping cart using loop
            for i in range(len(shopping_cart)):
                for i in shopping_cart:
                    
                    if shopping_cart[i] == products[i]:
                        price = price[i]
                
                print(f"#{(i + 1)}", shopping_cart[i] + "     " + f"${price}")
            print()