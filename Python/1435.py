while True:
    n = int(input())
    if n == 0: break
    
    matriz = [[0 for j in range(n)] for i in range(n)]
    
    for i in range(n):
        for j in range(i, n - i):
            matriz[i][j] = matriz[j][i] = matriz[n-i-1][j] = matriz[j][n-i-1] = i+1
            
    for i in range(n):
        for j in range(n):
            if j == n - 1:
                print(f"{matriz[i][j]:3}")
            else:
                print(f"{matriz[i][j]:3}", end=' ')
    print()
