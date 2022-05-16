def é_hipotenusa(n):
    i = 1
    j = 1
    while i<n:
        while j<n:
            if n**2 == i**2 + j**2:
                return (n)
            j = j+1
        i = i+1
        j = 0
    return (0)
                


def soma_hipotenusas(n):
    soma = 0
    while n >= 5:
        soma = soma + é_hipotenusa(n)
        n = n-1
    return (soma)
