#Building a simple ATM application


def showMenu():
     
         print('''Welcome to ATM

                1. Check Balance
                2. Deposit
                3. Withdraw
                4. Exit''')
    
         option = int(input("Please enter one of the options above:"))
         return option
     
     



def deposit(balance,amount):
    #global currentBalance 
    
    if(amount<0):
        print("Invalid amount")
    else:
        balance = balance + amount
        return balance

def withdraw(balance,amount):
    #global currentBalance
    if(amount>balance):
        print("Insufficient Balance")
        return balance
    else:
        balance = balance - amount
        return balance





def atmMain():
    accounts = {
    "nitin": 10000,
    "rahul": 5000,
    "priya": 25000
}
    name = input("Please enter your name:")
    if name in accounts:
         running = True
         balance = accounts[name]
         while(running):

            option = showMenu()
            

            if(option==1):
               print(f"Balance : {balance}") 
            elif(option==2):
                amount = int(input("Please enter the amount:"))
                balance = deposit(balance,amount)
                print(f"Updated balance : {balance}") 
            elif(option==3):
                amount = int(input("Please enter the amount:"))
                balance = withdraw(balance,amount)  
                print(f"Updated balance : {balance}") 
            elif(option==4):
                print("Thank you for using our ATM.")
                running = False
            else: 
                print("Invalid option")
    else:
        print("Account not found")
    


atmMain()
