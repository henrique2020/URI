tamanho = int(input())
count = 1
seq = int(input())
while(tamanho-1):
    num = int(input())
    if seq != num:
        count+=1
        seq = num
    tamanho-=1

print(count)
