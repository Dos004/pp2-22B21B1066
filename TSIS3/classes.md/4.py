class Point():
    def __init__(self,x1,x2,y1,y2):
        self.x1 = int(x1)
        self.x2 = int(x2)
        self.y1 = int(y1)
        self.y2 = int(y2)
    
    def show(self):
        print(f"coordinate of point A = {self.x1,self.y1} \ncoordinate of point B = {self.x2,self.y2}")
    
    def move(self,x11,x22,y11,y22):
        # заново создает кооридинаты удаляя прежние
        del self.x1,self.x2,self.y1,self.y2
        self.x11 = int(x1)
        self.x22 = int(x2)
        self.y11 = int(y1)
        self.y22 = int(y2)
    
    def dist(self):
        d = ((self.x1 - self.x2)**2 + (self.y1 - self.y2)**2)**0.5
        print(f"distance between 2 points A and B: {d}")

x1 = int(input())
x2 = int(input())
y1 = int(input())
y2 = int(input())

points = Point(x1,x2,y1,y2)
points.show()
points.move()
points.dist()