import math

arr = []


def is_prime(n):
    bounds = int(math.sqrt(n))
    for number in xrange(2, bounds + 2):
        if n % number == 0:
            return False
    return True


for i in xrange(0, 1000000):
    if is_prime(i):
        arr.append(i)
print (arr[10001])
