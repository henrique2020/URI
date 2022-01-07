quebra, fim = map(int, input().split())
ini = 1
while(ini <= fim):
    if (ini%quebra == 0):
        print(ini)
    else:
        print(ini, end=' ')
    ini+=1
