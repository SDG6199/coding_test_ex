#20:48
move_type=[(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(-1,2),(1,-2),(-1,-2)]
position=input()
x=int(position[1])
y=ord(position[0])-ord('a')+1
cnt=0
for dir in move_type:
    tx=x+dir[0]
    ty=y+dir[1]
    if 1<=tx and tx<=8 and 1<=ty and ty<=8:
        cnt+=1
print(cnt)
    
