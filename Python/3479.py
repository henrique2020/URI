signos = {
    'aquario': ['20/01', '18/02'],
    'peixes': ['19/02', '20/03'],
    'aries': ['21/03', '20/04'],
    'touro': ['21/04', '20/05'],
    'gemeos': ['21/05', '20/06'],
    'cancer': ['21/06', '22/07'],
    'leao': ['23/07', '22/08'],
    'virgem': ['23/08', '22/09'],
    'libra': ['23/09', '22/10'],
    'escorpiao': ['23/10', '21/11'],
    'sagitario': ['22/11', '21/12'],
    'capricornio': ['22/12', '19/01']}

aniversario = input()
dA, mA = map(int, aniversario.split('/'))

sig = list(signos.keys())[-1]
for signo, datas in signos.items():
    dI, mI = map(int, datas[0].split('/'))
    dF, mF = map(int, datas[1].split('/'))
    if mI <= mA <= mF:
        if (mA == mF and dA <= dF) or (mI == mA and dI <= dA):
            sig = signo
            break

print(sig)
        
