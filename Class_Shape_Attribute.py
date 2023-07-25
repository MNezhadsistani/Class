class Shape:
  'This is an example for the shape class'
  sides = 4 #first property
  name = "Square" #second property
  def description(des): #method defined
    return ("A square with 4 sides") 
shape1 = Shape() #creating an object of Shape
print("Name of shape is:",(shape1.name))
print("Number of sides are:",(shape1.sides))
print(shape1.description())
print(Shape.__doc__)
print(Shape.__name__)
print(Shape.__module__)
print(Shape.__bases__)
"""
Command output:
Name of shape is: Square
Number of sides are: 4
A square with 4 sides
This is an example for the shape class
Shape
__main__
(<class 'object'>,)
"""
