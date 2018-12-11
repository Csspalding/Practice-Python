# -*- coding: utf-8 -*-
"""
@author: Cassie
Created on Mon Sep 24 16:46:48 2018
Tutorial with Derek Banas 
File in & out
w write mode
r read mode
r+ read & write
a append to the file
if no mode is stipulated then r is automatic?? check this
'b' on the mode opens the file in binary

In text mode, the default when reading is to convert platform-specific line 
endings (\n on Unix, \r\n on Windows) to just \n. When writing in text mode,
 the default is to convert occurrences of \n back to platform-specific line 
 endings. This behind-the-scenes modification to file data is fine for text 
 files, but will corrupt binary data like that in JPEG or EXE files.
 Be very careful to use binary mode when reading and writing such files.

It is good practice to use the 'with' keyword when dealing with file objects.
 The advantage is that the file is properly closed after its suite finishes,
 even if an exception is raised at some point. Using 'with' is also much shorter 
 than writing equivalent try-finally blocks:

>>>
>>> with open('workfile') as f:
...     read_data = f.read()
>>> f.closed
True
If you’re not using the 'with' keyword, then you should call f.close() to close the file

"""
import os
import sys

test_file = open("testPython.txt", w)# mode to write to the file is w

print (test_file.mode)# returns the mode you created the file

print(test_file.name)# incase you forget the variable file name

test_file.write(bytes("I am writting this in my testPython file\n", 'UTF-8'))

test_file.close()

test_file = open("testPython.txt", "r+")# mode to be able to read and write the file r+

testPython.txt = test_file.read()
print(test_file)

#os.remove("testPython.txt") # to delete the file use os.remove() and pass in the name the file
