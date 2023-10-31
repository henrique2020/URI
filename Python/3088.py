while True:
    try: texto = input()
    except: break

    texto = texto.replace(' ,', ',')
    texto = texto.replace(' .', '.')
    print(texto)
