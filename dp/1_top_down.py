d=[0]*100
def fivo(x):
    if x==1 or x==2:
        return 1
    #이미 처리된 함수라면 처리하지 않음(동일문제반복해결을 피함)
    if d[x]!=0:
        return d[x]
    #큰 문제를 작은 문제로 쪼갬.
    #처리결과를 d[x]에 저장.
    d[x]=fivo(x-1)+fivo(x-2)
    return d[x]

print(fivo(5))