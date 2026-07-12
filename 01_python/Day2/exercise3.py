#provide gradings

def provideGrade():
    marks = int(input("Please enter your marks:"))

    if(marks>=90):print("Your grade is A")
    elif(marks>=75):print("Your grade is B")
    elif(marks>=60):print("Your grade is C")
    elif(marks>=40):print("Your grade is D")
    else:print("You failed")

provideGrade()

