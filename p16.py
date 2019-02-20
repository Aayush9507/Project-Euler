
import math

n = math.pow(2,1000)
m = long(n)
s = 0
while m:
    s += m % 10
    m //= 10
print s
