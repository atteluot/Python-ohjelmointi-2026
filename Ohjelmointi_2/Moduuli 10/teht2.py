class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.nykyinen_kerros = alin_kerros

    def kerros_ylös(self):
        if self.nykyinen_kerros < self.ylin_kerros:
            self.nykyinen_kerros += 1
            print(self.tulosta_kerros())
        else:
            print("Hissi on jo ylhäällä.")

    def kerros_alas(self):
        if self.nykyinen_kerros > self.alin_kerros:
            self.nykyinen_kerros -= 1
            print(self.tulosta_kerros())
        else:
            print("Hissi on jo alhaalla.")

    def tulosta_kerros(self):
        return f"KERROS = {self.nykyinen_kerros}"

    def siirry_kerrokseen(self, kohde_kerros):
        if kohde_kerros < self.alin_kerros or kohde_kerros > self.ylin_kerros:
            print(f"Kerrosta {kohde_kerros} ei ole.")
            return

        print(f"\nMennään kerrokseen {kohde_kerros}")
        
        while self.nykyinen_kerros < kohde_kerros:
            self.kerros_ylös()
        while self.nykyinen_kerros > kohde_kerros:
            self.kerros_alas()
class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_määrä):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.hissit = []
        for i in range(hissien_määrä):
            uusi_hissi = Hissi(alin_kerros, ylin_kerros)
            self.hissit.append(uusi_hissi)


    def aja_hissiä(self, hissin_numero, kohde_kerros):
        if hissin_numero < 1 or hissin_numero > len(self.hissit):
            print(f"Hissiä numero {hissin_numero} ei ole .")
            return

        print(f"\nUusi Hissi {hissin_numero}")
        valittu_hissi = self.hissit[hissin_numero - 1]
        valittu_hissi.siirry_kerrokseen(kohde_kerros)


if __name__ == "__main__":
    print("Uusi talo (kerrokset 1-7, 3 hissiä)")
    talo = Talo(1, 7, 3)

    talo.aja_hissiä(1, 5)
    talo.aja_hissiä(2, 3)
    talo.aja_hissiä(1, 1)