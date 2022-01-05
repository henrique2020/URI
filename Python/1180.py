input()
arr = list(map(int, input().split()))
print(f'Menor valor: {min(arr)}')
print(f'Posicao: {arr.index(min(arr))}')
