i = int(input('Digite a largura:'))
j = int(input('Digite a altura:'))
aux = i
while j > 0:
    while i > 0:
        print('#', end = "")
        i = i - 1
    j = j - 1
    i = aux
    print()

