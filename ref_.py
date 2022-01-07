import time
#통상 연산 1억번당 1~3초
tic=time.time()
for i in range(1,100000000):
    pass
toc=time.time()
print(tic-toc)
##########################
a=1.23456e2
print(round(a,2))
##########################
world=list()    # 2xn
for i in range(2):
    world.append(list(map(int,input().split(' '))))
for i in range(len(world)):
    for j in range(len(world[i])):
        print(world[i][j], end=' ')
    print()
##########################
#입력을 빨리 받아야할 때 // input()대신 sys.stdin.readline().rstrip('\n')
import sys
world=list()    # 2xn
for i in range(2):
    world.append(list(map(int,sys.stdin.readline().rstrip('\n').split(' '))))
for i in range(len(world)):
    for j in range(len(world[i])):
        print(world[i][j], end=' ')
    print()