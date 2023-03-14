import re

#The string below is commonly used in graphic design and publishing to
#temporarily fill in empty space. In this case it is very useful because
#it is a long, confusing set of words. It has many symbols, as well as upper and
#lower case characters. All the code I use would not be possible without the import
# re module above. All code that follows is an attempt to edit the string below.

Cicero = '''Lorem ipsum dolor sit-amet, consectetur adipiscing elit. Phasellus iaculis velit ac nunc interdum tempor. 
Ut volutpat elit metus, vel auctor enim commodo at. Nunc quis quam non ligula ultricies luctus porta id justo. 
Quisque dapibus est ut sagittis bibendum. Mauris ullamcorper pellentesque porttitor. Ut sit:amet ex nec dolor gravida 
porttitor. Proin at justo finibus justo vestibulum congue. Suspendisse et ipsum et ipsum eleifend dapibus a fermentum 
lacus. Vivamus porta nunc eu nisl sagittis, quis vulputate metus dignissim. Integer non fermentum nisl, id vestibulum 
elit. Sed euismod vestibulum purus ut porttitor. Integer sit-amet mollis neque. Donec sed lacinia diam, ac finibus 
lectus. Mauris tempor ipsum nisl, vitae posuere est lacinia nec. Nam eget euismod odio.'''

#First I made a variable that uses the caret ^ symbol within square brackets.
#This is important to mention because when the caret symbol is inside square
#brackets, it basically tells Python to exclude all the characters that follow (Regular Expressions).
#After I added all alphanumeric characters within the square brackets after the ^. 
#Next I created a results variable and put the re module to work. Typing re. 
#summons it, findall tells it to find all of the things I tell it to. Within
#Within the brackets is where I added the previous variable, as well as the string
#itself. Finally I ended with a simple print statement that prints the length (len)
#of the results variable.

#Regular Expressions. Retrieved June 14, 2020, from http://users.cs.cf.ac.uk/Dave.Marshall/Internet/NEWS/regexp.html

nonAlphanumeric = '[^a-zA-Z0-9]'
results = re.findall(nonAlphanumeric, Cicero)
print(len(results))

#The first thing I did here was add a variable called searchFor because I was
#asked to find all instances of sit amet with these symbols included (-:). The
#way to do that in Python is to first convert it to a string with '', then use square
#brackets inbetween the words (since that is the location we are looking for the
#symbols), and then place the symbols inside of those brackets. This tells Python
#to look for set amet as long as it has either - or : separating it.
#Next I created a howMany variable and summoned the re module. After re I put 
#Python to work and asked it to "findall" instances of the variable conditions
#I laid out earlier. I have to also specificy from which string so Cicero is
#in there as well. Lastly I printed the length of the string with the results of
#my howMany search.

searchFor = 'sit[-:]amet'
howMany = re.findall(searchFor, Cicero)
print(len(howMany))

#Much like before I created a variable called Old that highlights the words sit amet
#in the paragraph as long as the words have : or - inbetween them. Instead of going 
#through the paragraph myself and removing all of the instances of sit-amet and
#sit:amet, I can automate Python to do it. Next I created a variable called New
#that summons the re module and substitutes based on the conditions I set. First
#I placed the Old variable within the brackets so Python knows what to look for
#specifically. After I add in 'string' form what I want it to put in place of the
#old versions. Finally I show Python which string to search through by adding Cicero.
#If I were to just have this code:
#import re
#Old = 'sit[:-]amet'
#New = re.sub(Old, 'sit amet', Cicero)
#print(New)
#Then the paragraph above would print with the changes I made to sit amet. However,
#next I was asked to find out how many of those instances were changed. In order to
#do that I have to tell Python to re.findall. I already have a variable that 
#defines exactly what I'm looking for called Old, so I simply input that into a
#new variable called Search, as well as the paragraph variable itself. 
#To print the entire number correctly I have to use the len() function in the
#print statement, then print the Search variable.

Old = 'sit[:-]amet'
New = re.sub(Old, 'sit amet', Cicero)
Search = re.findall(Old, Cicero)
print(len(Search))
