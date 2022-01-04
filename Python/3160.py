amigos = input().split()
n_amigos = input()
indicacao = input()

if indicacao.lower() == 'nao':
    amigos.append(n_amigos)
else:
    amigos.insert(amigos.index(indicacao), n_amigos)
print(" ".join(amigos))
