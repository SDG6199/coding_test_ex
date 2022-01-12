n=2;merge=14
ls=[3,7]
#merge를 만들기위한 최소한의 화폐개수?
#불가능하면 -1출력.
d=[10001]*(merge+1)
#작은 merge에 대한 최적을 구해서 계속 더하면된다.
d[0]=0
for i in range(len(ls)):
    #화폐를 꺼낸다. i는 화폐인덱스.
    for j in range(ls[i],merge+1):
        #j원. 그리고 dp table의 인덱스.
        if d[j-ls[i]]!=10001:
            #dp테이블에 d[j-화폐단위]의 값이 존재하는 경우.
            #dp table을 update한다.
            d[j]=min(d[j],d[j-ls[i]]+1)
print(d[merge])