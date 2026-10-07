import math
def  is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 ==0:
        return False
    m=int(math.sqrt(n))
    for x in range(3,m+1,2):
        if n % x ==0:
            return False
    return True
print(is_prime)

