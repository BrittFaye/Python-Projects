import sys
#The checking starting amount is set to 500.25 using a set variable. Basically I told 
#Python what I want my starting bank amount to be.
checking = float(500.25)
#When the customer interacts with the ATM program, they must be able to tell Python what to do. 
#An answer variable is set with an input() in order for that to happen. 
#The first thing the banking customer sees is, "What would you like to do?"
answer = input("What would you like to do?\n")
#In order for each function to work, I must be able to change the customer's given answer.
#If this program was in the real world, this variable would not need to be updated in this way.
answer = 'W'
#For the amount of money put into the checking account, I made a specific function; a checkingD 
#variable was needed for the calculations to work.
checkingD = 200
#For the money taken out of the checking account, I made another funciton; a checkingW 
#variable was needed for the calculations to work.
#If this program was real, the bank's customer would enter these amounts themselves.
checkingW = 100
#The def keyword is how to tell Python you are creating a function, in the same way 
#= tells Python you are creating a variable.
#Writing def creates a function and what is typed afterward, in this case checkingB, is the name.
#This is a function now named checkingB. The function first outputs a string, 
#then it outputs the account_balance variable. That is what this function returns each
#time it is called. If I wanted to, I could cut out one of those print statements; however,
#since the function is so simple and small, this way removes the need for formatting.
def checkingB():
  print('Your current balance:\n')
  print(checking)
#This function is named checkingD and is only run if the customer selects D. 
#First the user is asked to enter a number for the money they want to put in. The float portion ensures Python
#understands the number can and should be a float, since it is a currency.
#Next the checking must be added to the input float: 500.25 + 200.00 = 700.25. In this case the customer put in $200.00. 
#Just like the % formatting, {}.format acts as a placeholder for the variables added at the end (PyFormat).
#Adding the : tells Python we are making visual adjustments, in this case making the float only go to 2 decimal places.
#This is the new Python 3 formatting method: .format(). The variables I want to insert into the formatted string
#are added at the end after .format. They are inserted into the placeholders {} at only :.2f decimal places.
def checkingD():
  responseD = float(input('How much would you like to deposit today?\n'))
  updated = checking + responseD
  print('Deposit was ${:.2f}, current balance is ${:.2f}'.format(responseD, updated)) 
#This function is named checkingW and is only called if the user selects W, thanks to the conditional statement below.
#The first thing this function is asked to do is receive the user's input in float form. 
#The second thing this function does is determine whether the checking is less than the money the customer wants to take out.
#Obviously this would be a problem in the real world, so it only makes sense for the bank to inform the customer.
#If the money removed is more than the amount of money in checking, the user will see this: 
#"1000.00 is greater than your account balance of 700.25."
#If the customer wants to take out less money than the checking account has total (which is the case here), the customer will see
#"Withdrawal amount was 100.00, current balance is 600.25."" The reason these floats look so clean is, again, because of the
#new .format() method. Without formatting the string, the customer would receive a much larger float.
def checkingW():
  responseW = float(input('How much would you like to withdraw today?\n'))
  if checking < responseW:
    print('${:.2f} is greater than your account balance of ${:.2f}'.format(responseW, checking))
  else:
    newB = checking - responseW
    print('Withdrawal amount was ${:.2f}, current balance is ${:.2f}'.format(responseW, newB))
#None of the above functions would work without this conditional statement. If it was removed entirely,
#the program would not know which function to run. In fact, the only thing that prints if the
#conditional statement is removed is the first question, "What would you like to do?"
#This is because Python cannot choose which function to run without instructions.
#The conditional statement guides the program by saying what to do if B, D, W or Q are selected.
if answer == 'B':
  checkingB()
elif answer == 'D':
  checkingD()
elif answer == 'W':
  checkingW()
else:
  print('Thank you for banking with us.')
  
  








