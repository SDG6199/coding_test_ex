import bisect

def count_num(ls,r,l):
    result=bisect.bisect_right(ls,r)-bisect.bisect_left(ls,l)
    if result==0:
        result=-1
    return result

ls=[1,1,2,2,2,2,3]
x=1
print(count_num(ls,x,x))
