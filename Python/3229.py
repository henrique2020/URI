# Problema: 3229 - Resenhas de Comida  | Resposta: Time limit exceeded
# Linguagem: Python 3.11 [+1s]         | Tempo: 2.000s

def tupla(n1, n2):
    return tuple(sorted((n1, n2)))

def busca(grafo, atual, inicio, obrigatorio, opcionais, visitado, custo, memo):
    if obrigatorio.issubset(visitado) and atual == inicio:
        return custo

    chave = (atual, frozenset(visitado))
    if chave in memo and custo >= memo[chave]:
        return float('inf')
    memo[chave] = custo

    melhor = float('inf')
    n = len(grafo)

    for vizinho in range(1, n):
        peso = grafo[atual][vizinho]
        if peso == -1: continue

        aresta = tupla(atual, vizinho)

        if aresta in visitado: continue

        novo_custo = custo + peso
        visitado_att = set(visitado)

        if aresta in obrigatorio or aresta in opcionais:
            visitado_att.add(aresta)
            custo_busca = busca(grafo, vizinho, inicio, obrigatorio, opcionais, visitado_att, novo_custo, memo)
            if custo_busca < melhor:
                melhor = custo_busca

    return melhor


aeroportos, obrigatorio = map(int, input().split())
matriz = [[-1 for _ in range(aeroportos + 1)] for _ in range(aeroportos + 1)]

aeroportos_obrigatorios = set()
for _ in range(obrigatorio):
    a1, a2, valor = map(int, input().split())
    matriz[a1][a2] = matriz[a2][a1] = valor
    aeroportos_obrigatorios.add(tupla(a1, a2))

aeroportos_opcionais = set()
for _ in range(int(input())):
    a1, a2, valor = map(int, input().split())
    matriz[a1][a2] = matriz[a2][a1] = valor
    aeroportos_opcionais.add(tupla(a1, a2))

inicio = list(aeroportos_obrigatorios)[0][0]
resultado = busca(matriz, inicio, inicio, aeroportos_obrigatorios, aeroportos_opcionais, set(), 0, {})
print(resultado)
