a=[1]*10
print(a)
##########################
array=[i**2 for i in range(0,20) if i%2==1]
print(array)
##########################
n=3; m=4
array=[[0]*m for _ in range(n)]  # nxm map
print(array)
##########################
array=[]
array.append()
array.sort()                #오름차순
array.sort(reverse=True)    #내림차순
array.insert([index], [value])
array.pop([index])
array.remove([value])
array.count([value])
array.index([value])
##########################
arr=[1,2,3,3,3,5,5,5]
while 1:
    if 3 in arr:
        arr.remove(3)
    if 5 in arr:
        arr.remove(5)
    if 3 not in arr and 5 not in arr :
        break
print(arr)

arr2=[1,2,3,3,3,5,5,5]
ref_set={3,5}
result=[i for i in arr2 if i not in ref_set]
print(result)
##########################
