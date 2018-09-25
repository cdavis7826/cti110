# Write a program that will determine a customers shipiing charges.

# CTI-110 
# P3HW2 - Shipping Charges 
# Chad Davis 
# 9/24/18
# (Enter/print disclaimer,
# Write code for user to enter the weight of their package,
# Set values of prices per pound (weight * predetermind dollar amount,




print()
# Enter disclaimer
print(' *****Fast Freight Shipping Charges are Per Pound*****')

print()
# User enters the weight of their package
weight = int(input('Please enter your packages weight: '))

# Set values per pound/Print weight of package times predetermined dollar amount.
if weight <= 2:
    print('Your shipping charges will be $' + str(weight * 1.50))
elif weight >2 and weight <=6:
    print ('Your shipping charges with be $' + str(weight * 3.00))
elif weight >6 and weight <=10:
    print ('Your shipping charges with be $' + str(weight * 4.00))
elif weight >10:
    print ('Your shipping charges with be $' + str(weight * 4.75))
