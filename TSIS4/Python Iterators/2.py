string_random = "I am atomic"
myit = iter(string_random)
for i in range(len(string_random)):
    print(next(myit))