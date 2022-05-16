def maior_elemento(lista):
#Ordenando a Lista
    i = 0
    j = 0
    while i < len(lista):
        j = i
        while j < len(lista)-1:
            if lista[i] > lista[j+1]:
                aux = lista[i]
                lista[i] = lista[j+1]
                lista[j+1] = aux
            j = j+1
        i = i+1

    return lista[-1]
   
