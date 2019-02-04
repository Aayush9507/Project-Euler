def factor_count(n):
    total = 2
    for j in range(2, n/2+1):
        if n % j == 0:
            # print j
            total = total+1
    return total


def factor_odd_count(n):
    total = 2
    for j in xrange(2,((n+1)/2)+1):
        if n%j == 0:
            # print j
            total = total + 1
    return total


for i in xrange(5000, 1000000):
    t = i*(i+1)/2
    if t % 2 != 2:
        n = factor_odd_count(t)
        if n >= 500:
            print t
            break
    else:
        n = factor_count(t)
        if n >= 500:
            print t
            break