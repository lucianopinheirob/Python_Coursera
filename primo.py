n = int(input())
i = 1
j=0
while i <= n:
    if n%i == 0:
        j = j+1
    i = i + 1
if j == 2:
    print("primo")
else:
    print("não primo")
