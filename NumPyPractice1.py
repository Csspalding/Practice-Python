# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 14:29:03 2018
NumPy Practice
Tutorial http://www.learnpython.org/en/Numpy_Arrays

@author: Cass
"""

# Import the numpy package as np
import numpy as np
# Create 2 new lists height and weight
height = [1.87,  1.87, 1.82, 1.91, 1.90, 1.85]
weight = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]
# Create 2 numpy arrays from height and weight
np_height = np.array(height)
np_weight = np.array(weight)

print("type")
print(type(np_height))

# Calculate bmi
bmi = np_weight / np_height ** 2

# Print the result
print("result bmi")
print(bmi)
print ("\n")
# For a boolean response
bmi > 25

# Print only those observations above 25
print("only bmi above 25")
print (bmi[bmi > 25])
weight_kg = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]



# Create a numpy array np_weight_kg from weight_kg
np_weight_kg = np.array(weight_kg)  

# Create np_weight_lbs from np_weight_kg scalar is 2.2lbs per kg
np_weight_lbs = np_weight_kg * 2.2
print ('weight kg converted to lbs array is' )
print (np_weight_lbs)
# Print out np_weight_lbs