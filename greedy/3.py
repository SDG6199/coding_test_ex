grp_cnt=0; mem_cnt=0

n=int(input())
ls=list(map(int,input().split()))
ls.sort()

for i in ls:
    mem_cnt+=1
    if mem_cnt>=i:
        mem_cnt=0
        grp_cnt+=1
print(grp_cnt)
