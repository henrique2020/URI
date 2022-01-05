## Primeira versão - 0.456s
arr = []
arr.append(int(input()))
arr.append(int(input()))
soma = 0
ini = min(arr)
fim = max(arr)
while ini <= fim:
    if ini%13 != 0:
        soma+=ini
    ini+=1
print(soma)

##Segunda versão - 0.111s
arr = []
arr.append(int(input()))
arr.append(int(input()))
arr.sort()
soma = 0
for x in range(arr[0], arr[1]+1):
    if x%13 != 0:
        soma+=x
print(soma)
