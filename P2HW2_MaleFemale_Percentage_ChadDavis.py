# Female and Male Percentage Exercise
# 9/18/18
# CTI-110 P2HW2 - Male Female Percentage
# Chad Davis
# Pseudocode (input the male and female values, Calculate total number of s students, percentages of male and female students, display results)



print('\n')
# Value for males
males = int(input("Please enter the number of males in the class: "))

# Value for females
females = int(input("Please enter the number of females in the class: "))

# Value of males plus females
totalStudents = males + females
print('\n')
# Value of male percentage
malePercentage = (males/totalStudents) * 100

#Value of female percetage
femalePercentage = (females/totalStudents) * 100

# This is the total number of students in the class
print( "The total number of students in this class is: " + str(totalStudents))
print('\n')
# Calculated male percetage
print( "The percentage of males is: " + str(malePercentage) + "%")

# Calculated female percentage
print( "The percentage of females is: " + str(femalePercentage) + "%")
