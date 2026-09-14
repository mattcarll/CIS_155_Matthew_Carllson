#enter up to 10 grades that are integer values.
# You should prompt the user to enter the number of grades they want and then prompt the user for the respective grades.
# After each grade has been entered, you should print the grade to the console. 
# After all grades have been entered, you should print "The user has entered "X" grades and is now done". 
# Hint: X is the value you entered for the total number of grades and you should use a While-loop to accomplish this.

x = int(input("Enter the number of grades (up to 10): "))

if x > 10:

    print("You can only enter up to 10 grades.")

else:

    count = 0

    while count < x:

        grade = int(input("Enter grade: "))

        print("You entered:", grade)

        count += 1

    print("The user has entered", x, "grades and is now done.")

