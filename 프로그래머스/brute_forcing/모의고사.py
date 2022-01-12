def solution(answers):
    rtn = []
    cnt_1,cnt_2,cnt_3=0,0,0
    n=len(answers)
    ls_1=[1,2,3,4,5]             #5
    ls_2=[2,1,2,3,2,4,2,5]       #8
    ls_3=[3,3,1,1,2,2,4,4,5,5]   #10
    if n<=5:
        ls_1=ls_1[:n]
    else:
        for i in range(n-5):
            ls_1.append(ls_1[i]) 
    if n<=8:
        ls_2=ls_2[:n]
    else:
        for i in range(n-8):
            ls_2.append(ls_2[i])
    if n<=10:
        ls_3=ls_3[:n]
    else:
        for i in range(n-10):
            ls_3.append(ls_3[i])
            
    for i in range(n):
        if ls_1[i]==answers[i]:
            cnt_1+=1
        if ls_2[i]==answers[i]:
            cnt_2+=1
        if ls_3[i]==answers[i]:
            cnt_3+=1
    max_score=max(cnt_1,cnt_2,cnt_3)
    if cnt_1==max_score:
        rtn.append(1)
    if cnt_2==max_score:
        rtn.append(2)
    if cnt_3==max_score:
        rtn.append(3)
    
    return rtn