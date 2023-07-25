class Shape:
    def __init__(self,name,color):
        self.name=name
        self.color=color
shape1=Shape("Circle","Yellow")
del shape1.name
print(shape1.name)
"""
Command output:
AttributeError: 'Shape' object has no attribute 'name'
"""
