def n_primos(n):
    i = 1
    j = 0
    k = 0
    while n >= 2:
        while i <= n:
            if n%i == 0:
                j = j+1
            i = i+1
        if j == 2:
            k = k+1
        n = n - 1
        i = 1
        j = 0
    return (k)
        
        
