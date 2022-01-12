import math
def solution(name):
    answer = 0
    temp_cur=0
    cur=len(name)-1
    a=len(name)-1
    for i in range(len(name)):
        answer+=min(abs(ord('A')-ord(name[i])), abs(ord(name[i])-(ord('Z')))+1)
        temp_cur=i+1
        while temp_cur<len(name) and name[temp_cur]=='A':
            temp_cur+=1
            a=i*2+1+len(name)-1-temp_cur
        cur= min(cur,a)
        
    answer+=cur
    return answer