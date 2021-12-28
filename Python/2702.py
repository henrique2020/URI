arquivo = open('entrada.txt', 'r')
for linha in arquivo:
    Cd, Bd, Pd = linha.split()
    Cd = int(Cd)
    Bd = int(Bd)
    Pd = int(Pd)
    
    linha = arquivo.readline()
    Cq, Bq, Pq = linha.split()
    Cq = int(Cq)
    Bq = int(Bq)
    Pq = int(Pq)
    
    #print("C: "+Cd, Cq+" B: "+Bd, Bq+" P: "+Pd, Pq)
    insatisfeitos = 0
    if(Cd < Cq):
        insatisfeitos += (Cq-Cd)
    if(Bd < Bq):
        insatisfeitos += (Bq-Bd)
    if(Pd < Pq):
        insatisfeitos += (Pq-Pd)
    print(insatisfeitos)
arquivo.close()

# ''' Comenta várias linhas
'''
linha = input().split()
Cd, Bd, Pd = linha
Cd = int(Cd)
Bd = int(Bd)
Pd = int(Pd)
    
linha = input().split()
Cq, Bq, Pq = linha
Cq = int(Cq)
Bq = int(Bq)
Pq = int(Pq)
    
#print("C: "+Cd, Cq+" B: "+Bd, Bq+" P: "+Pd, Pq)
insatisfeitos = 0
if(Cd < Cq):
    insatisfeitos += (Cq-Cd)
if(Bd < Bq):
    insatisfeitos += (Bq-Bd)
if(Pd < Pq):
    insatisfeitos += (Pq-Pd)
print(insatisfeitos)
'''
