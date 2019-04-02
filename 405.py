# Created by: Chris Asante
# Created on: 2-April-2019
# Created for: ICS3U
# Daily Assignment – Unit 4-05
# This application calculates the volume of a cylinder

from math import pi

def calculate(radius_input, height_input):

        answer = pi * radius_input ** 2 * height_input
        return answer

radius = int(input("Enter the radius of cylinder: "))
height = int(input("Enter the height of cylinder: "))

if radius < 0 or height < 0:
    print ("Enter a positive value for the height and radius  >:C")
else:

    show_volume = calculate(radius, height) 
    print("The volume of the cylinder is " + str('{:0.2f}'.format(show_volume)) + " units.")
