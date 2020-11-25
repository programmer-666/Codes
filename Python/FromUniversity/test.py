import random, time
obj = [[2,2],[2,1]]
mxx, mxy = 10, 10
while True:
    for y in range(1,mxy):
        for x in range(1,mxx):
            if y == random.randint(2,mxy-1) and x == random.randint(2,mxx-1):
                print("*", end="")
            else:
                print("", end="")
        print()