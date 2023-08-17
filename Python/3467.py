while True:
    try: sofa = input().upper()
    except: break
    
    lugar_sheldon = 3
    print("Esse eh o meu lugar" if lugar_sheldon == sofa.find('L')+1 else "Oi, Leonard")