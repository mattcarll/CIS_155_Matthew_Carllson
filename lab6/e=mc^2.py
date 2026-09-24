# Write a program that calculates energy in Joules from a given mass using
# the formula E = mc^2, where c = 2.99 * 10^8 m/s.
# The program allows the user to enter the mass as a floating-point value.
#Your program should use a function named calculate_energy() that accepts one argument(mass),
#and from the mass, you should calculate the energy produced and return the calculated value after calling the function. 
# Print the result as: "The energy produced is: xxx.xx Joules".

def calculate_energy(mass):

    c = 2.99 * 10**8

    return mass * c**2


mass = float(input("Enter the mass in kilograms: "))

energy = calculate_energy(mass)

print(f"The energy produced is: {energy:.2f} Joules")
    