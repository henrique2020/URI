for _ in range(int(input())):
    n = int(input())
    notas = list(map(int, input().split()))
    notas_ordernadas = sorted(notas, reverse=True)
    
    count = 0
    for i in range(n):
        if(notas[i] == notas_ordernadas[i]): 
            count+= 1
    
    print(count)
