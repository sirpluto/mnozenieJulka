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
    def dodawanie():
        return '+'

    @staticmethod
    def odejmowanie():
        return '-'

    @staticmethod
    def mnozenie_string():
        return 'mnozenie'

    @staticmethod
    def dzielenie_string():
        return 'dzielenie'

    @staticmethod
    def dodawanie_string():
        return 'dodawanie'

    @staticmethod
    def odejmowanie_string():
        return 'odejmowanie'

    @staticmethod
    def dzialanie_string(dzialanie):
        str = None
        if dzialanie == Przyklad.mnozenie():
            str = Przyklad.mnozenie_string()
        elif dzialanie == Przyklad.dzielenie():
            str = Przyklad.dzielenie_string()
        elif dzialanie == Przyklad.dodawanie():
            str = Przyklad.dodawanie_string()
        elif dzialanie == Przyklad.odejmowanie():
            str = Przyklad.odejmowanie_string()
        else:
            print("Bledne dzialanie w dzialanie_string()")
        return str

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

    def czy_dodawanie(self):
        if self.dzialanie == self.dodawanie():
            return True
        else:
            return False

    def czy_odejmowanie(self):
        if self.dzialanie == self.odejmowanie():
            return True
        else:
            return False

    def oblicz_wynik(self):
        if self.czy_mnozenie():
            self.wynik = self.a * self.b
        elif self.czy_dzielenie():
            self.wynik = self.a / self.b
        elif self.czy_dodawanie():
            self.wynik = self.a + self.b
        elif self.czy_odejmowanie():
            self.wynik = self.a - self.b
        else:
            print("Bledne dzialanie w oblicz_wynik()")

    def pytanie_wynik(self):
        if self.czy_mnozenie():
            pytanie = "Podaj wynik {} {}{}{}".format(self.mnozenie_string(), self.a, self.dzialanie, self.b)
        elif self.czy_dzielenie():
            pytanie = "Podaj wynik {} {}{}{}".format(self.dzielenie_string(), self.a, self.dzialanie, self.b)
        elif self.czy_dodawanie():
            pytanie = "Podaj wynik {} {}{}{}".format(self.dodawanie_string(), self.a, self.dzialanie, self.b)
        elif self.czy_odejmowanie():
            pytanie = "Podaj wynik {} {}{}{}".format(self.odejmowanie_string(), self.a, self.dzialanie, self.b)
        else:
            pytanie = "Nieprawidle dzialanie w pytanie_wynik()"
        return pytanie


class Losowy_przyklad(Przyklad):

    maxLiA =   0
    minLiA =   0
    maxLiB =   0
    minLiB =   0
    ilosc_zdobytych_pkt = 0

    def __init__(self, config, lista_dzialan):
        self.losuj_dzialanie(lista_dzialan)
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
        elif self.czy_dodawanie():
            self.maxLiA = config.get_max_dodawanie_li_a()
            self.minLiA = config.get_min_dodawanie_li_a()
            self.maxLiB = config.get_max_dodawanie_li_b()
            self.minLiB = config.get_min_dodawanie_li_b()
        elif self.czy_odejmowanie():
            self.maxLiA = config.get_max_dodawanie_li_a()
            self.minLiA = config.get_min_dodawanie_li_a()
            self.maxLiB = config.get_max_dodawanie_li_b()
            self.minLiB = config.get_min_dodawanie_li_b()

    def losuj_dzialanie(self, lista_dzialan):
        tmp = random.randint(1, 100)
        nr_dzialanie = tmp % len(lista_dzialan)
        self.dzialanie = lista_dzialan[nr_dzialanie]



    def losuj_liczby(self):
        if self.czy_mnozenie() or self.czy_dodawanie():
            self.a = random.randint(self.minLiA, self.maxLiA)
            self.b = random.randint(self.minLiB, self.maxLiB)
        elif self.czy_odejmowanie():
            self.a = random.randint(self.minLiA, self.maxLiA)
            self.b = random.randint(self.minLiB, self.maxLiB)
            if self.a < self.b:
                pom = self.a
                self.a = self.b
                self.b = pom
        else: #dzielenie
            self.a = 2
            self.b = 3
            while (self.a % self.b != 0) or (self.a / self.b > 10):
                self.a = random.randint(self.minLiA, self.maxLiA)
                self.b = random.randint(self.minLiB, self.maxLiB)
