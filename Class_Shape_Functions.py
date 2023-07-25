class Shape:
    def __init__(self,name,color):
        self.name=name
        self.color=color
shape1=Shape("Circle","Yellow")
shape2=Shape("Circle","Blue")
print(hasattr(shape1,'radius')) # Returns true if 'radius' attribute exists False
setattr(shape1,'radius',10)# Set attribute 'radius' at 8
print(shape1.radius)
shape2.radius=5
print(getattr(shape2,'radius')) # Returns value of 'radius' attribute
print(shape1.color)
delattr(shape1,'color') # Delete attribute 'color'
print(shape1.color)
"""
Command output:
False
10
5
Yellow
Traceback (most recent call last):
  File "C:\Users\m_nezhadsistani\Desktop\Class_Shape_info.py", line 14, in <module>
    print(shape1.color)
AttributeError: 'Shape' object has no attribute 'color'
"""
