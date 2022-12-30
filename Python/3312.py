import math
def primo(num):
    if (num%2 == 0 and num > 2) or num == 1:
        return False
    return all(num%i for i in range(3, int(math.sqrt(num))+1, 2))


def fat(num):
    fatorial = 1
    for i in range(1, num+1): fatorial *= i
    return fatorial


input()
entradas = list(map(int, input().split()))
for num in entradas:
    if primo(num):
        print(f'{num}! = {fat(num)}')
