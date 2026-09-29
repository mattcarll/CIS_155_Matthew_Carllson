#write a program that accepts a string input of at least 5 characters 
# from the console and create a function named isPalindrome(), 
# to determine if the entered string is a palindrome. 
# The function should return True if the string is a Palindrome 
# and False if the string is NOT a palindrome. 
# Use conditional logic and f-strings to print the result in the following 
# format if the string is a palindrome-> "The string xxxxx is a palindrome." 
# . If the string is NOT a palindrome, 
# then print the following-> "The string xxxxx is NOT a palindrome."

def Palindrome(word):

    if word == word[::-1]:

        return True

    else:

        return False

input = input("Enter a string with at least 5 characters:  ")

if len(input) >= 5:

    results = Palindrome(input)

    if results == True:

        print(f'The stirng {input} is a palindrome.')

    else:

        print(f'The string {input} is Not a palindrome.')

else:

    print("The word must be at least 5 characters long.")

