import math
def is_prime(n=1013):
    if n<2:
        return False
    if n == 2:
        return True
    if n%2:
        return False
    m=math.sqrt(n)
    m=int(m)+1
    for i in range(3,m+1,2):
        if n%x==0:
            return False
    return True
def is_prime3(n=1013):
    if n==2:
        return True #2 is prime
    if n%2 ==0:
        return False
    if n <2:
        return False
    prime = True
    for x in range(3,n+1,2):
        if n%x == 0:
            prime = False
            return prime
    return prime
import timeit
t1 = timeit.timeit(is_prime3)
t2 = timeit.timeit(is_prime)
print(t1,t2,t1/t2)