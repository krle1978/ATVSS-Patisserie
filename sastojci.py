from SastojakDecorator import SastojakDecorator
class TestoCokolada(SastojakDecorator):
    def __init__(self, kolac):
        super().__init__(kolac)

    def get_kalorije(self):
        return self.kolac.get_kalorije() + 50

    def get_cena(self):
        return self.kolac.get_cena() + 0.5

    def opis(self):
        return self.kolac.opis() + ', sa čokoladnim testom'

class PrelivJagoda(SastojakDecorator):
    def __init__(self, kolac):
        super().__init__(kolac)

    def get_kalorije(self):
        return self.kolac.get_kalorije() + 30

    def get_cena(self):
        return self.kolac.get_cena() + 0.3

    def opis(self):
        return self.kolac.opis() + ', sa jagodnim prelivom'
