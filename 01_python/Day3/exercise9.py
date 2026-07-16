#print reverse stars

def printRevStarts():
    n = int(input("Please enter the number of rows:"))

    for i in range(1,n+1):
        for j in range(1,n-i+2):
            print("*" ,end='')
            j+=1
        print('')
        i+=1
    
printRevStarts()