# Сколько ounce песка нужно чтобы заполнить сферу. (плотность песка = 1500 кг/м3)
# на ввод двется радиус сферы R
def ounces(grams):
    ounces = 28.3495231 * grams 
    return ounces

def volume(r):
    return float((4/3)*3.14 * r**3 )


r = int(input()) # radius of sphera
kilogramm = 1500
ro = ounces(kilogramm * 1000) #1500kg/m^3 -> ounce/m^3
m = volume(r) * ro
print(m)