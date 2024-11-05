def max_enfeites(galho, pacotes, capacidade_peso):
    dp = [0] * (capacidade_peso + 1)
    for enfeites, peso in pacotes:
        for w in range(capacidade_peso, peso - 1, -1):
            dp[w] = max(dp[w], dp[w - peso] + enfeites)
            
    return dp[capacidade_peso]


galhos = int(input())

for i in range(galhos):
    n_pacotes = int(input())
    m_peso = int(input())
    pacotes = []

    for _ in range(n_pacotes):
        n_enfeites, peso_pacote = map(int, input().split())
        pacotes.append((n_enfeites, peso_pacote))

    max_enfeites_galho = max_enfeites(i + 1, pacotes, m_peso)

    print(f"Galho {i + 1}:")
    print(f"Numero total de enfeites: {max_enfeites_galho}")
    print()
