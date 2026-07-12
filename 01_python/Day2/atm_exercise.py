#Building a simple ATM application

def displayATMMenu():
    currentBalance = 10000
    print('''Welcome to ATM

                1. Check Balance
                2. Deposit
                3. Withdraw
                4. Exit''')
    
    option = int(input("Please enter one of the options above:"))

    if(option==1):
        print(f"Current Balance : {currentBalance}")
    elif(option==2):
        deposit = int(input("Please enter the amount:"))
        print(f"Updated Balance : {currentBalance+deposit}")
    elif(option==3):
        withdrawl = int(input("Please enter the amount:"))
        if(withdrawl>currentBalance):print("Invalid amount, low balance!")
        else:print(f"Updated balance : {currentBalance - withdrawl}")
    elif(option==4):
        print("Thank you for using our ATM.")
    else: print("Invalid option")

displayATMMenu()
