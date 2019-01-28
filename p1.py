
list2 = []
list=range(0,1000)
for i in range(len(list)):
    if (i%3==0 or i%5==0):
        list2.append(i)
print sum(list2)