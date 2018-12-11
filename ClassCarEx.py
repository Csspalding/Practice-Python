# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 10:42:57 2018
CodeAcademy Python ex in classes CAR
@author: Cassie
"""
 # needs to inherit from the super python Object class// or another super class
class Car(object):
  condition = "new"
  def __init__(self, model, color, mpg):
    self.model = model
    self.color = color
    self.mpg   = mpg
    
  def display_car(self):
    message = "This is a " + self.color + " " +self.model + " with " + str(self.mpg) + " MPG."
    return message
    
  def drive_car(self):
    self.condition = "used"
    
my_car = Car("DeLorean", "silver", 88)

print (my_car.condition)
print (my_car.model)
print (my_car.color)
print (my_car.mpg)
my_car.drive_car()
print (my_car.condition)

class ElectricCar(Car):
  def __init__(self,model, color, mpg,battery_type): 
    self.model = model
    self.color = color
    self.mpg   = mpg
    self.battery_type = battery_type
  def drive_car(self):
    self.condition = "like new"
    
my_car = ElectricCar("audi","red", 120, "molten salt")
my_car.drive_car()
print (my_car.condition)    




