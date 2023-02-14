def has_33(nums):
    cnt=0
    for i in range(len(a)):
        if a[i] == 3 and a[i-1] == 3:
                cnt+=1
    if cnt >= 1:
         return True
    else:
         return False
a = [int(i) for i in input().split()]
print(has_33(a))
