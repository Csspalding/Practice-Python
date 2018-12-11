# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 20:10:24 2018
Tutorial Generators
http://www.learnpython.org/en/Generators
@author: Cassie
"""

import random

def lottery():
    # returns 6 numbers between 1 and 101
    for i in range(6):
        yield random.randint(1, 101)

    # returns a 7th number between 1 and 3
    yield random.randint(1,3)

for random_number in lottery():
       print("And the next number is... %d" %(random_number))