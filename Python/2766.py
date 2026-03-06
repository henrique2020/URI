# Problema: 2766 - Entrada e Saída Lendo e Pulando Nomes | Resposta: Accepted
# Linguagem: Python 3.11 [+1s]                           | Tempo: 0.005s

linhas = [input() for _ in range(10)]
print(*[linhas[i] for i in [2,6,8]], sep='\n')
