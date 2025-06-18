def ciclo(atual):
    if(atual == 0):
        return atual

    return 1 / (6 + ciclo(atual-1))

print(f"{3+ciclo(int(input())):.10f}")
