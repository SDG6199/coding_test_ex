#최대한 많은 식량을 털어야한다.
#문제를 작은문제로 나눌 수 있는 문제이다. 
#왼쪽부터 턴다고 생각할때 이전에 털었던 결과와 현재 위치를 털때 발생할 결과중 큰 경우를 선택해가면서 털면 현재 위치에 대해 최대한 많이 턴 식량의 값을 얻을 수 있다.
n=int(input())
# len(array)
array=list(map(int,input().split()))

d=[0]*100
d[0]=array[0]
d[1]=max(array[0],array[1])
for x in range(2,len(array)):
    #bottom-up
    d[x]=max(d[x-1],d[x-2]+array[x])

print(d[len(array)-1])