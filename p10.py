list=[]


to=0
for p in range(2, 2000000):
    for i in range(2, p):
        if p % i == 0:
            break
    else:
        list.append(p)
for j in list:
    to=to+j
print to
