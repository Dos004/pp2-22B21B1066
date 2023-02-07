s = str(input())
if (len(s) % 2 ==0):
    print(s[len(s)//2:]+s[0:len(s)//2])
else: 
    print(s[(len(s)+1)//2:]+s[0:(len(s)+1)//2])
