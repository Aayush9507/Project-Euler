q = 0

for i in range(1, 500):
    for j in range(1, 1000):
        for k in range(1, 1000):
            if(i < j < k) and (i*i)+(j*j) == (k*k) and i+j+k == 1000:

                p = i*j*k
                if p > q:
                    q = p

print q


