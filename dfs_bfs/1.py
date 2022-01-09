def factorial_recur(n):
    if n<=1:
        return 1
    return n*factorial_recur(n-1)
print(factorial_recur(5))

def gcd_recur(a,b):
    if a%b==0:
        return b
    return gcd_recur(b,a%b)
print(gcd_recur(192,162))