try:
    import tkinter as tk
    from tkinter import messagebox
except:
    import Tkinter as tk
    import tkMessageBox as messagebox

import pygubu
import runda
import przyklad
import time
import play_sound
import utils
import config

class MyApplication(pygubu.TkApplication):

    def _create_ui(self):
        #1: Create a builder
        self.builder = builder = pygubu.Builder()

        #2: Load an ui file
        builder.add_from_file('menu.ui')

        #3: Create the widget using self.master as parent
        self.mainwindow = builder.get_object('mainwindow', self.master)

        # Set main menu
        self.mainmenu = menu = builder.get_object('mainmenu', self.master)
        self.set_menu(menu)

        # Configure callbacks
        builder.connect_callbacks(self)

        # Set runda
        self.runda = None

        self.lista_a = []
        self.lista_b = []
        self.lissta_oper = []

        self.config = config.Config()

    def on_entry_wynik_keypress_enter(self, event=None):
        self.click_on_sprawdz()

    def click_on_wyjdz(self, itemid):
        if itemid == 'mopt_wyjdz':
            messagebox.showinfo('Wyjdz', 'Do zobaczenia.')
            self.quit()

    def click_on_nowa_runda(self, itemid):
        if itemid == 'mopt_nowa_runda':
            messagebox.showinfo('Nowa runda', 'Czas rozpoczac nowa runde')

            self.lista_a = []
            self.lista_b = []
            self.lista_oper = []

            self.runda = runda.Runda(self.config.get_ile_pkt_nagroda(),
                                     self.config.get_ile_pkt_szybka_odpowiedz(),
                                     self.config.get_czas_szybka_odpowiedz(),
                                     self.config.get_roznica_duzy_blad(),
                                     self.config.get_ile_pkt_duzy_blad())
            self.wyswietl_label_top(self.runda.komunikat())
            self.generuj_przyklad()

    def click_on_o_programie(self):
        messagebox.showinfo('O programie', 'To jest prgram dla Julki')

    def click_on_nagroda(self):
        if not self.runda.czy_nagroda():
            return
        czasNagrody = 9;
        p = utils.run_game()
        time.sleep(czasNagrody)
        utils.stop_game(p)
        self.runda.set_normal()

    def click_on_sprawdz(self):
        timeStop = time.perf_counter()
        wynik_uzytkownika = self.wczytaj_wynik()
        self.wyczysc_wynik()
        self.runda.aktualizuj(wynik_uzytkownika, self.dzialanie.wynik, timeStop - self.timeStart)
        self.wyswietl_label_top(self.runda.komunikat())

        if not self.lista_a:
            self.runda.set_normal()

        if wynik_uzytkownika == self.dzialanie.wynik:
            play_sound.play_random_happy()
            self.generuj_przyklad()
        else:
            play_sound.play_random_sad()
            self.generuj_nauke()
            self.generuj_przyklad()

    def generuj_przyklad(self):
        if self.runda.czy_nauka():
            self.dzialanie = przyklad.Przyklad(self.lista_a.pop(), self.lista_b.pop(), self.lista_oper.pop())
        elif self.runda.czy_normal():
            self.dzialanie = przyklad.Losowy_przyklad(self.config)

        komunikat = self.dzialanie.pytanie_wynik()
        self.wyswietl_label_l(komunikat)
        self.timeStart = time.perf_counter()

    def wczytaj_wynik(self):
        wynik_var = self.builder.get_variable('entry_wynik_var')
        wynik_uzytkownika = wynik_var.get()
        return wynik_uzytkownika

    def wyczysc_wynik(self):
        self.builder.tkvariables['entry_wynik_var'].set('')

    def wyswietl_label_l(self, txt):
        self.builder.tkvariables['label_l_var'].set(txt)

    def wyswietl_label_top(self, txt):
        self.builder.tkvariables['label_top_var'].set(txt)

    def generuj_nauke(self):
        if self.runda.czy_nauka():
            return

        self.runda.set_nauka()

        if self.dzialanie.czy_mnozenie():
            self.generuj_nauke_mnozenia()
        elif self.dzialanie.czy_dzielenie():
            self.generuj_nauke_dzielenia()
        else:
            print('Nieprawidlowo zdefiniowane dzialanie w generuj_nauke()')

    def generuj_nauke_mnozenia(self):
        for i in range(self.dzialanie.b, 0,  -1):
            self.lista_a.append(self.dzialanie.a)
            self.lista_b.append(i)
            self.lista_oper.append(self.dzialanie.dzialanie)

    def generuj_nauke_dzielenia(self):
        self.lista_a.append(self.dzialanie.a)
        self.lista_b.append(self.dzialanie.b)
        self.lista_oper.append(self.dzialanie.dzielenie())

        self.lista_a.append(self.dzialanie.b)
        self.lista_b.append(int(self.dzialanie.wynik))
        self.lista_oper.append(self.dzialanie.mnozenie())


if __name__ == '__main__':
    root = tk.Tk()
    app = MyApplication(root)
    app.run()