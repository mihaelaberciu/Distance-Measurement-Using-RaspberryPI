from modul_senzor import calcul_distanta
from modul_bluetooth import bluetooth_afisare
while True:
    distanta=calcul_distanta()
    bluetooth_afisare(distanta)