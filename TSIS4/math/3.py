import math
def area_polygon(sides,lenghth):
    return (sides * lenghth**2)/(4 * math.tan(math.pi/sides))
sides = int(input())
lenghth = int(input())
print(area_polygon(sides,lenghth))