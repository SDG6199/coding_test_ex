array=[7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)):
    start_i=i+1
    min_val_i=i
    for j in range(start_i,len(array)):
        if array[j]<array[min_val_i]:
            min_val_i=j
    if array[min_val_i]<array[i]:
        array[i],array[min_val_i] = array[min_val_i],array[i]

print(array)
        