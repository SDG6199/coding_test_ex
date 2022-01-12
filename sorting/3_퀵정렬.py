#대부분의 경우에 가장 적합하다.
array=[7,5,9,0,3,1,6,2,4,8]

def quick_sort(array,start,end):
    if start>=end:
        return
    pivot_i=start
    left=start+1
    right=end
    while 1:
        while left<len(array) and not(array[left]>array[pivot_i]):
            left+=1
        while right>0 and not(array[right]<array[pivot_i]):
            right-=1
        
        if left>right:
            array[pivot_i],array[right]=array[right],array[pivot_i]  
            break
        else:
            array[left],array[right]= array[right],array[left]

    quick_sort(array,start,right-1)
    quick_sort(array,right+1,end)

quick_sort(array,0,len(array)-1)

print(array)
