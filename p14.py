
def method(j):
    list=[]

    if j % 2 == 0:
        k = j/2

        list.append(k)
        if k == 1:
            print len(list)+1
        else:
            method(k)
    elif j % 2 != 0:
        k = j*3+1

        list.append(k)
        if k == 1:
            print len(list)+1
        else:
            method(k)

for f in range(1,13):
    method(f)