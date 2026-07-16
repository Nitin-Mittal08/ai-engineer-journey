#print name 10 times

def printName():
    name = input("Please enter your name:")
    i=0
    while(i<10):
        print(f"Hello {name}!")
        i+=1

printName()