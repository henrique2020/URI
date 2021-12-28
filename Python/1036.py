import math

valores = input().split()

A, B, C = valores

A = float(A)
B = float(B)
C = float(C)

delta = (B*B)-(4*C*A)

if A == 0 or delta < 0:
    print("Impossivel calcular")
else:
    raiz = math.sqrt(delta)
    R1 = ((-B)+raiz)/(A*2)
    R2 = ((-B)-raiz)/(A*2)
    print("R1 = %.5f\nR2 = %.5f" %(R1,R2))
