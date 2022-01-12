def solution(n, lost, reserve):
    answer = 0
    #중복된 부분을 제외하기위한 전처리.
    set_reserve=set(reserve)-set(lost)
    set_lost=set(lost)-set(reserve)
    for i in set_reserve:
        if i-1 in set_lost:
            set_lost.remove(i-1)
            continue
        if i+1 in set_lost:
            set_lost.remove(i+1)
    answer=n-len(set_lost)
    return answer