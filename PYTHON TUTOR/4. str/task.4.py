n = str(input())
x = n.find(' ')
print(n[x+1:]+n[x]+ n[:x])
