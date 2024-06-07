while True:
    try: pos = int(input())
    except: break

    if 0 <= pos < 90 or pos == 360: print('Bom Dia!!')
    elif 90 <= pos < 180: print('Boa Tarde!!')
    elif 180 <= pos < 270: print('Boa Noite!!')
    elif 270 <= pos: print('De Madrugada!!')
