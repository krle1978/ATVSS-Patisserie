
from kolac import Kolac
from sastojci import TestoCokolada, PrelivJagoda
def prikazi_meni():
    print("1. Kreiraj novi kolač")
    print("2. Pretraga kolača")
    print("3. Dodaj kolač u porudžbinu")
    print("4. Izbriši kolač iz porudžbine")
    print("5. Ukupna cena porudžbine")
    print("6. Ukupna kalorijska vrednost porudžbine")
    print("7. Izlaz")

porudzbina = []

def kreiraj_kolac():
    naziv = input("Unesite naziv kolača: ")
    osnovni_kolac = Kolac(naziv)

    while True:
        print("Izaberite dodatke: 1. Čokoladno testo 2. Jagodni preliv 0. Kraj")
        izbor = input("Unesite izbor: ")
        if izbor == "1":
            osnovni_kolac = TestoCokolada(osnovni_kolac)
        elif izbor == "2":
            osnovni_kolac = PrelivJagoda(osnovni_kolac)
        elif izbor == "0":
            break

    print(osnovni_kolac.opis())
    print(f"Kalorije: {osnovni_kolac.get_kalorije()}")
    print(f"Cena: {osnovni_kolac.get_cena()} EUR")
    return osnovni_kolac

def pretraga_kolaca():
    naziv = input("Unesite naziv kolača za pretragu: ")
    for kolac in porudzbina:
        if naziv in kolac.opis():
            print(f"Pronađen kolač: {kolac.opis()}")
            return
    print("Kolač nije pronađen.")

def dodaj_kolac_u_porudzbinu(kolac):
    porudzbina.append(kolac)
    print(f"Kolač {kolac.opis()} je dodat u porudžbinu.")

def izbrisi_kolac_iz_porudzbine():
    naziv = input("Unesite naziv kolača za brisanje: ")
    for kolac in porudzbina:
        if naziv in kolac.opis():
            porudzbina.remove(kolac)
            print(f"Kolač {kolac.opis()} je izbrisan iz porudžbine.")
            return
    print("Kolač nije pronađen.")

def ukupna_cena_porudzbine():
    ukupno = sum(kolac.get_cena() for kolac in porudzbina)
    print(f"Ukupna cena porudžbine: {ukupno} EUR")

def ukupna_kalorijska_vrednost_porudzbine():
    ukupno = sum(kolac.get_kalorije() for kolac in porudzbina)
    print(f"Ukupna kalorijska vrednost porudžbine: {ukupno} kcal")

while True:
    prikazi_meni()
    izbor = input("Unesite izbor: ")

    if izbor == "1":
        kolac = kreiraj_kolac()
        dodaj_kolac_u_porudzbinu(kolac)
    elif izbor == "2":
        pretraga_kolaca()
    elif izbor == "3":
        kolac = kreiraj_kolac()
        dodaj_kolac_u_porudzbinu(kolac)
    elif izbor == "4":
        izbrisi_kolac_iz_porudzbine()
    elif izbor == "5":
        ukupna_cena_porudzbine()
    elif izbor == "6":
        ukupna_kalorijska_vrednost_porudzbine()
    elif izbor == "7":
        break
    else:
        print("Pogrešan unos. Pokušajte ponovo.")
