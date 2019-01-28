import math

list2 = []
def IsNumberPrime(n):
    bounds = int(math.sqrt(n))
    for number in xrange(2, bounds+2):
        if n % number == 0:
            return False
    return True

for i in xrange(3, int(math.sqrt(600851475143))):
    if 600851475143 % i == 0:
        list2.append(i)
for j in list2:
    if IsNumberPrime(j):
        print j

