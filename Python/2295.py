pA, pG, rA, rG = input().split()
pA = float(pA)
pG = float(pG)
rA = float(rA)
rG = float(rG)

alcool = rA/pA
gasolina = rG/pG

if alcool > gasolina:
    print('A')
else:
    print('G')
    
