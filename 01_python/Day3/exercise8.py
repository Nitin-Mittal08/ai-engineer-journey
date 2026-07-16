#print stars

def printStars():
    n = int(input("Please enter the number of rows of stars:"))

    for i in range(1,n+1):
        for j in range(1,i+1):
            print("*", end='')
            j+=1
        print('')
        i+=1


printStars()
