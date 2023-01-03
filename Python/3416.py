#n -> Nº de estudantes
#l -> Litros que devem ser preparados por vez
#d -> Mililitros que cada estudante bebe por aula
n, l, d = map(int, input().split())
qtde_bebida = n*(d/1000)   #1L = 1000ml
cafe = qtde_bebida // l
if qtde_bebida % l != 0: cafe += 1
print(int(cafe*l))
