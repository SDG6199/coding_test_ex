import time
from typing import Counter
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
##########################
from itertools import permutations          #순열
from itertools import combinations          #조합
from itertools import product               #중복순열
from itertools import combinations_with_replacement     #중복조합

data=['A','B','C']
print(list(permutations(data,2)))
print(list(map("".join,list(permutations("12345",2)))))
print(list(combinations(data,2)))
print(list(product(data,repeat=2)))
print(list(combinations_with_replacement(data,2)))
##########################
import collections  #deque, counter등의 자료구조
from collections import Counter
counter=Counter(['A','B','A','A','C','B',1,1])
print(dict(counter))
from collections import deque
queue=deque([1,2])
queue.append(1)
queue.popleft()
queue.reverse()
print(queue)
##########################
import math         #factorial, pow, gcd 등
def lcm(a,b):
    return a*b//math.gcd(a,b)
a=21; b=14
print(math.gcd(a,b))
print(lcm(a,b))
print(math.factorial(5))
print(math.pow(2,5))
print(math.ceil(1.59122))
print(math.floor(1.59123))
print(round(1.59123,2))
##########################
import heapq        #heap자료구조의 que기능
import bisect       #binary search
