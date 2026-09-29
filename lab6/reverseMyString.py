#write a program that implements a user-defined function named reverseMyString(), 
# that accepts one arguments that is a string. 
# Your function should use the following syntax to reverse the string value passed into the function-> reversedWord = word[::-1]
#  and then using the print() function, you should print the reversedWord to the console.

def reverseMyString(word):

    reversedWord = word[::-1]

    print(reversedWord)

reverseMyString("word")