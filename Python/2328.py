int(input())
pedacos = 0
n = list(map(int, input().split()))
for div in n:
    pedacos+=(div-1)
    div-=1
print(pedacos)
