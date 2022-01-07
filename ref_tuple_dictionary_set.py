##########################
#tuple  //순서o, 수정불가
#서로 다른 성질의 데이터를 묶어서 보관할 때
#ex)(학번, 성적), (비용, 노드번호)
#키 값으로 사용할 때
a=(1,2,3,4,5,6,7,8,9)

##########################
#dictionary //순서x(즉, indexing 못함. index대신 key사용)
data=dict()
data['apple']='a'
data['banana']='b'
data['coconut']='c'
if 'apple' in data:
    print("사과있노")
key_list=data.keys()
value_list=data.values()
for key in key_list:
    print(data[key])

##########################
#set //수정불가, 중복허용x, 순서x(즉, indexing 못함. 무조건 오름차순)
even_set=set([i for i in range(10) if i%2==0])
odd_set=set([i for i in range(10) if i%2==1])
all_set=set([i for i in range(10)])
print(odd_set|even_set)
print(all_set&even_set)
print(all_set-even_set)
all_set.add(13)             #1개 원소 추가
all_set.update([11,12])     #여러개 원소 추가
all_set.remove(12)
print(all_set)
print(10 in all_set)

##########################
