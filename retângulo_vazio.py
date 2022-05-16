i = int(input('Digite a largura:'))
j = int(input('Digite a altura:'))
aux1 = i
aux2 = j
while j > 0:
    while i > 0:
        if j == 1 or j == aux2 or i == 1 or i == aux1:
            print('#', end = "")
        else:
            print(' ', end = "")
        i = i - 1
    j = j - 1
    i = aux1
    print()

