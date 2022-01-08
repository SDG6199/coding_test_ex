n=int(input())
plan=list(input().split())

x,y=1,1
# 우측부터 반시계
dx=[0,-1,0,1]
dy=[1,0,-1,0]
for d in plan:
    if d=='R':
        x+=dx[0]
        y+=dy[0]
        if not(1<=x and x<=n and 1<=y and y<=n):
            x-=dx[0]
            y-=dy[0]
    if d=='U':
        x+=dx[1]
        y+=dy[1]
        if not(1<=x and x<=n and 1<=y and y<=n):
            x-=dx[1]
            y-=dy[1]
    if d=='L':
        x+=dx[2]
        y+=dy[2]
        if not(1<=x and x<=n and 1<=y and y<=n):
            x-=dx[2]
            y-=dy[2]
    if d=='D':
        x+=dx[3]
        y+=dy[3]
        if not(1<=x and x<=n and 1<=y and y<=n):
            x-=dx[3]
            y-=dy[3]
print(x,y)