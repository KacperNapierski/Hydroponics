from math import sin

hw =0.01
sw =0.11
Pwy =2.0
g = 9.81
sinA = sin(1.15)
a=g*sinA
l = 4.0
#x= lambda hw,sw: (10^-3)/(60*hw*sw)
s =0.5

#konwerter l/min->m/s
def x(hw,sw):
    x=(10**(-3))/(60*hw*sw)
    return float(x)