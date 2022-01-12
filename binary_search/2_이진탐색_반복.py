def binary_search(ls,target,start,end):
    if start>end:
        return 
    while not(start>end):
        mid=(start+end)//2
        if ls[mid]==target:
            return mid
        if ls[mid]<target:
            start=mid+1
        else:
            end=mid-1

ls=[1,5,9,8,4,9,7,5,1,5,9,1]
ls.sort()
print(ls)
target=8
print(binary_search(ls,target,0,len(ls)-1))