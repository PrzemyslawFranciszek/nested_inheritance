class Zwierze:
    def __init__(self, nazwa, wiek, waga):
        self.nazwa = nazwa
        self.wiek = wiek
        self.waga = waga

    def przedstaw_sie(self):
        print(f"Jestem zwierzakiem {self.nazwa}, mam {self.wiek} lat oraz ważę {self.waga} kg.")

    def urodziny(self):
        self.wiek += 1
class Slon(Zwierze):
    def przedstaw_sie(self):
        print(f"Jestem słoniem {self.nazwa}, mam {self.wiek} oraz ważę {self.waga} kg")

class Lew(Zwierze):
    def przedstaw_sie(self):
        super().przedstaw_sie()
        print("A tak w ogóle jestem lwem")


class Papuga(Zwierze):
    pass

def main():
    Dumboo = Slon("Dumboo", 77, 600)
    Simba = Lew("Simba", 24, 100)
    Jago = Papuga("Jago", 32, 3)
    jakis_zwierz = Zwierze("Matka", 54, 50)
    Dumboo.przedstaw_sie()
    Simba.przedstaw_sie()
    Jago.przedstaw_sie()
    jakis_zwierz.przedstaw_sie()

    Dumboo.urodziny()
    Dumboo.przedstaw_sie()
if __name__ == "__main__":
    main()