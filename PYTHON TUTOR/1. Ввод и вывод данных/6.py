n = int(input())
next = n + 1
prev = n - 1
txt1 = "The next number for the number {} is {}."
txt2= "The previous number for the number {} is {}."

print(txt1.format(n,next))
print(txt2.format(n,prev))