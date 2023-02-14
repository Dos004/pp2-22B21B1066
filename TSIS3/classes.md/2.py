class Shape():
    def area(self):
        print(f"area of the shape: 0")
class Square(Shape):
    def __init__(self,length):
       self.length = length
    
    def area(self):
        print(f"area of square: {self.length ** 2}")

shape1 = Shape()
shape1.area()

side = int(input())
sq1 = Square(side)
sq1.area()