a = int(input())
b = int(input())
c = int(input())
if a!=b and a!=c and b!=a and b!=c and c!=a and c!=b:
    print(0)
elif (a==b and a>c or a<c) or (a==c and a>b or a<b) or (b==c and b > a or b < a):
    print(2)
elif a==b==c:
    print(3) 