class Inventaario:
    tavarat = []

    def lisää(self, tavara):
        self.tavarat.append(tavara)

    def tulosta_tavarat(self):
        if not self.tavarat:
            print("Varasto on tyhjä.")
        else:
            print("Varaston sisältö:")
            for tavara in self.tavarat:
                print(f"{tavara}")
varasto = Inventaario()


while True:
    syöte = input("Anna tavara:")
    varasto.lisää(syöte)
    varasto.tulosta_tavarat()


