# Problema: 2582 - System of a Download | Resposta: Accepted
# Linguagem: Python 3.11 [+1s]          | Tempo: 0.000s

import sys

playlist = (
    "PROXYCITY", "P.Y.N.G.", "DNSUEY!",
    "SERVERS", "HOST!", "CRIPTONIZE",
    "OFFLINE DAY", "SALT", "ANSWER!",
    "RAR?", "WIFI ANTENNAS"
)

data = iter(sys.stdin.read().split())
t = int(next(data))

res = []
for _ in range(t):
    b1 = int(next(data))
    b2 = int(next(data))
    res.append(playlist[b1 + b2])

print("\n".join(res))
