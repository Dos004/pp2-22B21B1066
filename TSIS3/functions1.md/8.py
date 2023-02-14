def spy_game(nums):
    code = [0,0,7,'x']
    for num in nums:
        if num == code[0]:
            code.pop(0)
        if len(code) == 1:
            return True
    return False

a = [int(i) for i in input().split()]
print(spy_game(a))