from collections import deque

def solution(progresses, speeds):
    answer = []
    day=0
    cnt=0
    queue=deque(progresses)
    speeds_queue=deque(speeds)
    while queue:
    #queue가 있는동안
        if queue[0]+speeds_queue[0]*day>=100:
            #맨 앞대기열을 검사.
            queue.popleft()
            speeds_queue.popleft()
            cnt+=1
        else: 
            if cnt>0:
                #배포가능할 경우
                answer.append(cnt)
                cnt=0
            else:
                #배포불가하고, 맨 앞대기열도 검사했으므로 day++
                day+=1
    #queue가 비었다는 것은 전날에 배포가 이루어졌음을 의미한다.
    #따라서 전날의 cnt를 append한다. 
    answer.append(cnt)

    return answer
print(solution([93, 30, 55], [1, 30, 5]))
    
