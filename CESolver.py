import sympy as sp
import variables

def PredkoscPoczatkowa(n):
    return lambda Predkosc: n

def WyliczanieCzasu(Predkosc,Przyspieszenie,DlugoscRuryPietra) :
    Czas=sp.Symbol('Czas')
    f = Predkosc*Czas+0.5*Przyspieszenie*(Czas**2)-DlugoscRuryPietra
    Czas=sp.solve(f)

    for Iteracja in Czas:
        if Iteracja>0:
            Time=Iteracja
            print('Czas = ' + str(Time))
    return Time