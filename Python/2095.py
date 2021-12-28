qtde = int(input())
quadradonia = list(map(int, input().split()))
quadradonia.sort()

noglonia = list(map(int, input().split()))
noglonia.sort()

vit = 0
exercitoN = 0
for exercitoQ in quadradonia:
    while(exercitoN < len(noglonia)):
        if noglonia[exercitoN] > exercitoQ:
            vit += 1
            exercitoN += 1
            break
        exercitoN += 1
    
print("%d" % vit)
