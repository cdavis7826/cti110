# Write a program that shows a table that is showing a tuition increase of
# 3% every year for the next 5 years.
# 9/29/18
# CTI0110 P4HW3 - Tuition Increase
# Chad Davis
# (Psuedocode - Set the baseline tuition of $8000,
#  Set table headers,
#  Write "for" loop and set "range" for years,
#  Enter equation for tuition increase per year
#  Write code to show year with equivalent cost.)

# Tuition baseling
currentTuition = 8000
print()

# Headers for table
print('Year\t\tTuition Cost')

# "for" loop and "range"
for currentYear in range(1, 6):

# Equation for 3% increase per year
    currentTuition += (3/100) * currentTuition
    print(currentYear, '\t\t', '$', format(currentTuition, '.2f'))
