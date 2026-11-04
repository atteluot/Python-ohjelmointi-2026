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

class Kilpailu:
    def __init__(self, nimi, pituus, autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot

    def tunti(self):
       for auto in self.autot:
            auto.kiihdytä(random.randint(-10, 15))
            auto.kulje(1)

    def tulostatilanne(self):
        print(f"{self.nimi}")
        for auto in self.autot:
            print(f"Rekkari={auto.rekkari}, Huippunopeus={auto.huippunopeus} km/h, Nopeus={auto.nopeus} km/h, Matka={auto.matka} km")

    def kilpailuloppu(self):
        for auto in self.autot:
            if auto.matka >= self.pituus:
        

autot = []
for i in range(1, 11):
    rekisteri = f"ABC-{i}"
    huippu = random.randint(100, 200)
    autot.append(Auto(rekisteri, huippu))

kilpailu = Kilpailu("Suuri romuralli", 8000, autot)
tunnit = 0

while not kilpailu.kilpailuloppu():
    kilpailu.tunti()
    tunnit += 1
    if tunnit % 10 == 0:
        kilpailu.tulosta_tilanne()

kilpailu.tulostatilanne()


#############################################################################
autot = []
for i in range (1,11):
    rekisteri = f"ABC-{i}"
    huippu = random.randint(100, 200) 
    autot.append(Auto(rekisteri, huippu))
maali = 1
while True:
     
    for auto in autot:
        auto.kiihdytä(random.randint(-10, 15))
        auto.kulje(1)
        if auto.matka >= 10000:
            maali = maali + 1
    if maali >= 2:
        break
    
for auto in autot:
    print(f"Rekkari = {auto.rekkari},   Huippunopeus = {auto.huippunopeus} km/h,   Nopeus = {auto.nopeus} km/h,   Matka = {auto.matka} km")