# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 11:45:37 2018
Class desmonstrating the use of the representation function __repr__()
@author: Cassie
"""

class Point3D(object):
  def __init__(self,x,y,z):
    self.x = x
    self.y = y
    self.z = z
  #__repr__  function that represents the object of the class using by return a print method for example  
  def __repr__(self):
    return "(%d, %d, %d)" % (self.x, self.y, self.z)
  
  
my_point = Point3D(1,2,3)
print (my_point)