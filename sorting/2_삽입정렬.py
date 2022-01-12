#데이터가 거의 정렬되어있을때 가장 빠르다.
array=[7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)-1):
    start=i+1
    while start>0:
        if array[start-1]>array[start]:
            array[start-1], array[start]= array[start], array[start-1]
            start-=1
        else:
            break
print(array)