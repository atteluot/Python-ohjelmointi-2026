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

        print(f"\nSiirrytään kerrokseen {kohde_kerros}")
        
        while self.nykyinen_kerros < kohde_kerros:
            self.kerros_ylös()
        while self.nykyinen_kerros > kohde_kerros:
            self.kerros_alas()

if __name__ == "__main__":
    h = Hissi(1, 10)

    print(h.tulosta_kerros())
    
    h.siirry_kerrokseen(5)
    h.siirry_kerrokseen(h.alin_kerros)
    
    print(h.tulosta_kerros())
