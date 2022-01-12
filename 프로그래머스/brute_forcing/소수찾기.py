#순서를 고려하되, sosu_set에 들어갈 값이 중복되는 것은 피해야한다.
from itertools import permutations

def is_sosu(n,sosu_set):
    n=int(n)
    if n<2 or n in sosu_set:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True

def solution(numbers):
    rtn = 0
    sosu_set=set()
    n=len(numbers)
    for i in range(n):
        for j in list(map(int,map("".join,list(permutations(numbers,i+1))))):
            if is_sosu(j,sosu_set):
                sosu_set|={j}
                rtn+=1
    return rtn
print(solution("1715"))

