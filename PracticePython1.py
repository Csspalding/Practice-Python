# -*- coding: utf-8 - Derick Benas tutorial Python in one session plus notes*-
"""
Created on Thu Aug 23 16:08:49 2018

@author: Cas
"""

import os
import random #random number generator
import sys # system

print ("hello world")
name = "Cas"
print (name)
quote = "\"Always remember you are unique\""
quote2 = '"Always remember to use the right brackets"'
multi_line_quote = '''just like everyone
else'''

print("%s %s %s" % ( 'I like the quote:-', quote, multi_line_quote))
print ("I don't like ", end="")# gets rid of the newline at the end of this printline
print ("newlines") 

print ("\n"* 5)#prints 5 new lines

#list
grocery_list = ['Juice', 'Tomatoes', 'Potatoes', 'Bananas']
print (grocery_list)
print (grocery_list, end="")
print('First Item =', grocery_list[0])
#change the value of the first item
grocery_list[0] = 'Green Juice'
print('First Item =', grocery_list[0])
print ("\n" *5)
#list of lists

other_events = ['Wash Car', 'make jam', 'pick up kids','cash cheque']

to_do_list = [other_events, grocery_list]

print(to_do_list)

print ((to_do_list[1][1]))# second list, second item is tomatoes
print ((to_do_list[0][2]))# prints pick up kids

grocery_list.append('Onions')
print(to_do_list)

grocery_list.insert(1,"Pickle")#inserts as item 2
#grocery_list.remove("Pickle") # search for and remove an item - Error message if it's not there??

#NOTE YOU MUST CALL THE FUNCTION, THEN PRINT IT OUT, IT DOES NOT WORK print (grocery_list.sort())
grocery_list.sort()# sorts list (how alphabetically?? what if there are numbers??)
print('sorted list: ', grocery_list)# here note the comma ',' for adding the list to the string  NOT A '+' IN A PRINT FUNCTION
print ('\n')

grocery_list.reverse()# reverses the sorted list ?? check what this does
print ('Reversed list:' , grocery_list)
del grocery_list[4] #delete item 4 
print ('\n')


print(to_do_list)#shows all the changes I made

xmas_list = ['Write cards', 'Wrap gifts', 'Plan food']
to_do_list2 = xmas_list + grocery_list

print(len(to_do_list2))
print(max(to_do_list))#max alphabetically lexidecimal
print(min(to_do_list))#min alphabetically


#tuples, unlike lists, we cannot change it after it is created, useful for data you do not want to change
#(if you did want to change it you could change it to a list then back to a tuple.)

pi_tuple = (3,1,4,1,5,9)
new_tuple = list(pi_tuple)# now it's a list
#make all the changes then
new_tuple = tuple(new_tuple)#changes the list back to a tuple
len(new_tuple)
min(new_tuple)
max(new_tuple)

#Dictionaries or maps
#have a unique key for each value ,but you cannot join dictionaries with + sign like you can lists
#dictionary name  = { key : value}
super_villans = {'Fiddler' : 'Isaac Bowin','Captain Cold' : 'Leonard Smart','Weather Wizard' : 'Sam Scudder','Pied Piper' : 'Thomas Peterson'}
for realName in super_villans:
    print(realName) #prints key
    print("super villan %s" % super_villans[realName])#prints value
    print(realName + ":"+ super_villans[realName])# prints key then value
 
knights = {'Gallahad': 'pure of heart', 'Robin Hood' : 'the brave'}
for v, k in knights.items():
    print(v, k)
    print(k, v) 
    
print (super_villans["Captain Cold"])# prints the value for this key
del super_villans['Fiddler']#delete an entry
super_villans['Pied Piper'] = 'Hartley Rathaway' #replaces the item/value for this key
print(len(super_villans))# prints length or number of items
print(super_villans.get("Pied Piper"))# prints item/value for this key
print(super_villans.keys())#prints a list of all the keys
print(super_villans.values())# prints a list of all the dictionary values

#Scrabble game, function to search for a word in the score dictionary to return a score
score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}
         
def scrabble_score(word):
  word = word.lower()
  total = 0
  for letter in word:
    for leter in score:
      if letter == leter:
        total = total + score[leter]
  return total

#order of operation matters in arithmetic BODMAS
numberOne = 5
numberTwo = 2
squaredNum = numberOne ** numberTwo #should print 25
print (squaredNum)
floorDivision = squaredNum // numberTwo 
print (floorDivision) # should print 5?? but prints 12??
numberThree = 9 
floorDivision  = numberThree // 3 #9//2 prints 3 as expected
print (floorDivision) 
print(125//3) #should print 5??  prints41??


#modulo


#comparision condition operators are 'if else elif == != > >= < <= '
# if executes code if a condition is met
#white space indentation is used to group blocks of code in python, 
#else executes code if condition is not met
#elif used if you want to check for multipule conditions "else if"
age = 22

if age < 16 :
    print ('not old enough to drive!')
else :
    print ('you are old enough to drive')
    
if age >= 21 :
    print ('Old enough for tractor or bus')
elif age >= 17:
    print ('Old enough to drive')
else : print ('Not old enough to drive!')

#logical operators 'and, or, not'  
# 
age = 30
# once the condition is met, it will not go on checking anything else, simple rule to remember
if ((age >=1)and (age<= 18)):  #only met if age is = to 1 or 18
    print ("you get a birthday")
elif (age == 21 ) or (age >= 65):
    print ('You get a birthday too')
elif not(age == 30): # not will change this true to a false
    print ('You don\'t get a birthday')
else :
    print ('You get a party, hey yeah yippee!')


#looping , perform an action a set number of times
for x in range(0,10):# will print 0-9 the loop happens ten times
    print(x, ' ', end="") # prints all on one line

print ('\n')


#loop through a list
for y in grocery_list:
    print(y)


for x in [2,4,6,8,10]:
    print(x)

num_list = [[1,2,3], [10,20,30],[100,200,300]]

for x in range(0,3):
    for y in range (0,3):
        print (num_list[x][y]) # prints out all the values in num_list ??? not sure how this works!!


# while loop, for when you don't know how many times you need to go through a loop

random_num = random.randrange(1,100) # gives a random number btwn 0-99

#this prints a list of random numbers until the condition is met i.e. random_num is 15
while (random_num != 15):
    print (random_num)
    random_num = random.randrange(0,100)

i = 0 

print ('\n')


while (i <= 20):
    if (i % 2 == 0):# even number
        print (i)
    elif (i == 9):# stop when you get to 9 and break out of the loop. 
        break
    else :
         i += 1 # i = i+1 increment by 1
         continue
    
    i += 1 #increment i again

#Functions

#def addNumber():
menu = ["pizza", "fishcakes", "lamb curry", "fish /'n/' chips","salmon & salad" ]
for index, item in enumerate(menu):# for int index, str item in enumerate(menu)you don't need to put in the type but it's useful to be aware of the syntax
    print (index,item) 