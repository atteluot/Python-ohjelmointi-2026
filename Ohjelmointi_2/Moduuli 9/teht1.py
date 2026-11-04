#Lisäsin yhden extran, että tajuan vähän miten toimii

class Auto:
    def __init__(self, rekkari, nopeus):
        self.rekkari = rekkari
        self.nopeus = nopeus
        self.vauhti = 0
        self.matka = 0
###########################################
mersu = Auto("VXY-231", 66) #tämä on extra#
###########################################
auto = Auto("KKL-246", 123)

print("AUTO")
print(f"Rekisteritunnus: {auto.rekkari}")
print(f"Huippunopeus: {auto.nopeus} km/h")
print(f"Nopeus: {auto.vauhti} km/h")
print(f"Matka: {auto.matka}")
#######################
#tästä alaspäin extraa#
#######################
print("MERSU")
print(f"Rekisteritunnus: {mersu.rekkari}")
print(f"Huippunopeus: {mersu.nopeus} km/h")
print(f"Nopeus: {mersu.vauhti} km/h")
print(f"Matka: {mersu.matka}")