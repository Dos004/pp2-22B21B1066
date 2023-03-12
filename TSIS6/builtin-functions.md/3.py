s = str(input())
def poli(s):
    return s == s[::-1]
    
if poli(s):
    print("YEs")

else:
    print("No")