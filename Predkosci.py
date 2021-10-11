from sympy.core.symbol import var
from CESolver import WyliczanieCzasu, predkosc_poczatkowa
import variables


#ZmiennaKonwertujaca= lambda WysokoscWody,SzerokoscWody: (10**-3)/(60*WysokoscWody*SzerokoscWody)
PredkoscWejsciowa=variables.PrzeplywWejsciowy*variables.ZmiennaKonwertujaca(variables.WysokoscWody,variables.SzerokoscWody)
print('predkosc wejsciowej wody =' + str(PredkoscWejsciowa))

#górna warstwa
CzasPierwszegoEtapu = WyliczanieCzasu(variables.ZmiennaKonwertujaca(variables.WysokoscWody,variables.SzerokoscWody)*variables.PrzeplywWejsciowy, variables.Przyspieszenie, variables.DlugoscRuryPietra)
PredkoscPierwszegoEtapu=variables.ZmiennaKonwertujaca(variables.WysokoscWody,variables.SzerokoscWody)*variables.PrzeplywWejsciowy + variables.Przyspieszenie*float(CzasPierwszegoEtapu)
print('predkosc na koncu gory ' + str(PredkoscPierwszegoEtapu))


#pion
CzasDrugiegoEtapu = WyliczanieCzasu(PredkoscPierwszegoEtapu, variables.StałaGrawitacyjna , variables.DlugoscRuryPionowej)
PredkoscDrugiegoEtapu=PredkoscPierwszegoEtapu + variables.StałaGrawitacyjna*CzasDrugiegoEtapu
print('predkosc na koncu rury czesci '+ str(PredkoscDrugiegoEtapu))

#dol
CzasTrzeciegoEtapu= WyliczanieCzasu (PredkoscDrugiegoEtapu, variables.Przyspieszenie, variables.DlugoscRuryPietra)
PredkoscTrzeciegoEtapu=PredkoscDrugiegoEtapu + variables.Przyspieszenie*CzasTrzeciegoEtapu
print('predkosc na koncu dolnej czesci ' + str(PredkoscTrzeciegoEtapu))

#konwersja na l/min
print('Przepływ wyjściowy = ' + str(PredkoscTrzeciegoEtapu/variables.ZmiennaKonwertujaca(variables.WysokoscWody,variables.SzerokoscWody)))