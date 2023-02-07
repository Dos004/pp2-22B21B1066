a = int(input())
b = int(input())
if a > b:
    for i in range(a,b-1,-1):
        print(i,sep=' ',end=' ')
elif a < b:
    for i in range(a,b+1):
        print(i,sep=' ',end=' ')
else:print(a or b)
