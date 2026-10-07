# Design and write a python program named max_value.py that implements function named max() that accepts two
#integer values as arguments and returns the value that is the greater of the two. For example, if 7 and 12
#are passed as arguments to the function, the function should return 12. You should use what you have learned
# about if-else conditions to apply the logic necessary. You should use the input() function in the program and prompt 
# the user to enter the two integer values. After the user has enetered the values, you should call the max() function 
# print the return value after it has been called.

def max(value1, value2):

    value1 = 7

    value2 = 12

    if value1 >= value2:

        return value1
    
    else:

        return value2

results = max(7, 12)

print(results)