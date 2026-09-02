Your_Grade = float(input("Enter your grade (0-100): ")) 

if Your_Grade >= 90:

    print("You got an A! You Passed The Class!")
elif Your_Grade >= 80:

    print("You got a B! You Passed The Class!")
elif Your_Grade >= 70:

    print("You got a C! You Passed The Class!")
elif Your_Grade >= 60:

    print("You got a D! You Passed The Class!")
elif Your_Grade <= 59:

    print("You got an F! You Failed The Class!")
else:
    
    print("Invalid grade. Please enter a grade between 0 and 100.")