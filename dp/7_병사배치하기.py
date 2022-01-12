n=7
ls=[15,11,4,8,5,2,4]
#순서를 뒤집어 '최장 증가 부분수열'문제로 변환
ls.reverse()
dp=[1]*n

for i in range(1,n):
    for j in range(i):
        if ls[j]<ls[i]:
            #오름차순경향이 유지되면
            #dp를 업데이트한다.
            #dp의 각 index는 해당 index의 array의 요소가 마지막 요소가 되는 배열의 길이를 의미한다.
            #그러므로 index i가 증가할때마다 마지막 요소가 변하고 그에 따른 dp[i]도 변하는 것이다.
            #오름차순 경향을 벗어나는 요소때문에 길이가 업데이트 안된만큼 array의 최대 길이는 줄었다.
            dp[i]=max(dp[i],dp[j]+1)
print(dp)
print(n-max(dp))