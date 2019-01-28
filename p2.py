
a=1
b=2
list = range(0,100)
list2=[]
list3=[]
list4=[]
list3.append(a)
list3.append(b)
for i in range(len(list)):
    c=a+b
    a=b
    b=c
    # print c
    list2.append(c)
for i in list2:
    if (i<4000000):
        list3.append(i)
# print list3
for j in list3:
    if (j%2==0):
        list4.append(j)
print sum(list4)




#     list[:10]
# print list
    # while(len(list)<=4000000):
    #     print list
