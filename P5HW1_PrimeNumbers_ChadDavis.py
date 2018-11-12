# Write a program that will tell if the user entered number
# is or is not a prime number.
# 11/10/18
# CTI-110 P5HW1 - Prime Numbers
# Chad Davis
# (Define parameters for baseline of what is and isn't a prime number,
#  define what "userNumber" is
#  use if/else along with print statements to display if the user
#  entered number is in fact prime or not prime.)



def isPrime(beginningNumber):
    evenDivide = 0
    if beginningNumber <= 1:
        return False
    for enteredNumber in range(1, beginningNumber + 1):
        if beginningNumber % enteredNumber == 0:
            evenDivide = evenDivide + 1
            if evenDivide > 2:
                return False
    return True

def main():
    userNumber = int(input('Enter a number:'))
    print()
    if isPrime(userNumber):
        print('The number', userNumber, 'IS a prime number.')
    else:
        print('The number', userNumber, 'IS NOT a prime number.')

main()    
    
    
