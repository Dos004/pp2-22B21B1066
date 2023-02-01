x = input()
a = input()
y = input()
z = input()
if int(a)%2 == int(x)%2 and int(y)%2 == int(z)%2:
    print("YES")
elif int(y)%2 == int(x)%2 and int(a)%2 == int(z)%2:
    print("YES")
elif int(z)%2 == int(x)%2 and int(y)%2 == int(a)%2:
    print("YES")
else: 
    print("NO")