#동일한 값을 가지는 데이터가 여러 개일때 적합하다.
array=[7,5,9,0,3,1,0,6,2,4,8]
coef_ls=[0]*(max(array)+1)
#index:0~9인 list.
result=[]
for i in array:
    coef_ls[i]+=1
for i in range(len(coef_ls)):
    for j in range(coef_ls[i]):
        result.append(i)
print(result)