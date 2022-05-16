n = int(input())
fat = 1
if n == 0:
    print(fat)
else:
    while n > 0:
        fat = n*fat
        n = n-1
    print(fat)
