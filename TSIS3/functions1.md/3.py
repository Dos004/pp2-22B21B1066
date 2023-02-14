def solve(numheads,numlegs):
    for rabbits in range(numheads+1):
        chickens = numheads - rabbits
        if(chickens * 2 + rabbits * 4 == numlegs):
            return (chickens,rabbits)
print(solve(int(input()),int(input())))