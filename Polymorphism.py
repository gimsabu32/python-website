class Shape:
    def area(self):
        pass #Placeholder method
        
class Circle:
    def __init__(self, radius):
      self.radius =radius 
    def area(self):
        return 3.14 * self.radius ** 2 
    
class rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
    
def calculate_area(shape):
    return shape.area()

circle = Circle(5)
rectangle = rectangle(4, 6)

print(calculate_area(circle))    # Calculatte area of the circle
print(calculate_area(rectangle)) # Calculate area of the rectangle