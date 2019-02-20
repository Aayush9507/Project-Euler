total = 0


def amicable(n):
    sm = 0
    for i in range(1, n-1):
        if n % i == 0:
            sm = sm+i
    return sm


for x in range(1, 10000):

    v = amicable(x)
    y = amicable(v)
    if x == y and x != v:
        total = total+x
        print x
print total

