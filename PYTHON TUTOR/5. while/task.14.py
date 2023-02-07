x = [0,1]
i=2
limit = int(input())
while i <= limit:
    x.append(x[i-1]+x[i-2])
    i+=1
if(limit == 0):
    print("0")
else:
    print(x[-1])
