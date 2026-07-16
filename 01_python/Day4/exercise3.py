#Check user

def checkUser():
    users = ["Nitin", "Rahul", "Ananya", "Priya", "Amit"]
    user = input("Please enter your name:")

    if user in users:
        print("User found")
    else:
        print("User not found")

checkUser()