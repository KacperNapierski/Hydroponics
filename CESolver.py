import sympy as sp
import variables

def predkosc_poczatkowa(n):
    return lambda Vo: n

def czas(Vo,a,l) :
    t=sp.Symbol('t')
    f = Vo*t+0.5*a*(t**2)-l
    t=sp.solve(f)

    for i in t:
        if i>0:
            time=i
            print(time)
    return time