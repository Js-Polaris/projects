def menu():
    print("Welcome to ZolaTel Data Bundle Selection\n1. Daily Data Bundles\n2.Nyongeza Bundles")

while True:
    User_Code = input("Enter product code:")
    if User_Code =="*101#":
        menu()
        break
    else:
        print("Invalid Code has been entered.")
        break

# defining the bundle offers  
Option_1 = ("Your daily Data Bundles\n1.200MBs-shs.2000\n2.500MBs-shs.3000\nEnyongeza Bundles\n3.5GB-shs.7500\n4.20GB-shs.14000")

#selection of bundle types

    ##For particular bundles
Selection = int(input("Bundle selection: "))
payment_options = ("1.Mobile Money\n2.Airtime")
while True:
    if Selection == 1:
        print(payment_options)
        break
    elif Selection == 2:
        print(payment_options)
        break
    else:
        print()
        break
##payment options
payment_mtd = int(input("Select method of payment: "))

if payment_mtd ==1:
        Account= {"Balance": 15000, "Pin": 2990}
        entered_pin = int(input("Please enter your Mobile money pin: "))
        bundle_price = {1:2000, 2: 3000,3: 14000,4: 7500, 0: "Back"}
        bundle_name = {1: "200MBS at 2000", 2: "300MBS at 3000", 3: "20GBS at 14000", 4: "1.5GBS at 7500"}
        print(Option_1)
        
        
        while True:
            selection = int(input("Select Bundle Option:"))
            if selection == 1:
                print(Option_1)
                break 
            elif selection == 2:
                print(Option_1)
                break
            elif selection==3:
                print(Option_1)
            elif selection == 4:
                    print(Option_1)
            else:
                    print("Wrong Bundle selection")
                    break
            
            
            if entered_pin == Account["Pin"]:
                    print("Access Granted")
                    print("You have", Account["Balance"], "Shs\n")
                    for key in bundle_name:
                        print(f"{key}.{bundle_name[key]}")
                        price = bundle_price[selection]               
                        if price == 0:
                            print(Option_1)
                        elif Account["Balance"]>= price:
                            Account["Balance"] -= price
                            print(f"You have bought: {bundle_name[selection]}")
                            print(f"You have: {Account["Balance"]}")
                            break
                        else:
                            print("You have insufficient Balance to buy this bundle.")
                    else:
                        print("Select right bundle.")
            else:
                    print("Invalid pin entered")
                    break

        
