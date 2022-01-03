abertura = float(input())
count = 0
for x in range(0, int(input())):
    estrela = float(input())
    fotons = estrela*abertura/10000000
    if(fotons >= 4):
        count+=1
print(count)
