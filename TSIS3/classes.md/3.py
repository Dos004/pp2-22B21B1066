class Shape():
    def area(self):
        print(f"area of the shape: 0")
class Rectangle(Shape):
    def __init__(self,length,width):
        self.length = length
        self.width = width
    
    def area(self):
        print(f"area of the rectangle: {self.length * self.width}")

a = int(input())
b = int(input())
rec1 = Rectangle(a,b)
rec1.area()