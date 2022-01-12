n=5
k=3
array_a=[1,6,5,1,4,5,1,5,6,1]
array_b=[4,5,6,1,2,6,5,1,5,8]
array_a.sort()
array_b.sort(reverse=True)
print(array_a, array_b)
for i in range(k):
    if array_a[i]<array_b[i]:
        array_a[i],array_b[i]=array_b[i],array_a[i]
    else:
        #array_a의 최소값이 array_b의 최대값보다 크면 swap안해도된다.
        break
print(sum(array_a))
