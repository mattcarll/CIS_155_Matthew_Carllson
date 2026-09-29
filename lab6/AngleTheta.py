#Write a program that uses a funtion and the same right triangle from #3 above and
#calculate the angle theta for the right triangle.
#Print the results in degrees to the console.
#Hint: To calculate theta, use the folowing trigonometric function: atan2(y,x) and multiply
#the results by 180 / 3.14 to get the angle in degress.

import math

def cal_theta(x, y):

    theta = math.atan2(y, x)

    degrees = theta * 180 / 3.14

    return degrees

theta = cal_theta(x, y)

print(f"The angle theta is: {theta:.2f} degrees")

cal_theta(x, y)