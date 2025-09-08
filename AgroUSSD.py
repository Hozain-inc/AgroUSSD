AgroUSSD = []

while True:
    ussd = input("Enter your USSD code: ")
    
    if ussd != "*123#":
        print("Invalid code! Try again.\n")
    else:
        print("Welcome to AgroUSSD!")
        
        while True:  
            print("\nMain Menu:")
            print("1. Register")
            print("2. Buy Product")
            print("3. Sell Product")
            print("4. Products and Prices")
            print("5. Exit")
            
            choice = input("Enter an option: ")
            
            if choice == "1":
                print("\nRegistration")
                name = input("Enter your full name: ")
                phone = input("Enter your phone number: ")
                location = input("Enter your location: ")
                
            
                print("\nRegister as:")
                print("1. Buyer")
                print("2. Seller")
                role_choice = input("Select role (1 or 2): ")
                
                if role_choice == "1":
                    category = "Buyer"
                elif role_choice == "2":
                    category = "Seller"
                else:
                    category = "Unspecified"
                
                # Save details
                user = {
                    "name": name,
                    "phone": phone,
                    "location": location,
                    "category": category
                }
                AgroUSSD.append(user)
                print(f"\n{name}, you have been registered successfully as a {category}!")
            
            elif choice == "2":
                if not AgroUSSD:
                    print("\nYou must register first before buying a product.")
                else:
                    product = input("Enter the product you want to buy: ")
                    print(f"You selected to buy {product}. We will reach out to you.")
            
            elif choice == "3":
                if not AgroUSSD:
                    print("\nYou must register first before selling a product.")
                else:
                    product = input("Enter the product you want to sell: ")
                    price = input("Enter your selling price: ")
                    print(f"You listed {product} for sale at {price} Naira.")
            
            elif choice == "4":
                if not AgroUSSD:
                    print("\nYou must register first to view products and prices.")
                else:
                    print("\nAvailable Products and Prices:")
                    print("1. Tomatoes - ₦500 per basket")
                    print("2. Maize - ₦20,000 per bag")
                    print("3. Rice - ₦35,000 per bag")
                    print("4. Yam - ₦1,000 per tuber")
            
            elif choice == "5":
                print("Thank you for using AgroUSSD. Goodbye!")
                break 
            
            else:
                print("Invalid!, please try again.")
        break 
