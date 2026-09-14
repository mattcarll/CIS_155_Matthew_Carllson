#create a program that will allow a user to enter an integer value between the range 0 and 100 using the input fuction in python.
# Your program should continue to prompt the user for values until a value is entered, such that it is outside of the specified range.
#When the range is breached , your program should print the following message to the console:
#"Sorry, the number you enetered is out of range!"
#Hint: ask yourself what type of. loop you need to accomplish this

while True:

    user = int(input(" Please enter a number between 0 and  100: "))

    if user < 0 or user > 100:

        print("Sorry, the number you entered is out of range!")

        break
