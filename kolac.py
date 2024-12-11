class Kolac:
    def __init__(self, naziv):
        self.naziv = naziv
        self.kalorije = 200  # osnovne kalorije
        self.cena = 2.00     # osnovna cena

    def get_kalorije(self):
        return self.kalorije

    def get_cena(self):
        return self.cena

    def opis(self):
        return self.naziv
