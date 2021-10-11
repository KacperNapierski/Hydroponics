from sympy.core.symbol import var
from CESolver import czas, predkosc_poczatkowa
import variables


#x= lambda hw,sw: (10**-3)/(60*hw*sw)
y=variables.Pwy*variables.x(variables.hw,variables.sw)
print('predkosc wejsciowej wody =' + str(y))

#górna warstwa
t = czas(variables.x(variables.hw,variables.sw)*variables.Pwy, variables.a, variables.l)
Vk=variables.x(variables.hw,variables.sw)*variables.Pwy + variables.a*float(t)
print('predkosc na koncu gory ' + str(Vk))


#pion
t2 = czas(Vk, variables.g , variables.s)
Vk2=Vk + variables.g*t2
print('predkosc na koncu rury czesci '+ str(Vk2))

#dol
t3= czas (Vk2, variables.a, variables.l)
Vk3=Vk2 + variables.a*t3
print('predkosc na koncu dolnej czesci ' + str(Vk3))

#konwersja na l/min
print('Pwe = ' + str(Vk3/variables.x(variables.hw,variables.sw)))