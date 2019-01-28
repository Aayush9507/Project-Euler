list = []
x = 0
y = 0
for i in range(100, 999):
    for j in range(100, 999):
        num = i*j
        reverse = 0
        temp = num
        while temp != 0:
            reverse = (reverse*10)+temp % 10
            temp = temp//10
        if num == reverse:
            list.append(num)
print max(list)