pi = 3.14
while True:
    try: 
        volume = float(input())
        diametro = float(input())
    except: break
    
    r = diametro / 2
    area = pi * r ** 2
    altura = volume / area
    
    print('ALTURA = {:.2f}'.format(altura))
    print('AREA = {:.2f}'.format(area))