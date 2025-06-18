for _ in range(int(input())):
    garrafas, troca = map(int, input().split())
    print(garrafas//troca + garrafas%troca)
