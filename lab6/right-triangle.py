#Write a program that implments a function to calculate the hypotenuse of a right triangle using the Pathagorean Theorem c= sqrt(x^2 + y^2).
#You should prompt the user to enter values fro the two legs of the triangle(x and y) and pass the values to a user-definesd fucntion that calculates the hypotenuse(c)
#prints the resltant value to the console.
#Hint: import the math function using import math at the top of your program.

import math


def cal_hypotenuse(x, y):

    c = math.sqrt(x**2 + y**2)  

    print(f"The hypotenuse is: {c}")

    def main():
     
     return c

def main():

    x = float(input("Enter value of x: "))

    y = float(input("Enter value of y: "))

    c = cal_hypotenuse(x, y)

    
main()