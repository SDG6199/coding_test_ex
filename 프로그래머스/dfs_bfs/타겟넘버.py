def dfs(numbers,result,target):
    cnt=0
    #깊이가 바닥에 닿았을 때
    if len(numbers)==1:
        if target==result+numbers[0] or target==result-numbers[0]:
            return 1
        else: 
            return 0
    #재귀순서에 관계없이 cnt에 1씩 쌓인다.
    cnt+=dfs(numbers[1:],result+numbers[0],target)
    cnt+=dfs(numbers[1:],result-numbers[0],target)
    return cnt     

    # result+= 에 대해 +-numbers[i]의 케이스로 나뉜다.
    # result+= numbers[i]를 한 경우,
    # 그 다음 루프에서 다시 +-numbers[i]의 케이스로 나뉜다.
    # 즉, 재귀적으로 케이스가 나뉜다.

def solution(numbers, target):
    result=0
    answer=dfs(numbers,result,target)
    return answer
print(solution([1, 1, 1, 1, 1],3))
