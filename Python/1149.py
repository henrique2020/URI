entrada = list(map(int, input().split()))
a = entrada[0]
for x in range(1, len(entrada)):
    if entrada[x] > 0:
        b = entrada[x]-1
        break

soma = a
while b:
    soma+=a+b
    b-=1
print(soma)
