import time
#통상 연산 1억번당 1~3초
tic=time.time()
for i in range(1,100000000):
    pass
toc=time.time()
print(tic-toc)
##########################
a=1.23456e2
print(round(a,2))
##########################
