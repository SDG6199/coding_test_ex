#문자열 최대값
data=input()
pre=int(data[0])
for i in range(1,len(data)):
    now=int(data[i])
    if pre<=1 or now<=1:
        pre+=now
    else:
        pre*=now
    
print(pre)
     

