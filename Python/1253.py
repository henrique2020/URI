for x in range(int(input())):
    entrada = input()
    cod = int(input())
    cifra = ''
    for x in entrada:
        letter = chr(ord(x)-cod)
        if(letter.isalpha() and letter.isupper()):
            cifra+=letter
        else:
            cifra+=chr(ord(letter)+26)
    print(cifra)