n = int(input())

aux1 = n//10
aux2 = n%10
aux3 = 0

while aux1 >= 0:
    aux2 = aux2 + aux3
    if aux1 == 0:
        break
    aux3 = aux1%10
    aux1 = aux1//10

print(aux2)
