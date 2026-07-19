#palindrome checker

def palindrome_checker():
    str = input("Please enter your string:").lower()
    rev_str = str[::-1].lower()

    if str == rev_str:
        return True
    else:
        return False

print(palindrome_checker())