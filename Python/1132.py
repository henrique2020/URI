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
