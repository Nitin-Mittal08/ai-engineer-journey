#print even numbers

def printEvenNumbers():
    n = int(input("Please enter your number:"))

    for i in range(1,n+1):
        if(i%2==0):
            print(i)
        else:
            continue


printEvenNumbers()
