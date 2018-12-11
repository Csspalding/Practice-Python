# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 21:39:22 2018
python practise - classes and objects from codeacademy exercises
SYNTAX
class Name(object)
    def __init__(self): // here the constructor initialises the instance of the object/class
    
    
@author: Cassie  
"""
class Triangle(object):"""the class has to inherit from object as default"""
def __init__(self, angle1, angle2,angle3):
    self.angle1 = angle1
    self.angle2 = angle2
    self.angle3 = angle3


class Fruit(object):
  """A class that makes various tasty fruits."""
  def __init__(self, name, color, flavor, poisonous):
    self.name = name
    self.color = color
    self.flavor = flavor
    self.poisonous = poisonous

  def description(self):
    print ("I'm a %s %s and I taste %s." % (self.color, self.name, self.flavor))

  def is_edible(self):
    if not self.poisonous:
      print ("Yep! I'm edible.")
    else:
      print("Don't eat me! I am super poisonous.")

lemon = Fruit("lemon", "yellow", "sour", False)

lemon.description()
lemon.is_edible()







class Animal(object):
  """Makes cute animals. and uses class member variables, is_alive & health are only available to that class
  other variables are Global variables - available to everywhere in scope, 
  and Instance variables - only in scope for that instance of the method or function"""
  is_alive = True
  health = "good"
  #is_hungry = False 
  def __init__(self, name, age): # For initializing our instance objects
    self.name = name
    self.age = age
  # Add your method here!
  def description(self):
    print (self.name)
    print (self.age)
# Note that self is only used in the __init__()
# function definition; we don't need to pass it
# to our instance objects.

zebra = Animal("Jeffrey", 2)
giraffe = Animal("Bruce", 1)
panda = Animal("Chad", 7)

print (zebra.name, zebra.age, zebra.is_alive)
print (giraffe.name, giraffe.age, giraffe.is_alive)
print (panda.name, panda.age, panda.is_alive)

 
    
    
hippo = Animal("Anderson", 36)
hippo.description()
sloth = Animal("Slug", 20)
ocelot = Animal ("Harriet",70)
print (hippo.health)
print (sloth.health)
print (ocelot.health)

class ShoppingCart(object):
  """Creates shopping cart objects
  for users of our fine website."""
  items_in_cart = {}
  def __init__(self, customer_name):
    self.customer_name = customer_name

  def add_item(self, product, price):
    """Add product to the cart."""
    if not product in self.items_in_cart:
      self.items_in_cart[product] = price
      print (product + " added.")
    else:
      print (product + " is already in the cart.")

  def remove_item(self, product):
    """Remove product from the cart."""
    if product in self.items_in_cart:
      del self.items_in_cart[product]
      print (product + " removed.")
    else:
      print (product + " is not in the cart.")
my_cart = ShoppingCart("Becki")
my_cart.add_item("orange", 0.40)


"""inheritance returning customer is-a customer"""
class Customer(object):
  """Produces objects that represent customers."""
  def __init__(self, customer_id):
    self.customer_id = customer_id

  def display_cart(self):
    print ("I'm a string that stands in for the contents of your shopping cart!")

class ReturningCustomer(Customer):
  """For customers of the repeat variety."""
  def display_order_history(self):
    print ("I'm a string that stands in for your order history!")

monty_python = ReturningCustomer("ID: 12345")
monty_python.display_cart()
monty_python.display_order_history()


"""Inheritance triangle is-a shape"""

class Shape(object):
  """Makes shapes!"""
  def __init__(self, number_of_sides):
    self.number_of_sides = number_of_sides

# Add your Triangle class below!
class Triangle(Shape):
  def __init__(self, side1, side2, side3):
    self.side1 = side1
    self.side2 = side2
    self.side3 = side3
    
    
  """Inheritance and Override a method """
  
class Employee(object):
  def __init__(self, name):
    self.name = name
  def greet(self, other):
    print ("Hello, %s" % other.name)

class CEO(Employee):
  def greet(self, other):
    print ("Get back to work, %s!" % other.name)

ceo = CEO("Emily")
emp = Employee("Steve")
emp.greet(ceo)
# Hello, Emily
ceo.greet(emp)
# Get back to work, Steve!



class Employee(object):
  """Models real-life employees!"""
  def __init__(self, employee_name):
    self.employee_name = employee_name

  def calculate_wage(self, hours):
    self.hours = hours
    return hours * 20.00

# Add your code below!
class PartTimeEmployee(Employee):
  def calculate_wage(self, hours):
    self.hours = hours
    return hours * 12.00  

""" If you override a method in the base (super)class that later you realise you need to call, you can 
call the super class original method SYNTAX
class Derived(Base):
  def m(self):
    return super(Derived, self).m() """

class Employee2(object):
  """Models real-life employees!"""
  def __init__(self, employee_name):
    self.employee_name = employee_name

  def calculate_wage(self, hours):
    self.hours = hours
    return hours * 20.00

"""Call the super command when overriding a method to get the original superclass method"""
class PartTimeEmployee2(Employee2):
  def calculate_wage(self, hours):
    self.hours = hours
    return hours * 12.00
  
  def full_time_wage(self,hours):
    self.hours = hours
    return super(PartTimeEmployee2, self).calculate_wage(hours)#here the super class of the derived class is called
  
milton = PartTimeEmployee2("Max")
print (milton.full_time_wage(10))


class Triangle2(object):
  
  number_of_sides = 3
  def __init__(self,angle1,angle2,angle3):
    self.angle1 = angle1
    self.angle2 = angle2
    self.angle3 = angle3
    
  def check_angles(self):
    if (self.angle1 + self.angle2 + self.angle3 == 180):
      return True
    else: 
      return False
  
my_triangle = Triangle2(90,30,60)
print (my_triangle.number_of_sides)
print(my_triangle.check_angles())


"""This triangle has equal angles, inherits from triangle class
self.angle1 is from the super class and is equal to the member varialbe angle 60"""
class Equilateral(Triangle2):
  angle = 60
  def __init__(self):
    self.angle1 = self.angle
    self.angle2 = self.angle
    self.angle3 = self.angle
    
  def check_angles(self):
      if (self.angle1 and self.angle2 and self.angle3 == 60):
          print ("All angles equal 60 degrees")
          return True
      else: 
          return False
   
  
    
equT = Equilateral
print (equT.number_of_sides)
print ( equT.angle)
print (equT.check_angles)    
    
    
    
    
    
    