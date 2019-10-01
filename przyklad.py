import random
import utils


class Przyklad():
    a = 0
    b = 0
    dzialanie = ''
    wynik = 0
    czas = 0

    def __init__(self, a, b, dzialanie):
        self.a = a
        self.b = b
        self.dzialanie = dzialanie
        self.oblicz_wynik()

    @staticmethod
    def mnozenie():
        return '*'

    @staticmethod
    def dzielenie():
        return '/'

    @staticmethod
    def mnozenie_string():
        return 'mnozenie'

    def dzielenie_string(self):
        return 'dzielenie'

    def czy_mnozenie(self):
        if self.dzialanie == self.mnozenie():
            return True
        else:
            return False

    def czy_dzielenie(self):
        if self.dzialanie == self.dzielenie():
            return True
        else:
            return False

    def oblicz_wynik(self):
        if self.czy_mnozenie():
            self.wynik = self.a * self.b
        elif self.czy_dzielenie():
            self.wynik = self.a / self.b
        else:
            print("Bledne dzialanie w oblicz_wynik()")

    def pytanie_wynik(self):
        if self.czy_mnozenie():
            pytanie = "Podaj wynik {} {}{}{}".format(self.mnozenie_string(), self.a, self.dzialanie, self.b)
        elif self.czy_dzielenie():
            pytanie = "Podaj wynik {} {}{}{}".format(self.dzielenie_string(), self.a, self.dzialanie, self.b)
        else:
            pytanie = "Nieprawidle dzialanie w pytanie_wynik()"
        return pytanie



class Losowy_przyklad(Przyklad):

    maxLiA =   0
    minLiA =   0
    maxLiB =   0
    minLiB =   0
    ilosc_zdobytych_pkt = 0

    def __init__(self, config, matrix_errors):
        self.losuj_dzialanie()
        self.ustaw_limity(config)
        self.losuj_liczby()
        self.oblicz_wynik()

    def ustaw_limity(self, config):
        if self.czy_mnozenie():
            self.maxLiA = config.get_max_mnozenie_li_a()
            self.minLiA = config.get_min_mnozenie_li_a()
            self.maxLiB = config.get_max_mnozenie_li_b()
            self.minLiB = config.get_min_mnozenie_li_b()
        elif self.czy_dzielenie():
            self.maxLiA = config.get_max_dzielenie_li_a()
            self.minLiA = config.get_min_dzielenie_li_a()
            self.maxLiB = config.get_max_dzielenie_li_b()
            self.minLiB = config.get_min_dzielenie_li_b()



    def losuj_dzialanie(self):
        tmp = random.randint(1, 100)
        if tmp%2 == 0:
            self.dzialanie = self.mnozenie()
        else:
            self.dzialanie = self.dzielenie()


    def losuj_liczby(self):
        if self.czy_mnozenie():
            self.a = random.randint(self.minLiA, self.maxLiA)
            self.b = random.randint(self.minLiB, self.maxLiB)
        else: #dzielenie
            self.a = 2
            self.b = 3
            while (self.a % self.b != 0) or (self.a / self.b > 10):
                self.a = random.randint(self.minLiA, self.maxLiA)
                self.b = random.randint(self.minLiB, self.maxLiB)
'''
    def nauka_mnozenia(self):
        czy_wynik_ok = False

        utils.wyswietl(self.builder, "Sprobujmy cos latwiejszego :)")
        for i in range(1, self.b+1):
            przyklad = Przyklad(self.builder, self.a, i, self.mnozenie())
            przyklad.pytanie_wynik()
            wynik = utils.wczytaj_wynik()
            if wynik == przyklad.wynik:
                utils.wyswietl(self.builder, "Brawo")
            else:
                utils.wyswietl(self.builder, ":(")
                utils.wyswietl(self.builder, "Prawidlowa odpowiedz to: {}".format(przyklad.wynik))
        utils.wyswietl(self.builder, "Teraz znasz juz odpowiedz na {}{}{}".format(self.a, self.dzialanie, self.b))
        wynik = utils.wczytaj_wynik()
        if wynik == self.wynik:
            utils.wyswietl(self.builder, "Brawo")
            czy_wynik_ok = True
        else:
            utils.wyswietl(self.builder, "Sprobjemy inne dzialanie")
        return czy_wynik_ok

    def nauka_dzielenia(self):
        czy_wynik_ok = False

        przyklad = Przyklad(self.builder, self.b, int(self.wynik), self.mnozenie())
        przyklad.pytanie_wynik()
        wynik = utils.wczytaj_wynik()
        if wynik == przyklad.wynik:
            utils.wyswietl(self.builder, "Brawo :)")
        else:
            utils.wyswietl(self.builder, ":(")
            utils.wyswietl(self.builder, "Prawidlowa odpowiedz to: []".format(przyklad.wynik))
        utils.wyswietl(self.builder, "Teraz znasz juz odpowiedz na {}{}{}".format(self.a, self.dzialanie, self.b))
        wynik = utils.wczytaj_wynik()
        if wynik == self.wynik:
            utils.wyswietl(self.builder, "Brawo")
            czy_wynik_ok = True
        else:
            utils.wyswietl(self.builder, "Sprobujemy inne dzialanie")

        return czy_wynik_ok

    def nauka(self):
        czy_wynik_ok = False

        if self.czy_mnozenie():
            czy_wynik_ok = self.nauka_mnozenia()
        elif self.czy_dzielenie():
            czy_wynik_ok = self.nauka_dzielenia()
        else:
            utils.wyswietl(self.builder, "Niezdefiniowane dzialanie w nauka()")
        return czy_wynik_ok
'''