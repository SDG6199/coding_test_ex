from collections import deque

def bfs(graph,start,visited):
    queue=deque([start])
    visited[start]=True
    while queue:
        v=queue.popleft()
        print(v,end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True
graph=[          #각 인접리스트는 오름차순이므로 노드번호가 작은 노드부터 방문하는 규칙임.
    [],          #0번노드는 없다.
    [2,3,8],     #1번노드의 인접리스트
    [1,7],       #2번노드의 인접리스트
    [1,4,5],     #...
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]        #8번노드의 인접리스트
]
#각 노드가 방문된 정보를 표현.
visited=[False]*9
bfs(graph,1,visited)

