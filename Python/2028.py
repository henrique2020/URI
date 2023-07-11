i = 1
while True:
    try: n = int(input())
    except: break
    
    num = ['0']
    [num.extend(' '.join([str(x)]*x).split()) for x in range(1, n+1)]
    
    s = 's' if len(num) > 1 else ''
    print(f'Caso {i}: {len(num)} numero{s}')
    print(' '.join(num))
    print()
    
    i+= 1