#reverse a string

string = input("Please enter your string:")
reverse_str = string[::-1]
print(reverse_str)

def reverse_string():
    str = input("Please enter the string:")
    reversedStr=''
    i = len(str)-1

    while i>=0:
        reversedStr = reversedStr + str[i]
        i-=1
    
    print(reversedStr)

reverse_string()


   
