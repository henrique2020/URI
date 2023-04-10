n_alunos = int(input())

matricula, nota = input().split()
nota = float(nota)

for _ in range(1, n_alunos):
    m, n = input().split()
    n = float(n)
    if nota < n:
        matricula = m
        nota = n

if nota < 8: print('Minimum note not reached')
else: print(matricula)