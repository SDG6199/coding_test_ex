#N이 1이 될 때까지.
#1<=N<=100000, 2<=K<=100000, 
result=0

N,k=map(int,input().split())

while 1:
    temp=(N//k)*k
    result+=N-temp
    N=temp
    if N<k:
        break
    result+=1
    N=N//k
result+=N-1
print(result)


