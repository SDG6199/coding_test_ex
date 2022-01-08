y_cor=['a','b','c','d','e','f','g','h']
position=input()
for i in range(len(y_cor)):
    if position[0]==y_cor[i]:
        y=i+1
x=int(position[1])
#우측부터 반시계.
dx=[0,-1,0,1]
dy=[1,0,-1,0]
ddx=[0,-2,0,2]
ddy=[2,0,-2,0]
cnt=0
move_type_ver=[1,3]
move_type_lat=[0,2]

for i in range(4):
    if i%2==0:   #수평이동
        tx=x+ddx[i]
        ty=y+ddy[i]

        if 1<=tx and tx<=8 and 1<=ty and ty<=8:
            for j in move_type_ver:
                ttx=tx+dx[j]
                tty=ty+dy[j]

                if 1<=ttx and ttx<=8 and 1<=tty and tty<=8:
                    cnt+=1
    else:       #수직이동
        tx=x+ddx[i]
        ty=y+ddy[i]
        if 1<=tx and tx<=8 and 1<=ty and ty<=8:
            for j in move_type_lat:
                ttx=tx+dx[j]
                tty=ty+dy[j]
                if 1<=ttx and ttx<=8 and 1<=tty and tty<=8:
                    cnt+=1
print(cnt)