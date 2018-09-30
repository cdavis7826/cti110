# Write a program that that will show if you went over or stayed under your monthly of budget amount.
# 9/29/18
# CTI-110 P4HW1 - Budget Analysis
# Chad Davis
# (Psuedo Code - Enter algorithm to set the value of monthly budget (budgetAmount),
#  Enter algorithm to have "y" key loop to add more purchases,
#  Create loop so that additional purchases can be entered,
#  Set "if" command to define and show how much the user went over their set monthly budget,
#  Set "elif" command to show how much user stayed under their set monthly budget.)




# Enter algorithm to set the value of monthly budget (budgetAmount).

budgetAmount = float(input('Enter the amount you have budgeted for this month: '))

# Enter algorithm to have "y" key loop to add more purchases.
additionalPurchases = 'y'
totalSpent = 0

# Create loop so that additional purchases can be entered.
while additionalPurchases == 'y':
    purchaseAmount = float(input('Enter a purchase amount: '))
    totalSpent += purchaseAmount
    additionalPurchases = input('Did you make anymore purchases this month?: Type y for yes, press "Enter" for no: ')

# Set "if" command to define and show how much the user went over their set monthly budget.
if totalSpent > budgetAmount: 
    print('You went over this months budget of $', format(budgetAmount, ',.2f'),'by $',format(totalSpent - budgetAmount,',.2f'))
    
# Set "elif" command to show how much user stayed under their set monthly budget.
elif budgetAmount > totalSpent:
    print('You stayed under this months budget of $', format(budgetAmount, ',.2f'), 'by $',format(budgetAmount - totalSpent, ',.2f'))
