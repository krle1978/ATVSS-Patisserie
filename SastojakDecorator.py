
from kolac import Kolac
class SastojakDecorator(Kolac):
    def __init__(self, kolac):
        self.kolac = kolac

    def get_kalorije(self):
        return self.kolac.get_kalorije()

    def get_cena(self):
        return self.kolac.get_cena()

    def opis(self):
        return self.kolac.opis()
