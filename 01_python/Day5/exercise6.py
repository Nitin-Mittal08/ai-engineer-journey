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
    
    new_dict = dict(sorted(dict_of_words.items(),key=lambda item: item[1],reverse=True))
    print(new_dict)


get_word_frequency()
