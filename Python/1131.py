grenais = 0
vI = 0
vG = 0
e = 0
while True:
    i, g = map(int, input().split())
    if g>i:
        vG+=1
    elif i>g:
        vI+=1
    else:
        e+=1
    grenais+=1
    print('Novo grenal (1-sim 2-nao)')
    novo = input()
    if(novo == '2'):
        break

print(f'{grenais} grenais')
print(f'Inter:{vI}')
print(f'Gremio:{vG}')
print(f'Empates:{e}')
if vG>vI:
    print('Gremio venceu mais')
elif vI>vG:
    print('Inter venceu mais')
else:
    print('Nao houve vencedor')
