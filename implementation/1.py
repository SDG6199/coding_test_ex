# 동쪽부터 반시계.
dx=[0,-1,0,1]
dy=[1,0,-1,0]
x,y=2,2
ls=[]
# ls=[[0]*4 for i in range(5)]  #5x4

row=int(input())
for i in range(row):
    ls.append(list(map(int,input().split())))
for i in range(4):
    ls[x][y]=1
    x+=dx[i]
    y+=dy[i]
    
for i in range(row):
    for j in range(len(ls[1])):
        print(ls[i][j], end=' ')
    print()