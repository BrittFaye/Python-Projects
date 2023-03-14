#Curly brackets tell Python that the data type is a {dictionary}.
shoppingCenterD = {}
#Square brackets tell Python I have created a [list]. I have now created an empty {dictionary} and [list].
shoppingCenterL = []    
#Next I created the stop variable using a boolean value. This is necessary in order to communicate with Python
#and let it know exactly when the while loop should end. This won't work unless I include the boolean in the loop code. 
stop = False    
#Here is where I started the while loop. It means that while stop does NOT equal q, continue iterating through the loop. 
#This sets a loop condition using the previously created Boolean data type.
#For each of the variables within the while loop, I ensured the user can input() their chosen food, cosmetic, etc., items. 
#The program will output for the end user what is inside the quotation marks, besides the \n, 
#which just takes the output to the next line. 
while stop != 'q':         
    element = input('Item name:\n')
    amount = input('Quantity purchased:\n')
    money = input('Price per item:\n') 
#Now that Python can communicate with the user, who can then input data, I must define the keys for that data in order to
#interact with the dictionary in a useful way.  
#The amount of things the customer buys will be an integer, hence the int().
#The price of the items will be a decimal value, hence the float().
#Since the label element will be typed and read as a string, that portion doesn't need anything extra.
    shoppingCenterD['label'] = element    
    shoppingCenterD['tally'] = int(amount)   
    shoppingCenterD['figure'] = float(money)    
#Here I appended (added) shoppingCenterD to the shoppingCenterL list. This command copies everything from the shoppingCenterD 
#dictionary to the shoppingCenterL list. The loop will continue until the 'q' condition is met (until the user enters q).
    shoppingCenterL.append(shoppingCenterD.copy())   
#This stop input allows the user to decide whether to continue or quit. The user decides when to stop the loop.
    stop = input("Would you like to enter another item?\nType 'c' for continue or 'q' to quit:\n")  
#Before starting the calculations, I had to set the addUpTo variable to 0. Otherwise the person using the program
#might get angry when they realize they have an extra charge that came from nowhere.
addUpTo = 0     
#This for loop says for the e(elements) in the shoppingCenterL list, do the following.
#First I created elementSum for the element's amount multiplied by the element's price.
#This calculation takes addUpTo (which starts at 0) and adds the elementSum to addUpTo for each loop.
#Python knows how to do this despite the lack of numbers in the block of code itself because
#of the list and dictionary. It pulls the 'tally' and 'figure' key that was created earlier.
for e in shoppingCenterL:    
  elementSum = e['tally'] * e['figure']   
  addUpTo += elementSum       
  #print('%d %s @ $%f ea $%f' % (item['number'], item['name'], item['price'], item_total))
#The % symbol is a placeholder. Since the first item is number, we use d to hold the place for a numeric or decimal value. %s means string.
#The spaces, @, ea, and $ are there so they are printed in the formatted string.
#To determine the decimal places, a period is used to say this is a (decimal), and a 2 to say to 2 decimal places (.2f).
#If I just put a placeholder and a float (f), like so (%f), Python defaults to 6 decimal places. I made an example print statement as a comment.
  print('%d %s @ $%.2f ea $%.2f' % (e['tally'], e['label'], e['figure'], elementSum)) 
#Set the elementSum to 0.
  elementSum = 0
#Another formatted string that gives the user a string to read, as well as the grand total formatted to 2 decimal places.
print('Grand Total: $%.2f' % addUpTo)  
  

