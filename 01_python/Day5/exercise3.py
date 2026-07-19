#Count vowels

def count_vowels():
    str = input("Please enter your string:").lower()
    vowels = ["a","e","i","o","u"]
    count = 0

    for i in str:
        if(i in vowels):
            count+=1
        else:
            pass
    print(count)

count_vowels()