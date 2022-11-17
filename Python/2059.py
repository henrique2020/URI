p, j1, j2, r, a = map(int, input().split())

if r and a: print('Jogador 2 ganha!')
elif (r and not a) or (not r and a): print('Jogador 1 ganha!')
else:
  rp = (j1 + j2) % 2
  if (p and not rp) or (not p and rp): print('Jogador 1 ganha!')
  else: print('Jogador 2 ganha!')
