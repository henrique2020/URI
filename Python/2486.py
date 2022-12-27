vitaminas = {
    'suco de laranja': 120,
    'morango fresco': 85,
    'mamao': 85, 
    'goiaba vermelha': 70, 
    'manga': 56, 
    'laranja': 50, 
    'brocolis': 34
}

while True:
    alimentos = int(input())
    if alimentos == 0: break
    
    mg = 0
    for _ in range(alimentos):
        qtde, alimento = input().split(maxsplit=1)
        qtde = int(qtde)
        mg += qtde * vitaminas[alimento]
        
    if mg < 110: print(f'Mais {110 - mg} mg')
    elif mg > 130:  print(f'Menos {mg - 130} mg')
    else: print(f'{mg} mg')
