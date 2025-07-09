##entering the number of students who attended the test.
while True:
    try:
        for i in range(3):
            Attending_students = int(input("How many students did the test:"))
            if 0<Attending_students<= 5:
                print("You are free to continue.")
                break
            else:
                print("This number of students is not registered.")
                exit()
    except ValueError:
        print("Please enter a valid number of students between 1 and 5.")
        continue
##For each student entered, the marks are entered and the average is calculated.        
    for student_index in range(Attending_students):
        
            while True:
                try:
                    marks= print(f"Enter the student's marks for {student_index + 1}")
                    one = float(input("Mark 1:"))
                    two = float(input("Mark 2: "))
                    three= float(input("Mark 3: "))
                    if 0<=one<=100 and 0<=two<=100 and 0<=three<=100:
                        print("Marks are valid")
                    else:
                        print("Invalid Marks")
                        break
                        
                except ValueError:
                    print("Please Enter mark between 0 and 100")
                    break
            
## Calculate the average and print the result.    
    Average = int(((one+two+three)/3).round(2))
    print(f"The student has and average of {Average}")
    if Average>= 80:
        print("Excellent")
    elif 50>=Average>=19:
        print("Pass")
    elif 0<=Average<=50:
        print("Fail")
    exit()