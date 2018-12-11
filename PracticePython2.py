# -*- Sept 17th 2018 Python Programming Practice second half YouTube tutorial Derek Banas 
#author Cass

import random
import sys
import os

#functions
def addNumber(fNum,lNum):
    sumNum = fNum + lNum
    return print(sumNum)

fNum = 5
lNum = 4
addNumber(fNum, lNum)

print(addNumber(15,15))

#input from user sys

print("What is your name")

name = sys.stdin.readline() # BUT if I use this it does not wait for input, it runs the next line of code with no input!
name = input() # this is my solution instead, and it works fine

print("You said your name was " + name + " is that right?")

#Strings and printing parts of the string

quote = "to be or not to be that is the question" # a long string made up of 10 short strings

print (quote[0:1])# this prints the first character t (characters from 0 - 1 but not including 1)

print (quote[0:12])# this prints the first 12 characters counting white spaces too

print (quote[-5:]) #prints the last 5 characters

print (quote[:-5]) #does the opp so prints everything APPART FROM THE LAST 5 characters    

print (quote[:2] + " have understanding")# prints the first 2 plus 

print ("%c is my %s letter and my favourite number is %d number, and my favourite fraction is is %.5f" % ('X', 'favourite', 1, .3333333))

print (quote.capitalize() + '\n')

upperString = "THIS STRING IS IN UPPER CASE"

print (str.lower(upperString))

print(upperString)

print (upperString.find("UPPER"))

print(upperString.isalpha())

print (len(upperString))

print (upperString.replace("UPPER", "LOWER"))
#Stripping a string
whiteSpaceString = "    this string has lots of white space at the begining and the end    "
print(whiteSpaceString.strip())# strips all the white space at the begining and the end of the string

str = "*****this is string example....wow!!!*****" # strips the stars at the begining and the end of the string
print (str.strip( '*' ))

str = "00000123 this is string example....wow!!!XFV123456780"#MORE WORK NEEDED HERE 
print (str.strip( 'digits' ))
#Splitting strings

newString_list = upperString.split(" ")# splitting on a white space saves it as a list

print (newString_list)

#Files IN and OUT 
