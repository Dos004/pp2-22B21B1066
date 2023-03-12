s = input()
suma = 0

sumA = 0
for i in s:
    if i.islower():
        suma +=1
    else:
        sumA +=1

print(suma)

print(sumA)