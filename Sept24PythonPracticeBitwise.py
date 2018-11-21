# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 08:24:39 2018
PythonPractice Bitwise operations and binary in Python
@author: Cassie
"""

#BITWISE in python manipulating bytes  

print( 5 >> 4 ) # Right Shift
print (5 << 1)  # Left Shift
print( 8 & 5)   # Bitwise AND
print( 9 | 4 )  # Bitwise OR
print (12 ^ 42) # Bitwise XOR
print( ~88)     # Bitwise NOT
print("**********************")

print (0b1,end=" ")   #1
print (0b10,end=" ")   #2
print (0b11,end=" ") #3
print (0b100,end=" ")  #4
print (0b101,end=" ")  #5
print (0b110,end=" ")  #6
print (0b111,end=" ")   #7
print (0b1000,end=" ") #8
print (0b1001,end=" ") #9
print (0b1010)  #10
print ("******")
print (0b1 + 0b11)
print (0b11 * 0b11)

'''
USEFUL NUMBERS TO KNOW FOR bits
2 ** 0 = 1
2 ** 1 = 2
2 ** 2 = 4
2 ** 3 = 8
2 ** 4 = 16
2 ** 5 = 32
2 ** 6 = 64
2 ** 7 = 128
2 ** 8 = 256
2 ** 9 = 512
2 ** 10 = 1024

one = 0b1
two = 0b10
three = 0b11
four = 0b100
five = 0b101
six  = 0b110
seven  = 0b111
eight  = 0b1000
nine = 0b1001
ten = 0b1010
eleven = 0b1011
twelve = 0b1100

To print a number in binary use the bin() function which takes an integer as input and returns the binary representation of that integer in a string.
Note that after using bin() you can no longer operate on the value like a number.
NB you can acess base 8 and base 16 using the oct() and hex() functions in the same way
'''
'''
In Python  casting using int() function. Also has second parameter, by passing a string containing a number and the base that number is in, 
the function will return the value of that number converted to base ten. syntax int("5", 2)
'''
print (int("110", 2))
# ==> 6
print ("******************")
print (int("1",2))
print (int("10",8))# base 8 for example
print (int("111",2))
print (int("0b100",2))
print (int(bin(5),2))
# Print out the decimal equivalent of the binary 11001001.
print (int("0b11001001", 2))


# Left Bit Shift (<<) 
print ("Left shift operator") 
print(0b000001 << 2) # == 0b000100 (1 << 2 = 4), so prints 4
print (0b000101 << 3) # == 0b101000 (5 << 3 = 40) prints 40       

# Right Bit Shift (>>)
0b0010100 >> 3 # == 0b000010 (20 >> 3 = 2)
0b0000010 >> 2 # == 0b000000 (2 >> 2 = 0)

shift_right = 0b1100
shift_left = 0b1

# Your code here!
shift_right = shift_right >> 2
shift_left = shift_left << 2

print("Shift right 1100 in binary using bin(): " +bin(shift_right))
print( "Shift left 1 in binary using bin(): " +bin(shift_left))
'''
The & AND operator
The bitwise AND (&) operator compares two numbers on a bit level and returns
 a number where the bits of that number are turned on if the corresponding bits 
 of both numbers are 1. or ON not off 
      a:   00101010   42
      b:   00001111   15       
===================
 a & b:    00001010   10


#Note that using the & operator can only result in a number that is less 
#than or equal to the smaller of the two values.
0 & 0 = 0
0 & 1 = 0
1 & 0 = 0
1 & 1 = 1
'''
0b111 (7) & 0b1010 (10) # results in 0b10
#   a   0111
#   b   1010
#gives  0010

print (bin(0b1110 & 0b101))# 0b100
'''
The bitwise OR (|) operator compares two numbers on a bit level and returns a
 number where the bits of that number are turned on if either of the 
 corresponding bits of either number are 1, including if both are 1.
     a:  00101010  42
     b:  00001111  15       
================
a | b:   00101111  47 
 
0 | 0 = 0
0 | 1 = 1 
1 | 0 = 1
1 | 1 = 1
 
110 (6) | 1010 (10)#  = 1110 (14)
'''

#give the binary string for 0b1110 | 0b101
 #        1110
 #        0101
print ("0b1111")

'''
The XOR (^) or exclusive or operator compares two numbers on a bit level
 and returns a number where the bits of that number are turned on if either
 of the corresponding bits of the two numbers are 1, but not both.
 
    a:  00101010   42
    b:  00001111   15       
================
a ^ b:  00100101   37
Keep in mind that if a bit is off in both numbers, it stays off in the result. 
Note that XOR-ing a number with itself will always result in 0.

0 ^ 0 = 0
0 ^ 1 = 1
1 ^ 0 = 1
1 ^ 1 = 0
'''
111 (7) ^ 1010 (10) = 1101 (13)
#give the binary string for 0b1110 ^ 0b101
#        1110
#        0101
print("0b1011")

'''
The bitwise NOT operator (~) just flips all of the bits in a single number.
this is equivalent to adding one to the number and then making it negative.
'''
print (~1)
print(~101)
print(~256)

''' BIT MASK
A bit mask is just a variable that aids you with bitwise operations. 
A bit mask can help you turn specific bits on, turn others off, 
or just collect data from an integer about which bits are on or off.
'''
num  = 0b1100
mask = 0b0100
desired = num & mask
if desired > 0:
  print ("Bit was on")

#function to check if the 4th bit is ON i.e. 1
def check_bit4(input):    
  num = input
  mask = 0b1000
  desired = num & mask
  if desired > 0:
    return "on"
  else:
    return "off"

'''
You can also use masks to turn a bit in a number on using |.
e.g. to make sure the rightmost bit of number a is turned on
'''
a = 0b110 # 6
mask = 0b1 # 1
desired =  a | mask # 0b111, or 7

#here the 3rd bit is changed to ON using mask and the | operater
#note that printing a gives the base10 number, bin() gives the binary base2 number
a = 0b10111011
mask = 0b100
desired = a | mask
print(a)#187
print (bin(0b10111111))#0b10111111
print (bin(desired))

#USING ^ OR OPERATOR TO FLIP THE BITS
a = 0b11101110
mask = 0b11111111
desired = a ^ mask
print(a)
print(desired)
print (bin(desired))

'''
SLIDING BITS WITH MASK
use the left shift (<<) and right shift (>>) operators to slide masks into place.
'''
a = 0b101 
# Tenth bit mask
mask = (0b1 << 9)  # One less than ten AS SLIDING FROM THE FIRST TO THE TENTH IS 9 PLACES
desired = a ^ mask
#a function to take any number and the n position to flip the bit
def flip_bit(number,n):
 #shift from position 1 to position n-1
  a = number
  bit = n-1
  mask = (0b1 << bit)
  result = a ^ mask
  return (bin(result))























 
 