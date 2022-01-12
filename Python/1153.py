valor = int(input())

fat = 1
for x in range(0, valor):
    fat *= valor-x
print(fat)
