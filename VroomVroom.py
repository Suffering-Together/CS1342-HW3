"""
Author / s : Jesse Contreras, Damini Gopal
Serial Number: 22, 33

Due Date : March, 4th 2020
Assignment Number 3
Spring 2020 - CS 1342 - 251

Instructor: Husain Gholoom.
"""

print("""This program calculates and prints a parking fees for parking company
\nThis program is written by Jesse Contreras and Damini Gopal\n""")

#string (single character) value of the type of vehicle
#"C" or "c" = car, "B" or "b" = bus, "T" or "t" = truck
vehicle = str(input("""Enter Your Type of Vehicle:
\t C or c for Car5
\t B or b for Bus
\t T or t for Truck ):  """))

if (vehicle.upper() == "C"):
    print("car")
elif (vehicle.upper() == "B"):
    print("bus")
elif (vehicle.upper() == "T"):
    print("truck")
else: print("Invalid vehicle input")

hours = int(input("\nEnter Number of Hours Parked ( 1-23 ) : "))
minutes = int(input("\nEnter Number of Minutes Parked : "))




