from math import sin

WysokoscWody =0.01       # m
SzerokoscWody =0.11      # m
PrzeplywWejsciowy =2.0   # L/min
StałaGrawitacyjna = 9.81 #m/s^2
sinA = sin(1.15)
Przyspieszenie=StałaGrawitacyjna*sinA #m/s^2
DlugoscRuryPietra = 4.0  #m
#ZmiennaKonwertujaca= lambda WysokoscWody,SzerokoscWody: (10^-3)/(60*WysokoscWody*SzerokoscWody)
DlugoscRuryPionowej =0.5 #m

#konwerter l/min->m/s
def ZmiennaKonwertujaca(WysokoscWody,SzerokoscWody):
    ZmiennaKonwertujaca=(10**(-3))/(60*WysokoscWody*SzerokoscWody)
    return float(ZmiennaKonwertujaca)