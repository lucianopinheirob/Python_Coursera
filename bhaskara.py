a = int(input())
b = int(input())
c = int(input())

import math

delta = b**2 - 4*a*c

if delta > 0:
    delta = math.sqrt(delta)
    r1 = (-b+delta)/(2*a)
    r2 = (-b-delta)/(2*a)
    print("as raízes da equação são",r2,"e",r1)
elif delta == 0:
    r = (-b)/(2*a)
    print("a raíz desta equação é",r)
else:
    print("esta equação não possui raízes reais")

    
