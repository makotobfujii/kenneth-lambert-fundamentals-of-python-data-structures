"""
Write a program that takes the radius of a sphere (a floating-point number) as 
input and outputs the sphere’s diameter, circumference, surface area, and volume.
"""
import math
def main():
    radius = float(input("Please input the radius of your sphere: "))

    diameter = radius * 2
    circumference = 2 * math.pi * radius
    surfaceArea = 4 * math.pi * radius ** 2
    volume = 4/3 * math.pi * radius ** 3

    print("Diameter:", diameter, "\nCircumference:", circumference, "\nSurface Area:", surfaceArea, "\nvolume:", volume)

if __name__ == "__main__":
    main() 