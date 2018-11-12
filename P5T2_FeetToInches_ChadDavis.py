#  Write code that will take user information in feet and convert to inches.
#  11/7/18
#  CTI-110 P5T2_FeetToInches
#  Chad Davis
#  (Set variable for inches per foot.
#   Enter code to receive user information,
#   Print conversion of feet to inches,
#   Define function of feet * inches.)







# Defining inches per foot.
Inches_Per_Foot = 12


def main():
    # User inputs information.
    feet = int(input('Enter a number of feet:'))

    # Displays converted answer.
    print (feet, 'feet equals',feet_to_inches(feet), 'inches.')

# Conversion of feet to inches.
def feet_to_inches(feet):
    return feet * Inches_Per_Foot

main()
