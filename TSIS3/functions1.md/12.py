def histogram(a):
    for i in a:
        print('*' * i)

a = [int(i) for i in input().split()]
histogram(a)