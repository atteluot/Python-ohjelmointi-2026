import random
class Auto:
    def __init__(self, rekkari, huippunopeus):
        self.rekkari = rekkari
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

    def kiihdytä(self, muutos):
        self.nopeus = self.nopeus + muutos

        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        
        elif self.nopeus < 0:
            self.nopeus = 0




    def kulje(self, aika):
        self.matka = self.matka + self.nopeus * aika

class Sähkö(Auto):

    def __init__(self, rekkari, huippunopeus, kwh):
        super().__init__(rekkari, huippunopeus)
        self.akkukapasiteetti = kwh
class bensa(Auto):
    def __init__(self, rekkari, huippunopeus, koko):
        super().__init__(rekkari, huippunopeus)
        self.tankin_koko = koko
        
bensa_auto = bensa("ACD-123", 165, 32.3)
sähköauto = Sähkö("ABC-15", 180, 52.5)   

sähköauto.kiihdytä(100)
bensa_auto.kiihdytä(120)

sähköauto.kulje(3)
bensa_auto.kulje(3)

print(f"{sähköauto.rekkari}: matkamittari {sähköauto.matka} km")
print(f"{bensa_auto.rekkari}: matkamittari {bensa_auto.matka} km")