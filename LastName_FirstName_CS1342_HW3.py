"""
Author / s : Jesse Contreras, Damini Gopal
Serial Number: 22, 33
Due Date : March, 4th 2020
Assignment Number 3
Spring 2020 - CS 1342 - 251
Instructor: Husain Gholoom.

This program calculates and prints parking fees for a parking company
"""

import sys


vehicle = ""    #string (single character) value of the type of vehicle
                #input: "C" or "c" = car, "B" or "b" = bus, "T" or "t" = truck

hours = 0       #integer value of the amount of hours parked in lot
                #input: must be in range 1-23

minutes = 0     #integer value of the amount of remainder minutes parked in lot
                #input: must be in range 1-60

tot_hours = 0.0 #float value giving total time parked in hours factoring in minutes

fee = 0.0       #float value that is eqaul to the total amount charged for parking duriation

import math

def endProgram():
    print("\n\nProgram is implement by Jesse Contreras and Damini Gopal\n3-4-20")
    sys.exit()
    
def showTotal():
    math.floor(fee)          
    print("\nYour car has been parked for", hours, "hours and", minutes,"minutes")
    print("\nAmount Due  =  $", int(fee),".00")
    endProgram()
    
print("""This program calculates and prints a parking fees for parking company
\nThis program is written by Jesse Contreras and Damini Gopal\n""")

vehicle = input("""Enter Your Type of Vehicle:
\t C or c for Car
\t B or b for Bus
\t T or t for Truck ):  """)           

if (vehicle.upper() not in {"C", "B", "T"}):
    print("\n",vehicle,"is an invalid vehicle type")
    endProgram()

hours = int(input("\nEnter Number of Hours Parked ( 1-23 ) : "))
if (hours not in range(1,24)):
    print("\n",hours, "is an Invalid number of hours parked")
    endProgram()

minutes = int(input("\nEnter Number of Minutes Parked : "))
if (minutes not in range(1,60)):
    print("\n",minutes, "is an Invalid number of minutes parked")
    endProgram()

tot_hours = hours + minutes/60        

if (vehicle.upper() == "C"):
    if (tot_hours <=2): fee = math.floor(tot_hours)
    else: fee = 2 + (math.floor(tot_hours)-2)*1.75
elif (vehicle.upper() == "B"):
    if (tot_hours <=2): fee = 3*math.floor(tot_hours)
    else: fee = 6 + (math.floor(tot_hours)-2)*3.25
elif (vehicle.upper() == "T"):
    if (tot_hours <=2): fee = 2*math.floor(tot_hours)
    else: fee = 4 + (math.floor(tot_hours)-2)*2.75

showTotal()
