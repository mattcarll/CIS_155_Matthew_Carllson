# the program should implement a user-defined function named getMyList() 
# that does not take any arguments.
#The function should use the folowing list [10,20,30,40,50,60] in a for-loop and 
#print the loop variable for each loop iteration.
# Once the loop is complete, you should return the total number of loop iterations to the
#calling function and using the print() function, you should print the total to the concole

def getMyList():

    my_list = [10, 20, 30, 40, 50, 60]

    iterations = 0

    for item in my_list:

        print(item)

        iterations += 1

    print(iterations)
    
    return iterations


getMyList()
        