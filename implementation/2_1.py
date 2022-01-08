n=int(input())
plan=list(input().split())

x,y=1,1
# 우측부터 반시계
dx=[0,-1,0,1]
dy=[1,0,-1,0]
move_type=['R','U','L','D']

for dir in plan:
    #move_type과 대조.
    for i in range(len(move_type)):
        if dir==move_type[i]:
            tx=x+dx[i]
            ty=y+dy[i]
    if not(1<=tx and tx<=n and 1<=ty and ty<=n):
        continue
    x=tx
    y=ty
print(x,y)