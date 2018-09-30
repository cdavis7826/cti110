# Write a program that shows the Celsius temperatures and their Fahrenheit
# equivalents.
# 9/29/18
# CTI-110 P4HW2 - Celsius to Fahrenheit Table
# Chad Davis
# (Psuedocode - Enter values for the table headers,
#  Enter the "for" loop and "range" algorithms,
#  Enter the equation to calculate the conversion from Celsius to Fahrenheit.)




# ct = Celsius Temperature
# eft = Equivelant Fanrenheit Temperature

print()
# Enter table headers
print('Celsius Temperature\tFanrenheit Temperature')


# Enter alogrithm for "for" loop to show Celsius to Fahrenheit temperatures.
# ct = Celsius Temperature
for ct in range(21):
    
# eft = Equivelant Fanrenheit Temperature    
    eft = (9/5)*ct + 32
    print('\t',ct, '\t\t\t', format(eft, '.1f'))
    
    
