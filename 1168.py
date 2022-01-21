import numbers


leds = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6] ##[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for x in range(int(input())):
    number = input()
    qtde = 0
    for x in number:
        qtde+=leds[int(x)]
    print(f'{qtde} leds')