#print multiplication table for n

def printMultiplicationTable():
    n = int(input("Please enter your number:"))

    for i in range(1,11):
        print(f"{n} X {i} = {n*i}")


printMultiplicationTable()