
class Runda():

    ile_pkt_nagroda = 0
    ile_pkt_szybka_odpowiedz = 0
    czas_szybka_odpowiedz = 0
    roznica_duzy_blad = 0
    ile_pkt_duzy_blad = 0
    akt_pkt = 0
    stan = ''

    def __init__(self, ile_pkt_nagroda, ile_pkt_szybka_odpowiedz, czas_szybka_odpowiedz, roznica_duzy_blad, ile_pkt_duzy_blad):
        self.ile_pkt_nagroda = ile_pkt_nagroda
        self.ile_pkt_szybka_odpowiedz = ile_pkt_szybka_odpowiedz
        self.czas_szybka_odpowiedz = czas_szybka_odpowiedz
        self.roznica_duzy_blad = roznica_duzy_blad
        self.ile_pkt_duzy_blad = ile_pkt_duzy_blad
        self.stan = 'normal'

    def aktualizuj_punkty(self, wynik_uzytkownika, wynik, czas):
        czy_duzy_blad = abs(wynik_uzytkownika - wynik) > self.roznica_duzy_blad
        czy_szybka_odpowiedz = czas < self.czas_szybka_odpowiedz
        czy_wynik_ok = 0 == wynik - wynik_uzytkownika

        if not czy_wynik_ok:
            if czy_duzy_blad:
                self.akt_pkt -= self.ile_pkt_duzy_blad
            else:
                self.akt_pkt -= 1
        else:
            if czy_szybka_odpowiedz:
                self.akt_pkt += self.ile_pkt_szybka_odpowiedz
            else:
                self.akt_pkt += 1

    def aktualizuj(self, wynik_uzytkownika, wynik, ilosc_przykladow, czas):
        czy_wynik_ok = 0 == wynik - wynik_uzytkownika

        if self.stan != 'nauka':
            self.aktualizuj_punkty(wynik_uzytkownika, wynik, czas)

        if ilosc_przykladow > 0:
            return

        if czy_wynik_ok:
            self.stan = 'normal'
        else:
            self.stan = 'nauka'

        if self.akt_pkt > self.ile_pkt_nagroda:
            self.set_nagroda()

    def komunikat(self):
        return 'Do nagrody pozostalo: {} z {}'.format(self.ile_pkt_nagroda - self.akt_pkt, self.ile_pkt_nagroda)

    def czy_normal(self):
        return self.stan == 'normal'

    def czy_nagroda(self):
        return self.stan == 'nagroda'

    def czy_nauka(self):
        return self.stan == 'nauka'

    def set_normal(self):
        self.stan = 'normal'

    def set_nauka(self):
        self.stan = 'nauka'

    def set_nagroda(self):
        self.stan = 'nagroda'







