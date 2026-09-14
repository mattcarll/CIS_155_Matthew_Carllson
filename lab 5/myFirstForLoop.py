# prompts the user to enter the number of iterations(e.g. loops) they want to do.
#  Then using a for-in loop,
#  your program should loop until the expected iterations are reached and print the value of each loop(e.g. the loop count). 

num = int(input("Enter the number of iterations: "))

for i in range(num):

    print("This is loop number:", i )