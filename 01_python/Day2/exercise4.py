#check login credentials

def checkLoginCredentials():
    username = input("Please enter your username:")
    password = input("Please enter your password:")

    if(username=='admin' and password=='python123'): print("Login Successful")
    else: print("Invalid Credentials")


checkLoginCredentials()