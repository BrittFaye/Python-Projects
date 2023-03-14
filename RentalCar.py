import sys
''

##Collect Customer Data - Part 1

rentalCode = input("(B)udget, (D)aily, or (W)eekly rental?\n") #Set rental code variable using =, and then allowing for user input using input().
if rentalCode == 'B' or rentalCode == 'D': #Began a conditional statement to allow for three different inputs. The == means equal to.
  rentalPeriod = int(input("Number of Days Rented:\n"))  #If the user enters B or D, the rentalPeriod will show the user "Number of Days Rented:" and then the integer they enter.
else:
  rentalPeriod = int(input("Number of Weeks Rented:\n"))  #If the user enters W, the rentalPeriod will show the user "Number of Weeks Rented:" and then the integer they enter.
#print(rentalCode)   #Commented out old print statements.
#print(rentalPeriod)

daysRented = rentalPeriod  #set daysRented variable.

#print('Number of Days Rented:')   #Commented out old print statements.
#rentalCode = 'D'      #Commented out old variable that allowed the previous program to run.
#print(rentalCode)

budgetCharge = 40.00    #Set charge variables, which are essential values for the math portion.
dailyCharge = 60.00
weeklyCharge = 190.00

##Collect Customer Data - Part 2

odoStart = input("Starting Odometer Reading:\n") #Set odometer variables. The user can input() their integer after seeing "Starting Odometer Reading:" on their screen.
odoEnd = input("Ending Odometer Reading:\n")    #Again, the string combined with an input allows a user to read whichever string I write, and then enter an answer.
totalMiles = int(odoEnd) - int(odoStart)    #Since the odometer's end value will be higher than the odometer's start value, the odoEnd must be subtracted from the odoStart. The int() tells Python that the output should and will be an integer.
#print(odoStart)     #Commented out old print statements that allowed this portion of code to test.
#print(odoEnd)
#print(totalMiles)

##Calculations
if rentalCode == 'B':     #This conditional statement tells Python that if B was previously entered as the rentalCode, do the following:
  baseCharge = rentalPeriod * budgetCharge      #Set a new value (baseCharge) that multiplies the rentalPeriod by the budgetCharge if the rentalCode is B.
elif rentalCode == 'D':     #This conditional statement tells Python that if D was entered as the rentalCode, do the following:
  baseCharge = rentalPeriod * dailyCharge #If D is the rentalCode, the baseCharge variable will multiply the rentalPeriod by the dailyCharge, which looks like this: baseCharge = 5 * 60.00 (300)
else:
  baseCharge = rentalPeriod * weeklyCharge   #The else statement is used instead of writing rentalCode == 'W' because it is now the only option left, which Python can figure out on its own. If W, the rentalPeriod is multiplied by the weeklyCharge.
#print("{0:.2f}".format(baseCharge))    #Commented out old formatted print statement.

if rentalCode == 'B':   #This conditional statement goes into more detail when concering the calculations. If B is the rentalCode chosen, then:
  mileCharge = totalMiles * 0.25  #The mileCharge variable will be the totalMiles multiplied by 0.25. totalMiles(2222-1234) * 0.25 = mileCharge(247)

if rentalCode == 'D':   #If the rentalCode entered is D, then this is the calculation Python will execute:
  averageDayMiles = totalMiles/rentalPeriod    #The averageDayMiles variable will divide totalMiles by the rentalPeriod. In this case it is 988/5 = 197.6

  if averageDayMiles <= 100:   #This nested if statement applies to the if statement above, but cannot be executed until the previous calculation is done. If the previous calculation for averageDayMiles is less than 100, then:
    mileCharge = 0       #The mileCharge is 0.   
  elif averageDayMiles > 100:      #Else if the averageDayMiles calculation is greater than 100 then:       
    extraMiles = averageDayMiles - 100   #An extraMiles variable is created to subtract 100 from averageDayMiles, like so: 197.6 - 100 = 97.6
    mileCharge = extraMiles * 0.25       #The mileCharge variable (instead of just being 0) multiplies the extraMiles by 0.25. It looks like this: 97.6 * 0.25 = 24.4
  
if rentalCode =='W':     #If rentalCode is equal to W then:
  averageWeekMiles = totalMiles/rentalPeriod   #The averageWeekMiles variable will divide totalMiles by the rentalPeriod.

  if averageWeekMiles <= 900:   #Once the totalMiles and rental period have been divided, Python must determine if the quotient is less than or greater than 900.
      mileCharge = 0   #If it is less than 900, mileCharge is 0.
  elif averageWeekMiles > 900:   #If it is greater than 900, mileCharge is the rentalPeriod divided by 100.00.
      mileCharge = rentalPeriod * 100.00

#print("{0:.2f}".format(mileCharge))

amtDue = baseCharge + mileCharge    #The amtDue variable is set for all conditional statements, which is the baseCharge plus the mileCharge: 300 + 24.4 = 324.4

print('Rental Summary')    #All print statments are placed at the end so they are easy to find and read. Well organized code is better than confusing code!
print('Rental Code: ' + str(rentalCode))      #Most of the print satements require the combination of a string and a defined variable, hence the + and str().
print('Rental Period: ' + str(rentalPeriod))
print('Starting Odometer: ' + str(odoStart))
print('Ending Odometer: ' + str(odoEnd))
print('Miles Driven: ' + str(totalMiles))
print('Amount Due: ' + '${:,.2f}'.format(amtDue))  #{:,.2f} "Format float 2 decimal places" (M, 2020). 

#M. (2020, May 13). Python String Format Cookbook. Retrieved May 21, 2020, from https://mkaz.blog/code/python-string-format-cookbook/