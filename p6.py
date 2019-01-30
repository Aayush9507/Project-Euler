list=[]
total = sum(range(1, 101))
total=total*total
for i in range(1,  101):
    i=i*i
    list.append(i)
sq = sum(list)
print total-sq

