##########################
a=2.123
print("%05.2f" %a)
print('Hello Python!',end='')  #줄바꿈제거
print('Hello Python!'.center(20))
print('Hello Python!'.rjust(20))
print('Hello Python!'.ljust(20))
print('Hello Python!'.zfill(20))
print('hello python!'.capitalize())
print('hello python!'.title())
print('hello python!'.upper())
print('HELLO PYTHON!'.lower())
print('HeLlO pYtHoN!'.swapcase())
print('HeLlO pYtHoN!'.strip('!'))
##########################
print(float('1.1'))
print(eval("(3+5)*7"))
str=input()
int_a,int_b=map(int,input().split(' '))
data=list(map(int,input().split(' ')))
print(str)
print('%d %d' %(int_a,int_b))
print(data)
##########################
a=1;b=2;c=3
print(a,b,c,sep=',')
##########################
print(list("hesda"))
print("".join(list("hesda")))
