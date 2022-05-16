lis = []
i = 0
j = 0
n = 1
while n != '0':
    n = input()
    lis.append(n)
del lis[-1]
lis_inv = []
while i <= len(lis)-1:
    lis_inv.append(lis[len(lis)-1-i])
    i = i+1
for i in lis_inv:
    print(i)
