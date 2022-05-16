n = int(input())

adj = False

aux1 = n%10
aux2 = n//10

while aux2 != 0 and not adj:
    aux3 = aux2%10
    if aux1 == aux3:
        adj = True
    aux2 = aux2//10
    aux1 = aux3

if (adj):
    print("sim")
else:
    print("não")
        
