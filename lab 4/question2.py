num1 = int(input("Enter the first number: "))

num2 = int(input("Enter the second number: "))

result = num1 - num2

print("The result is:", result)

if result < 0: 
    print("###################################")
    print( "Invalid! The Value Is Less Than 0")
    print("###################################")

else:

    print("The Value entered were valid integers.")