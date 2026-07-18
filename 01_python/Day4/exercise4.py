# remove even


def removeEven():
    numList = [2, 5, 8, 11, 14, 17, 20]
    newList = [num for num in numList if num % 2 != 0]
    print(newList)

    """for num in numList:
        if num%2==0:
            numList.remove(num)
        else:
            pass
    print(numList)"""


removeEven()
