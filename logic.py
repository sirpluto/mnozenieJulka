import matrix
import config
import runda
import przyklad
import time
import play_sound
import utils
import emoticon


class Logic:

    def __init__(self):
        self.config = config.Config()

        self.lista_przykladow = []

        self.akt_dzialanie = None
        self.wynik_uzytkownika = None

        self.runda = None

        self.statistic = matrix.Statisctic(self.config)

    @staticmethod
    def generuj_nauke_mnozenia(a, b):
        lista_przykladow = []

        for i in range(b, 0,  -1):
            lista_przykladow.append(przyklad.Przyklad(a, i, przyklad.Przyklad.mnozenie()))

        return lista_przykladow

    @staticmethod
    def generuj_nauke_dzielenia(a, b, wynik):
        lista_przykladow = []

        lista_przykladow.append(przyklad.Przyklad(a, b, przyklad.Przyklad.dzielenie()))
        lista_przykladow.append(przyklad.Przyklad(b, wynik, przyklad.Przyklad.mnozenie()))

        return lista_przykladow

    @staticmethod
    def generuj_nauke(dzialanie):
        lista_przykladow = []

        if dzialanie.czy_mnozenie():
            lista_przykladow = Logic.generuj_nauke_mnozenia(dzialanie.a, dzialanie.b)
        elif dzialanie.czy_dzielenie():
            lista_przykladow = Logic.generuj_nauke_dzielenia(dzialanie.a, dzialanie.b, dzialanie.wynik)
        else:
            print('Nieprawidlowo zdefiniowane dzialanie w generuj_nauke()')

        return lista_przykladow

    def generuj_przyklad(self):
        lista = []

        a, b = self.statistic.generuj_skladniki_dzialania(self.config)
        if a == -1:
            lista.append(przyklad.Losowy_przyklad(self.config, self.statistic))
        else:
            lista.append(przyklad.Przyklad(a, b, przyklad.Przyklad.mnozenie()))
        return lista

    def dodaj_przyklady_do_listy(self):
        if len(self.lista_przykladow) > 0:
            return

        if self.czy_wynik_ok():
            lista = self.generuj_przyklad()
        else:
            lista = self.generuj_nauke(self.akt_dzialanie)

        for element in lista:
            self.lista_przykladow.append(element)

    def wczytaj_przyklad_z_listy(self):
        self.akt_dzialanie = self.lista_przykladow.pop()

    def czy_wynik_ok(self):
        if not self.akt_dzialanie and not self.wynik_uzytkownika:
            return True
        return self.akt_dzialanie.wynik == self.wynik_uzytkownika

    def set_wynik_uzytownika(self, wynik):
        self.wynik_uzytkownika = wynik;

    def pytanie_dzialanie(self):
        return self.akt_dzialanie.pytanie_wynik()

    def komunikat(self):
        return self.runda.komunikat()

    def nowa_runda(self):
        self.statistic.save()

        self.lista_przykladow = []
        self.akt_dzialanie = None
        self.wynik_uzytkownika = None

        self.runda = runda.Runda(self.config.get_ile_pkt_nagroda(),
                                 self.config.get_ile_pkt_szybka_odpowiedz(),
                                 self.config.get_czas_szybka_odpowiedz(),
                                 self.config.get_roznica_duzy_blad(),
                                 self.config.get_ile_pkt_duzy_blad())

    def wyjdz(self):
        self.statistic.save()

    def set_start_time(self):
        self.time_start = time.perf_counter()

    def set_stop_time(self):
        self.time_stop = time.perf_counter()

    def play_sound(self):
        if self.czy_wynik_ok():
            if self.runda.czy_normal():
                play_sound.play_random_happy()
        else:
            play_sound.play_random_sad()

    def emoticon_file(self):
        emot = emoticon.Emoticon(self.czy_wynik_ok())
        return emot.file_name()


    def aktulizuj_runde(self):
        self.runda.aktualizuj(self.wynik_uzytkownika, self.akt_dzialanie.wynik, len(self.lista_przykladow), self.time_stop - self.time_start)

    def aktualizuj_matryce_bledow(self):
        if self.runda.czy_normal():
            self.statistic.update_all_matrix(self.akt_dzialanie, self.czy_wynik_ok())

    def aktualizuj(self):
        self.aktualizuj_matryce_bledow()
        self.aktulizuj_runde()

    def nagroda(self):
        if not self.runda.czy_nagroda():
            return
        czasNagrody = self.config.get_czas_nagrody();
        p = utils.run_game()
        time.sleep(czasNagrody)
        utils.stop_game(p)
        self.runda.set_normal()

