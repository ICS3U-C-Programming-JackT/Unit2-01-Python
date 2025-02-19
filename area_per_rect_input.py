#!/usr/bin/env python3
# Created By: Jack Turcotte
# Date: February 19, 2025
# This program calculates the area and perimeter of a rectangle based on user input

import math


def main():
    length = float(input("Enter length of the rectangle (mm): "))
    width = float(input("Enter width of the rectangle (mm): "))
    print("The area of your rectangle is " + str(length * width) + "mm^2")


if __name__ == "__main__":
    main()
