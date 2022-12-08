#!/usr/bin/env python3
# Created by: Lia Duggan
# Created on: Dec 8th, 2022
# This program rounds the number the user input
# to the decimal place the user wants it rounded to

def round_decimal(decimal_place, rounding_num ):

    # Pass by Reference
    Number_var = [rounding_num]
    Number_var.append(rounding_num)

    # Doing the math to round it to the decimal place the user wants
    ten_power = 10 ** decimal_place
    total = Number_var[0] * ten_power + 0.5 
    total= int(total)
    Number_var[0] = total / ten_power
    
    print(Number_var[0])

def main():
    # Getting the numbers from the user
    rounding_num = input("What number would you like rounded? ")
    decimal_place = input("How many decimal places do you want the number rounded to? ")

    # Making sure the user put valid input
    try:
        rounding_num = float(rounding_num)
        decimal_place = int(decimal_place)

        if decimal_place < 0:
            print("You can't round to negative decimal places")
        else:
            # Displaying the rounded number to the user
            print("{} rounded to {} decimal places is".format(rounding_num, decimal_place)) 
            round_decimal(decimal_place,rounding_num,)

    except ValueError:
          print("please enter a valid input")


if __name__ == "__main__":
    main()
