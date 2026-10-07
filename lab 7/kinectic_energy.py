# write a python program named kinetic_energy.py. You should implement a function named kinetic_energy(mass,velocity)
#  that accepts an object’s mass (in kilograms) and velocity (in meters per second) as arguments. 
# The function should return the amount of kinetic energy that the object has. 
# Using the input() function the program should ask the user to enter values for mass and velocity, 
# then you should call the kinetic_energy() function to get the object’s kinetic energy and using f-strings, 
# you should print the resultant value to the console with the correct units.


def kinetic_energy(mass, velocity):

    energy = 0.5 * mass * velocity ** 2

    return energy

mass = float(input( " enter the mass in kg:  "))

velocity = float(input( " eneter velocity in m/s: "))

energy = kinetic_energy(mass, velocity)

print(f"Object's kinetic energy is: {energy: .2f} joules")