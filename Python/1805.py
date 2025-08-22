ini, fim = map(int, input().split())

num = fim-ini
soma = ini+fim
if(num % 2 == 0):
    rep = num/2
    result = soma*rep + fim-rep
else:
    rep = (num+1)/2
    result = soma*rep

print(int(result))
