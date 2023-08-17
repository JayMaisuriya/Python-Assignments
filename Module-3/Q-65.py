# Write a Python program to calculate surface volume and area of a cylinder.

import math

radius = float(input("Enter radius: "))
height = float(input("Enter height: "))
surface_area = 2 * math.pi * radius * (radius + height)
volume = math.pi * radius * radius * height
print("Surface area of cylinder:", surface_area)
print("Volume of cylinder:", volume)
