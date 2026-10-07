#write a python program named monthsOfYear.py 
# that implements a function named months_of_year()
#  that takes two integer arguments startMonth and endMonth 
# that determines which months of the year you would 
# like to return(for example: to return
#  the first six months you would pass in 0,6 ). 
# The months of the year should be a list and 
#  you should prompt the user for the start and end months using
#  the input() function and then you should call the function
#  from the body of your program passing in the arguments.
#  The function should return the specified months on the year
#  based on the integer values you passed in. 
# Example of returned months when 0 and 6 are passed 
# ['Jan', 'Feb', 'March', 'April', 'May', 'June']

def months_of_year(startMonth, endMonth):

    months = ["jan", "feb", "mar", "apr", "may", 
              "jun", "jul", "aug", "sep", "oct",
              "nov", "dec"]

    return months[startMonth - 1:endMonth]

startMonth = int(input("starting month number: "))

endMonth = int(input("ending month number: "))

selected_months = months_of_year(startMonth, endMonth)

print(f'selected months are: {selected_months}')
