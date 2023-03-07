mytuple = ("apple","banana","cherry")
myit = iter(mytuple)
# i = 0
# while i < len(mytuple):
#     print(next(myit)) 
#     i += 1
for i in range(len(mytuple)):
    print(next(myit))