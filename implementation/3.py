n=int(input())
cnt=(n*60+59)*60+59
check_cnt=0

for i in range(cnt+1):
    s=i%60
    m=(i//60)%60
    h=(i//60)//60
    t_str=str(h)+str(m)+str(s)
    if '3' in list(t_str):
        check_cnt+=1
print(list(t_str))
print(check_cnt)