# Correct/write student Grade Program- Lab
# CTI-110
# Chad Davis
# 9/24/18
# (Find and correct errors in code,
# Input missing code,
# Establish values for each letter grade,
# Set "score" value,
# Input responses for numerical grades,
# Test all strings.)

def main():
    # This program takes a number grade and outputs a letter grade.

    # system uses 10-point grading scale
    # Put in number to letter values

    A_score = 90
    B_score = 80
    C_score = 70
    D_score = 60

    # Define the "score" value
    print()
    score = int(input('Enter grade: '))

    # Input responses to number grades 

    if score >= A_score:
        print('Your grade is: A')
    elif score >= B_score:
        print('Your grade is: B')
    elif score >= C_score:
        print('Your grade is: C')
    elif score >= D_score:
        print('Your score is: D')
    else:
        print('Your grade is: F')

   #test test test     




# program start
main()
