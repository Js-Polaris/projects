print("Welcome to The Library Return Portal")
while True:
    try:
        Late_days = int(input("How many late days does this book have: "))
    except ValueError:
        print("Try again!")
    break
##validation for days
##validation for days:
if 0<Late_days<= 7:
    fine_paid= (Late_days*1000)
elif 7< Late_days<= 30:
    fine_paid =(Late_days*2000)
elif Late_days>= 30:
    fine_paid= 50000
    print("You have been banned from the library.")
else:
    print("Input the right value.")
number_of_late_days = Late_days
print(f"Your book is {Late_days} overdue. Your fine is Shs.{fine_paid}")


