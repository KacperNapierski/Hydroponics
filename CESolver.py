import sympy as sp
import variables

def predkosc_poczatkowa(n):
    return lambda Vo: n

def WyliczanieCzasu(Vo,Przyspieszenie,DlugoscRuryPietra) :
    t=sp.Symbol('t')
    f = Vo*t+0.5*Przyspieszenie*(t**2)-DlugoscRuryPietra
    t=sp.solve(f)

    for i in t:
        if i>0:
            time=i
            print('Czas = ' + str(time))
    return time