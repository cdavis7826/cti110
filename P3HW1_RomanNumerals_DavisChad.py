# Write a program that asks the user to enter a number between 1 and 10
# and show its roman numeral equivalent.

# CTI-110
# P3HW1 - Roman Numerals
# Chad Davis
# 9/24/18
# (Assign value to/for the number input by user (userNumber),
#  Assign Roman Numeral that is equal to number that user inputs,
#  Write "print" command to display the roman numeral that equals user input number,
#  Write error message if user number entered is greater than 10.)


# Enter number to be shown as a roman numeral.

userNumber = int(input('Please enter a number between 1 and 10 to get the Roman Numeral Equivalent: '))

# Enter values/code of number 1 through 10 and the roman numeral equivalent.
if userNumber == 1:
    print('Roman Numeral = I')
elif userNumber == 2:
    print('Roman Numeral = II')
elif userNumber == 3:
    print('Roman Numeral = III')
elif userNumber == 4:
    print('Roman Numeral = IV')
elif userNumber == 5:
    print('Roman Numeral = V')
elif userNumber == 6:
    print('Roman Numeral = VI')
elif userNumber == 7:
    print('Roman Numeral = VII')
elif userNumber == 8:
    print('Roman Numeral = VIII')
elif userNumber == 9:
    print('Roman Numeral = IX')
elif userNumber == 10:
    print('Roman Numeral = X')
# Error message if entered number is greater than 10.
else:
    print('Invalid number, please restart program and enter a number between 1 and 10.')

