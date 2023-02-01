a = int(input())
b = int(input())
c = int(input())
sum = 0
if (a % 2==0):
    sum+=a/2
else :
    sum+=int(a/2)+1 

if (b % 2==0):
    sum+=b/2
else :
    sum+=int(b/2)+1 

if (c % 2==0):
    sum+=c/2
else :
    sum+=int(c/2)+1 
print(sum)