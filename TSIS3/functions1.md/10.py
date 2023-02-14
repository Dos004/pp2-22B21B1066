def unique_list(a):
    b=[]
    for i in a:
        if i not in b:
            b.append(i)
            
    return b


a = [int(i) for i in input().split()]
print(unique_list(a))