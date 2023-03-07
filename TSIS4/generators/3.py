def printer(N):
    for i in range(0,N+1):
        if i % 4==0 and i % 3==0:
            yield i
for j in printer(int(input())):
    print(j)