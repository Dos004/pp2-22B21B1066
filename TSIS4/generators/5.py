def inverse(N):
    for i in range(N,0,-1):
        yield i
for j in inverse(int(input())):
    print(j)