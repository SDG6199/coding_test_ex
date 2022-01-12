n,m=list(map(int,input().split()))
ls=[]
d=[]
dir_type=[0,1,2]
#0:우상, 1:우, 2:우하
for i in range(n):
    ls.append(list(map(int,input().split())))
    d.append(ls[i])

for j in range(1,m):
    #한 열씩 순회
    for i in range(n):
        if i==0: left_up=0
        else: left_up=ls[i-1][j-1]
        if i==n-1: left_down=0
        else: left_down=ls[i+1][j-1]
        left=ls[i][j-1]
        d[i][j]=ls[i][j]+max(left_up,left_down,left)
print(max([i[m-1] for i in d]))

for i in range(n):
    print(d[i])