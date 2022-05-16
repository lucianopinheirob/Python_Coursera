def maior_primo(n):
    i = 1
    j=3
    while j > 2:
        j = 0
        while i <= n:
            if n%i == 0:
                j = j+1
            i = i + 1
        i = 1
        n = n - 1
    return (n+1)

