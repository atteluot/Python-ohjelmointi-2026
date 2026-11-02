
class Lentokone:
    def __init__(self, nimi, bensa, bensamax):
        self.nimi = nimi
        self.bensa = bensa
        self.bensamax = bensamax

    def tiedot(self):
        print(f"{self.nimi}: bensaa {self.bensa}/{self.bensamax}")

class lentokenttä:
    def __init__(self, kenttänimi):
        self.kenttänimi = kenttänimi
        self.koneet = []
    def listaakone(self, kone):
        self.koneet.append(kone)
    def kaikki(self):
        print(f"{self.nimi}")
        for kone in self.koneet:
            kone.tiedot()



lentsikat = []

for i in range(1, 6):
    nimi = f"Lentokone-{i}"
    bensa = 0
    bensamax = 100
    lentsikat.append(Lentokone(nimi, bensa, bensamax))

print("--Lentokoneiden tiedot--")
for kone in lentsikat:
    kone.tiedot()



