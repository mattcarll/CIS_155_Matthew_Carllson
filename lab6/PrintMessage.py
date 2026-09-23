#write a python program that implements two functions named print_message1() and print_message2().
# You should call the print_message1() function first, and then call the print_message2() function from the body of the program and
#print_message1() should in-turn call print_message2().
#The print_message1() function should print the message "I was called first" 
#and the print_message2() function should print "I was called from print_message1()".
#Both functions should rerturn void and print their respective messages to the console.

def print_message1():

    print(" I was called first")

    print_message2()

    return

def print_message2():

    print(" I was called from print_message1()")

    return

print_message1()