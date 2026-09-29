#write a program that implements a user-defined function named print_iterations() that accepts one integer argument named val.
#The function should loop over the val argument using a for-loop with a range and increment a local variable named loopCounter
#each iteration through the loop. After the for-loop is complete, 
#you should return the loop_Counter variable and print the following statement-> "The function call looped X times."
 
def print_iterations(val):

    loop_Counter = 0

    for x in range(val):
        loop_Counter = loop_Counter + 1

    return loop_Counter

val = int(input("Enter Number: "))

loop_Counter  = print_iterations(val)

print(" The Function called looped", loop_Counter, "times")