# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 08:20:16 2018

@author: Cassie
"""
#CodeAcademy python practice Sept 23rd, trailling comma keeps printing ALL ON ONE LINE
d = { 
  "name": "Eric",
  "age": 26
}

for key in d:
  print ( key, d[key], end=" ")
print("\n")
for letter in "Eric":
  print (letter, end= "")  # note the comma!
  my_dict = {
  'name': 'Nick',
  'age':  31,
  'occupation': 'Dentist',
}
#Solution nb the trailling comma is python 2, in 3 you have to spipulate what you want after the comma ,end=" " 
#for key in my_dict:
 # print key, my_dict[key]
print("\n" *5)
 #BUILDING LISTS using python LIST COMPREHENSION builder enerates the list following an instruction statment
 # using keywords: for if in
 
evens_to_50 = [i for i in range(51) if i % 2 == 0]
print (evens_to_50)

doubles_by_3 = [x * 2 for x in range(1, 6) if (x * 2) % 3 == 0]

even_squares = [x * x for x in range(1,11) if (x * x) % 2 == 0]

print (even_squares)

cubes_by_four = [x ** 3 for x in range(1, 11) if ((x ** 3) % 4) == 0]
print (cubes_by_four)

#SLICE OF A LIST syntax List_name [start(inclusive): end(exclusive): stride)]
l = [i ** 2 for i in range(1, 11)]
# Should be [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# WHERE i IS 1 ,2, 3, 4,  5,  6,   7,  8,  9,  10

print (l[2:9:2]) # should print [9, 25, 49, 81]
my_list = range(1, 11)
backwards_my_list = my_list[::-1]

to_one_hundred = range(101)
backwards_by_tens = to_one_hundred[::-10]
print(backwards_by_tens)

to_21 = range(1, 22)
print = (to_21)
odd = to_21[::2]
print(odd)

middle_third = to_21[7:14]
print(middle_third)

#LAMBDA functional programming passes the function to a filter, does the work and returns a value,
# does not need to know the function name 
languages = ["HTML", "JavaScript", "Python", "Ruby"]

# Add arguments to the filter()
print (filter(lambda x: x == "Python", languages))

squares = [x * x for x in range(1,11)]

print (squares)
#filter the list so only the sq numbers btwn 30-70 print
print (filter(lambda x: x > 29 and x< 71, squares))

# more comprehension list building
squares = [x ** 2 for x in range(5)]

threes_and_fives = [x for x in range(1,16) if x % 3 == 0 or x % 5 == 0]
#reveil the secret message, it's backwards and every other letter
garbled = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"
message = garbled[::-2]
#removing an element from a string, here X is removed to reveil a secret message
garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"
message = filter(lambda ch:  ch != "X",garbled)
print(message)

#BITWISE in python manipulating bytes 
print (5 >> 4)  # Right Shift
print (5 << 1 ) # Left Shift
print (8 & 5)   # Bitwise AND
print (9 | 4 )  # Bitwise OR
print (12 ^ 42) # Bitwise XOR
print (~88)     # Bitwise NOT