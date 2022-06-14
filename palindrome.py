

def palindrome(string):
    if len(string)<2:
        return True
    else:
        print(string[0], string[1:-1], string[-1])
        return  palindrome(string[1:-1])
        return string[0]==string[-1]
print("yes, It's a palindrome ")

palindrome('malayalam')