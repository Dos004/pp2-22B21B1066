number = int(input())
i = 1
while 2**i <= number:
    i += 1
print(i-1, 2**(i-1))
