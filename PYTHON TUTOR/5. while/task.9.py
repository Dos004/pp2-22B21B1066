max = 0
i = -1
n = -1
len = 0
while n != 0:
    n = int(input())
    if n > max:
        max = n
        i = len
    len += 1
print(i)
