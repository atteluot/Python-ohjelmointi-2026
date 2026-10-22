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

auto = Auto("KKL-246", 150)

auto.kiihdytä(30)
print(f"nopeus: {auto.nopeus} km/h")
auto.kiihdytä(70)
print(f"nopeus: {auto.nopeus} km/h")
auto.kiihdytä(50)
print(f"nopeus: {auto.nopeus} km/h")
auto.kiihdytä(-200)
print(f"nopeus: {auto.nopeus} km/h")
print("")
print("AUTO")
print(f"Rekisteritunnus: {auto.rekkari}")
print(f"Huippunopeus: {auto.huippunopeus} km/h")
print(f"Nopeus: {auto.nopeus} km/h")
print(f"Matka: {auto.matka}")