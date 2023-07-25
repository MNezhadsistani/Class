class Shape:
    size=10
    def __init__(self,name,color):
        self.name=name
        self.color=color
shape1=Shape("Circle","Yellow")
shape2=Shape("Square","Green")
print(shape1.size)
print(shape1.name)
print(shape1.color)
shape1.color='Blue'
shape1.radius=20
print(shape1.color)
print(shape1.radius)
"""
Command output:
10
Circle
Yellow
Blue
20
"""
