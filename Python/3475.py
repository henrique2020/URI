words = ["zero", "um", "dois", "tres", "quatro", "cinco", "seis", "sete", "oito", "nove"]
n = input()
if n.isnumeric(): print(words[int(n)])
elif n in words: print(words.index(n))
