from abc import ABC, abstractmethod
class Zwierze(ABC):
    def __init__(self, nazwa, wiek, waga):
        self.nazwa = nazwa
        self.wiek = wiek
        self.waga = waga

    @abstractmethod #tutaj wymuszamy implementację tej metody w klsach pochodnych
    def nazwa_gatunku(self):
        pass

    def przedstaw_sie(self):
        print(f"Jestem {self.nazwa_gatunku()}, mam na imię {self.nazwa} mam {self.wiek} lat oraz ważę {self.waga} kg.")

    def urodziny(self):
        self.wiek += 1

class Slon(Zwierze):
    def nazwa_gatunku(self):
        return "Słoń"

class Lew(Zwierze):
    def nazwa_gatunku(self):
        return "Lew"

class Papuga(Zwierze):
    def nazwa_gatunku(self):
        return  "Papuga"
    def __init__(self,nazwa, wiek, waga, kolor):
        super().__init__(nazwa,wiek,waga)
        self.kolor = kolor
    def przedstaw_sie(self):
        super().przedstaw_sie()
        print(f"Jako papuga mój kolor to {self.kolor}")
def nowy_rok(zoo):
    for zwierze in zoo:
        zwierze.urodziny()

def przedstaw_zwierzeta(zoo):
    for zwierze in zoo:
        zwierze.przedstaw_sie()

def main():
    Dumboo = Slon("Dumboo", 77, 600)
    Simba = Lew("Simba", 24, 100)
    Jago = Papuga("Jago", 32, 3, "czerwony")

    Dumboo.przedstaw_sie()
    Simba.przedstaw_sie()
    Jago.przedstaw_sie()


    Dumboo.urodziny()
    Dumboo.przedstaw_sie()
    zoo = [Dumboo, Simba, Jago]
    nowy_rok(zoo)
    przedstaw_zwierzeta(zoo)

if __name__ == "__main__":
    main()