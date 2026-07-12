#Check the number

def checkNumber():
    num = int(input("Please enter your number:"))
    if(num>0):print("number is positive")
    elif(num<0):print("number is negative")
    else: print("number is zero")


checkNumber()