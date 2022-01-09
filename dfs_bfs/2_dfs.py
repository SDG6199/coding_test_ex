def dfs(graph,start,visited):
    #현재 노드를 방문처리
    visited[start]=True
    #현재 노드와 연결된 다른 노드를 재귀적으로 방문.
    print(start,end=' ')
    for i in graph[start]:
        if not visited[i]:
            dfs(graph,i,visited)

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
dfs(graph,1,visited)