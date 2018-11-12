# Write a program that let's the user play
# "Rock, Paper, Scissors" against the computer.
# 11/11/2018
# CTI-110 P5HW2 - Rock, Paper, Scissors Game
# Chad Davis
#
# (import the random function and define range, define if/elif for rock, paper, scissors.
#  print command for user to imput data,
#  define messages for outcomes of computer and user selections,
#  enter if/elif statements to define what messages to display for user and computer selections
#  enter main and restart algorithm to create a loop in case of computer and user selectiong same
#  options. Test)


import random

def randomPickGenerator():
    randomPick = random.randint(1, 3)
    return randomPick

def getComputerChoice(randomPick):
    if randomPick == 1:
        computerChoice = 'rock'
    elif randomPick == 2:
        computerChoice = 'paper'
    elif randomPick == 3:
        computerChoice = 'scissors'
    return computerChoice


print('Lets play a game of Rock, Paper, Scissors!')
def getUserChoice():
    userChoice = input('\nPlease enter one of the following, rock, paper or scissors:')
    return userChoice

def winnerWinner(computerChoice, userChoice):

    rockWinner = 'rock smashes scissors'
    scissorsWinner = 'scissors cut paper'
    paperWinner = 'paper wraps rock'
    winner = 'no one wins'
    message = ()

    if computerChoice == 'rock' and userChoice == 'scissors':
        winner = '\nThe computer'
        message = rockWinner
    elif computerChoice == 'scissors' and userChoice == 'rock':
        winner = '\nYou'
        message = rockWinner

    if computerChoice == 'scissors' and userChoice == 'paper':
        winner = '\nThe computer'
        message = scissorsWinner
    elif computerChoice == 'paper' and userChoice == 'scissors':
        winner = '\nYou'
        message = scissorsWinner

    if computerChoice == 'paper' and userChoice == 'rock':
        winner = '\nThe computer'
        message = paperWinner
    elif computerChoice == 'rock' and userChoice == 'paper':
        winner = '\nYou'
        message = paperWinner

    return winner, message


def reStart():
    randomPick = randomPickGenerator()
    computerPick = getComputerChoice(randomPick)
    userChoice = getUserChoice()

    print('\nThe computer picked', computerPick)
    winner, message = winnerWinner(computerPick, userChoice)

    if winner != 'no one wins':
        print (winner, 'won because',message)
    return winner

        
def main():
    
    randomPick = randomPickGenerator()
    computerPick = getComputerChoice(randomPick)
    userChoice = getUserChoice()
    
    print('The computer picked', computerPick)
    winner, message = winnerWinner(computerPick, userChoice)

    if winner != 'no one wins':
        print (winner, 'won because', message)

    while winner ==  'no one wins':
        print('\nIt is a draw, you and the computer made the same choice, please try again.')
        winner = reStart()

main()

        
