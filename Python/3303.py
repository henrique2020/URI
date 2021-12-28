while True:
    try: palavra = input()
    except: break

    if len(palavra) >= 10:
        print('palavrao')
    else:
        print('palavrinha')
