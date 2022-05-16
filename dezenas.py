n = (input("Digite um número inteiro:"))
n = int(n)
if (n<10):
    print(0)
else:
    while(n>100):
        n = n//10
        print(n)
    print(n%10)
    
