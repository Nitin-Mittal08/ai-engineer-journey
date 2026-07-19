#Capitalize every word

string = input("Please enter your string:")
new_string = string.title()
print(new_string)

def capitalize_words():

    str = input("Please enter your string:")

    list_of_word = str.split(" ")

    new_str = ""

    for word in list_of_word:
        word = word[0].upper() + word[1:]
        new_str = new_str + " " + word

    print(new_str)

capitalize_words()
