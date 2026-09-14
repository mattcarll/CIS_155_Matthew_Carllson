battery_percentage = int(input("Enter the battery level percentage (0-100): "))

if battery_percentage == 100:
    print("Battery fully charged. Unplug your charger.")
elif battery_percentage <= 20:
    print("Low battery! Switch to Power Saving Mode.")
else:
    print("Battery percentage is healthy.")
