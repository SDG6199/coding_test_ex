a=input()
num_char=sorted(a)
result_str=""
result_num=0
char_ls=[chr(i) for i in range(ord('A'),ord('A')+26)]
for i in num_char:
    if i in char_ls:
        result_str+=i
    else:
        result_num+=int(i)
print(result_str+str(result_num))
