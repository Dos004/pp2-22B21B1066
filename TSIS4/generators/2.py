def print_evens(N):
    for even in range(0,N+1,2):
        yield str(even)
N = int(input())
even_num = print_evens(N)
print(','.join(even_num))