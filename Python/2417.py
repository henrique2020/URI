Cv, Ce, Cs, Fv, Fe, Fs = map(int, input().split())
Cp = (Cv * 3) + Ce
Fp = (Fv * 3) + Fe

if(Cp == Fp):
    Cp += Cs
    Fp += Fs

print('C' if Cp > Fp else 'F' if Cp < Fp else '=')