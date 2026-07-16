#Ask five numbers

def askNumbers():
    numList=[]
    for i in range(1,6):
        numList.append(int(input(f"Please enter the {i} number:")))

    print(f"List:{numList}")
    numList.sort(reverse=True)
    print(f"Largest number:{numList[0]}")
    print(f"Smallest number:{numList[len(numList)-1]}")
    total=0
    for num in numList:
        total+=num
    print(f"Sum:{total}")
    print(f"Average:{total/len(numList)}")


askNumbers()




