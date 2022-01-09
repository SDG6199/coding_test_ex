from collections import deque

n,m=map(int,input().split())
graph=[]
for i in range(n):
    graph.append(list(map(int,input())))
#x,y=0,0

#상하좌우
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x,y):
    queue=deque()
    queue.append((x,y))
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            tx=x+dx[i]
            ty=y+dy[i]
            if not(0<=tx and tx<=n-1 and 0<=ty and ty<=m-1):
                continue
            if graph[tx][ty]==0:
                continue
            if graph[tx][ty]==1:
                graph[tx][ty]=graph[x][y]+1
                queue.append((tx,ty))
    return graph[n-1][m-1]

print(bfs(0,0))
