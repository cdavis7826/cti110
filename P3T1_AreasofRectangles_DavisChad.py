# CTI-110
# Write a program that will show the area of rectangles
# Chad Davis
# 9/24/18
# Input the length and width of rectangle 1
# Input the length and width of rectangle 2
# Calculate the area of rectangle 1
# Calculate the area of rectangle 2
# "if" area1>area2 - Display that rectangle 1 has the greatest area
# "elif" area2>area1 - Display that rectangle 2 has the greatest area
# "else" - Display that both rectangles have the same area

# Get the dimensions of rectangle 1

print()
length1 = int(input('Enter the length of rectangle 1: '))
print()
width1 = int(input('Enter the width of rectangle 1: '))
print()

# Get the dimensions of rectangle 2
length2 = int(input('Enter the length of rectangle 2: '))
print()
width2 = int(input('Enter the width of rectangle 2: '))
print()
# Multiply length vs. width
Area1 = length1 * width1
Area2 = length2 * width2
print()
# Display which rectangle is larger or if they are the same size
if Area1 > Area2:
    print('Rectangle 1 is larger than rectangle 2.')         
elif Area1 < Area2:
    print('Rectangle 2 is larger than rectangle 1.')
else:
    print('Both rectangles are the same size.')

             
