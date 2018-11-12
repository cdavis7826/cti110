# Write Code to convert user enter kilometers to miles.
# 10/28/18
# CTI-110 P5T1_KilometerConverter
# Chad Davis
#  Enter conversion factor of 0.6214,
#  Define kilometers
#  Enter conversion from (km) to (miles)



# Define "Conversion_Factor"
Conversion_Factor = 0.6214


def main():

    # Enter float for user input
    kilometers = float(input('Enter a distance in kilometers:'))

    show_miles(kilometers)



def show_miles(km):

    # Alogorithm for conversion from kilometers to miles.
    miles = km * Conversion_Factor

    # Print converted numbers
    print (km, 'kilometers equals', format(miles, '.2f'),'miles.')


main()
