##Time limit exceded

qtde = int(input())
quadradonia = input().split()
quadradonia.sort(key=int)
quadradonia = list(map(int, quadradonia))

noglonia = input().split()
noglonia.sort(key=int)
noglonia = list(map(int, noglonia))

vit_nog = 0
for exercitoQ in quadradonia:
    n_entrou = True
    for exercitoN in noglonia:
        if exercitoN > exercitoQ:
            vit_nog += 1
            noglonia.remove(exercitoN)
            n_entrou = False
            break
    
    if n_entrou:
        noglonia.pop(0)

print("%d" % vit_nog)
