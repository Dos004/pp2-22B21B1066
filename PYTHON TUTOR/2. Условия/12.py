a = int(input())
b = int(input())
c = int(input())
if (a * b) > c and ((c % a == 0) or (c % b == 0)):
    print("YES")
else:
    print("NO")