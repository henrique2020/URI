rep = int(input())
while(rep):
    arrays = int(input())
    count = 0
    i = 0
    while(arrays):
        string = input()
        tamanho = len(string)
        while(tamanho):
            count += (ord(string[tamanho-1])-65) + tamanho-1 + arrays-1
            tamanho -= 1
        arrays -= 1
    print(count)
    rep -= 1
