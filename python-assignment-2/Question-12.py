def checkpalindrome(string):
    reversestring= string[::-1]
    if string==reversestring:
        print("palindrome")
    else:
        print("Not palindrome")

if __name__=="__main__":
    checkpalindrome("aabbaa")
    checkpalindrome("reviver")
    checkpalindrome("palindrome")
