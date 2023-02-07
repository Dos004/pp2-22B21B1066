max = 0
i = 0
n = -1
while n != 0:
    n = int(input())
    if n > max:
        max, i = n, 1
    elif n == max:
        i += 1        
print(i)
