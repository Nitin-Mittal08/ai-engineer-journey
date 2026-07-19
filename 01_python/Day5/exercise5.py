#word frequency

def get_word_frequency():
    str = input("Please enter your string:")

    list_of_words = str.split()

    dict_of_words = {}

    for word in list_of_words:
        if word in dict_of_words:
            dict_of_words[word]+=1
        else:
            dict_of_words[word] = 1
    
    print(dict_of_words)


get_word_frequency()
