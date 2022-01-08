a=input()
result=""
sum=0
for i in a:
    if i.isalpha():
        result+=i
    else:
        sum+=int(i)
result="".join(sorted(result))
if sum!=0:
    result+=str(sum)
print(result)
