def binary_search(arr,gross,start,end):
    while 1:
        mid=(start+end)//2
        temp_gross=0
        for i in arr:
            if i>mid:
                temp_gross+=i-mid
        if start>mid:
            break
        if temp_gross<gross:
            #잘린양이 목표량보다 작을 때
            #왼쪽으로 이진탐색.
            end=mid-1
        else:
            #잘린양이 목표량보다 클 때
            #오른쪽으로 이진탐색.
            start=mid+1
            #임시저장.
            result=mid
    return result
    
n,m=list(map(int,input().split()))
ls=list(map(int,input().split()))
print(binary_search(ls,m,0,max(ls)))