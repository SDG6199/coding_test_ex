#순서를 유지하면서 대소비교를 통해 요소를 수정하고 있으므로 스택을 사용해야한다.

def solution(number, k):
    answer = ''
    number=list(number)
    stack=[number[0]]
    for i in range(1,len(number)):
        while stack[-1]<number[i] and k>0:
            stack.pop()
            k-=1
            # stack이 비었을 때
            if (not stack):
                break
        stack.append(number[i])
    if k>0:
        stack=stack[:-k]
    answer="".join(stack) 
    return answer

print(solution("1231234",3))
