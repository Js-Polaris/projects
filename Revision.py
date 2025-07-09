print("WELCOME TO THE SCRUMPTIUOS CAFE")
def menu():
    A = {1:"1.Standard Meal-12,000UGX",
         2:"2.Vegetarian Meal-10,000UGX",
         3:"3.Deluxe Meal-15,000UGX"}
    MENU =("1.Standard Meal-12,000UGX","2.Vegetarian Meal-10,000UGX","3.Deluxe Meal-15,000UGX")
    for item in MENU:
        print(item)
menu()
stan_meal = 12000
Veg_meal = 10000
Del_meals = 15000
try:   
    Ordering_Hours = int(input("Hour of placing order: "))
except ValueError:
    print("Please Enter a Valid hour.")
if 1900<Ordering_Hours or Ordering_Hours <700:
    print("We are currnetly closed. Try again in our working hours.")
    exit()
else:
    while True:
        try:
            A = int(input("How many Standard Meals are you having: "))
            B =int(input("How many Vegetarian Meals are you having: "))
            C = int(input("How many Deluxe are you having: "))
        except ValueError:
            print("Enter a valid Order")
            break
        if A <0:
            print("Wrong number of orders made.")
            break
        elif B<0:
            print("Wrong order made")
            break
        elif C < 0:
            print("Wrong number of order made.")
        else:
            print("Your order has been successfully received.")
            break
Main_Order = A+B+C
prices = (A*stan_meal) + (B*Veg_meal) +(C*Del_meals)
print(f"You have ordered for {Main_Order} meals.")
if Main_Order>3:
    discount = (Main_Order -(prices*0.1))
    final_price = abs(discount)
    print(f"You have been awarded a 10% discount. Your new price is shs.{final_price}")
else:
    new_price = prices
    print(f" You have paid {new_price}. Thank you for coming")
exit()