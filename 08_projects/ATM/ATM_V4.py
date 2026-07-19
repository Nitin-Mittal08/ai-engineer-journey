# Building a simple ATM application


def show_menu():

    print("""Welcome to ATM

                1. Check Balance
                2. Deposit
                3. Withdraw
                4. Exit""")

    option = int(input("Please enter one of the options above:"))
    return option


def get_amount():
    amount = int(input("Please enter the amount:"))
    return amount

def print_balance(amount):
    print(f"Updated balance : {amount}")




def deposit(balance, amount):
    # global currentBalance

    if amount < 0:
        print("Invalid amount")
        return balance
    else:
        balance = balance + amount
        return balance


def withdraw(balance, amount):
    # global currentBalance
    if amount > balance:
        print("Insufficient Balance")
        return balance
    else:
        balance = balance - amount
        return balance


def atm_main():
    accounts = {"nitin": 10000, "rahul": 5000, "priya": 25000}
    name = input("Please enter your name:")
    if name in accounts:
        running = True
        # balance = accounts[name]
        while running:
            option = show_menu()

            if option == 1:
                print(f"Balance : {accounts[name]}")
            elif option == 2:
                amount = get_amount()
                accounts[name] = deposit(accounts[name], amount)
                print_balance(accounts[name])
            elif option == 3:
                amount = get_amount()
                accounts[name] = withdraw(accounts[name], amount)
                print_balance(accounts[name])
            elif option == 4:
                print("Thank you for using our ATM.")
                running = False
            else:
                print("Invalid option")
    else:
        print("Account not found")


atm_main()
