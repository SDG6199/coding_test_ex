n,m=map(int,input().split())
ls=[]
for i in range(n):
    ls.append(list(map(int,input())))
cnt=0
def dfs(x,y):
    count=1         #@1 count=0
    if not(0<=x and x<=n-1 and 0<=y and y<=m-1):
        return False,0
    #아직방문하지 않았다면
    if ls[x][y]==0:
        ls[x][y]=1
        #인접된 모든노드를 방문(인접리스트를 순회하는 것과 같은 역할)
        count+=dfs(x-1,y)[1]    #@1 count=1+dfs(x-1,y)[1]]
        count+=dfs(x+1,y)[1]
        count+=dfs(x,y-1)[1]
        count+=dfs(x,y+1)[1]
        return True,count
    return False,0

for i in range(n):
    for j in range(m):
        ckeck_visit,count=dfs(i,j)
        if ckeck_visit==True:
            print(ckeck_visit,count)
            cnt+=1

print("cnt: %d" %(cnt))
print(ls)
