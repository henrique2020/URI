l, c = map(int, input().split())

vida = []
disciplina = []
for x in range(l):
    var = input().split()
    for p in var:
        if p[-1].upper() == 'V': vida.append(p)
        else: disciplina.append(p)
        
vida.sort(reverse=True)
print("\n".join(vida))

disciplina.sort(reverse=True)
print("\n".join(disciplina))
