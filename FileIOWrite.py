# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 11:54:21 2018
Demonstrating IO files
Opens (if it does not exit it creates a file) output.txt (if it exists it writes over the file)
Write to the file 
Close the file
@author: Cassie
"""

my_list = [i ** 2 for i in range(1, 11)]
# Generates a list of squares of the numbers 1 - 10

f = open("output.txt", "w")#write to a file

for item in my_list:
  f.write(str(item) + "\n")
  
f.write("Done")# add any new text her to check it over writes the file

f.close()


my_file = open("output.txt", "r")# read a file

print (my_file.read())

my_file.close()

my_file2 = open("text.txt", "r+")# read and write to a file
my_file2.write("I'm the first line of the file!\nI'm the second line.\nThird line here, boss.")

print (my_file2.readline())
print (my_file2.readline())
print (my_file2.readline())

my_file2.close()

"""file objects contain a special pair of built-in methods: __enter__() and __exit__(). 
The details aren't important, but what is important is that when a file object's __exit__() method is invoked,
 it automatically closes the file.
 How do we invoke this method? With command with and command as.
 SYNTAX
 with open("file", "mode") as variable name:
  # Read or write to the file   """
  
 # with...as  command we don't need to explicity close the file  
with open("text2.txt", "w") as textfile: # textfile is the variable name for the file
  textfile.write("Success!") 
#Check if it actually did close automatically object __exit__ method wrapped in WithAs  
if (textfile.closed == False):# bool  .closed is True if the file is closed
  textfile.close()
print (textfile.closed)
  
 
"""Any code you would normally write outside of a block to work with a file 
could be written inside of a with-as code block.
Just be sure to indent your code using 2 spaces per indentation level, depending on compliler, 
otherwise Python won’t know that you intended for the code to be part of the with-as block. 
Failing to indent will cause an error if you try accessing anything you created inside of that code block,
or trying to access the file variable.""" 
  
  
  
  