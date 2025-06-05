visitantes = 0
jipes = 0

while True:
    i = input()
    if i == 'ABEND':
        print(visitantes)
        print(jipes)
        break
    else:
        t, v = i.split()
        v = int(v)
        
        if t == 'SALIDA':
            jipes += 1
            visitantes += v
        else:
            jipes -= 1
            visitantes -= v
