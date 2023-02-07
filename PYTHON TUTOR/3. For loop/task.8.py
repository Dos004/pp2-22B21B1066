from math import factorial
s=0
m=int(input())
for k in range (1,m+1) :
    s=s+factorial(k)
print (s)
