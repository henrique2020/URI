def ciclo(atual):
    if(atual == 0):
        return atual

    return 1 / (2 + ciclo(atual-1))

print(f"{1+ciclo(int(input())):.10f}")
