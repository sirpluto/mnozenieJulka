try:
    import tkinter as tk
    from tkinter import messagebox
except:
    import Tkinter as tk
    import tkMessageBox as messagebox

import pygubu
import logic
import przyklad
import steam_cli


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

        self.canvas = self.builder.get_object('canvas_image')
        self.wyswietl_liste_nagrod()

        # Configure callbacks
        builder.connect_callbacks(self)

        self.logic = None

        self.login = None

    def on_entry_wynik_keypress_enter(self, event=None):
        self.click_on_sprawdz()

    def click_on_wyjdz(self, itemid):
        if itemid == 'mopt_wyjdz':
            messagebox.showinfo('Wyjdz', 'Do zobaczenia.')
            if self.logic:
                self.logic.wyjdz()
            self.quit()

    def nowa_runda(self, lista_dzialan):
        if self.login == None:
            messagebox.showinfo('Brak użytkownika', 'Zaloguj sie. Plik->Login')
        else:
            self.logic = logic.Logic(self.login)
            self.on_liste_nagrod_select(None)
            self.logic.nowa_runda(lista_dzialan, self.login)
            messagebox.showinfo('Nowa runda', 'Czas rozpoczac nowa runde')
            self.logic.dodaj_przyklady_do_listy()
            self.logic.wczytaj_przyklad_z_listy()
            self.wyczysc_wynik()
            self.wyswietl_label_top(self.logic.komunikat())
            self.wyswietl_label_l(self.logic.pytanie_dzialanie())
            self.logic.set_start_time()

    def click_on_login_julka(self, itemid):
        if itemid == 'mopt_login_julka':
            self.wyswietl_canvas_image('images/login/girl_math.gif')
            self.login = 'julka'

    def click_on_login_jas(self, itemid):
        if itemid == 'mopt_login_jas':
            self.wyswietl_canvas_image('images/login/boy_math.gif')
            self.login = 'jas'


    def click_on_runda_mix(self, itemid):
        if itemid == 'mopt_runda_mix':
            lista_dzialan = [przyklad.Przyklad.mnozenie(), przyklad.Przyklad.dzielenie(),
                             przyklad.Przyklad.dodawanie(), przyklad.Przyklad.odejmowanie()]
            self.nowa_runda(lista_dzialan)

    def click_on_runda_mnozenie(self, itemid):
        if itemid == 'mopt_runda_mnozenie':
            lista_dzialan = [przyklad.Przyklad.mnozenie()]
            self.nowa_runda(lista_dzialan)

    def click_on_runda_dzielenie(self, itemid):
        if itemid == 'mopt_runda_dzielenie':
            lista_dzialan = [przyklad.Przyklad.dzielenie()]
            self.nowa_runda(lista_dzialan)

    def click_on_runda_dodawanie(self, itemid):
        if itemid == 'mopt_runda_dodawanie':
            lista_dzialan = [przyklad.Przyklad.dodawanie()]
            self.nowa_runda(lista_dzialan)

    def click_on_runda_odejmowanie(self, itemid):
        if itemid == 'mopt_runda_odejmowanie':
            lista_dzialan = [przyklad.Przyklad.odejmowanie()]
            self.nowa_runda(lista_dzialan)

    def click_on_o_programie(self):
        messagebox.showinfo('O programie', 'To jest prgram dla Julki')

    def click_on_nagroda(self):
        if not self.logic == None:
            self.logic.nagroda(self.login)

    def click_on_sprawdz(self):

        if not self.wczytaj_wynik() == None:
            self.logic.set_stop_time()
            self.wyswietl_canvas_image(self.logic.emoticon_file())
            self.logic.play_sound()
            self.logic.aktualizuj()
            self.logic.dodaj_przyklady_do_listy()
            self.logic.wczytaj_przyklad_z_listy()
            self.wyczysc_wynik()
            self.wyswietl_label_top(self.logic.komunikat())
            self.wyswietl_label_l(self.logic.pytanie_dzialanie())
            self.logic.set_start_time()

    def wczytaj_wynik(self):
        wynik_var = self.builder.get_variable('entry_wynik_var')
        try:
            wynik_uzytkownika = wynik_var.get()
        except:
            wynik_uzytkownika = None
        self.logic.set_wynik_uzytownika(wynik_uzytkownika)
        return wynik_uzytkownika

    def wyczysc_wynik(self):
        self.builder.tkvariables['entry_wynik_var'].set('')

    def wyswietl_label_l(self, txt):
        self.builder.tkvariables['label_l_var'].set(txt)

    def wyswietl_label_top(self, txt):
        self.builder.tkvariables['label_top_var'].set(txt)

    def wyswietl_canvas_image(self, file_name):
        self._image = img = tk.PhotoImage(file=file_name)
        # draw in canvas
        c = self.canvas
        c.create_image(15, 15, anchor='nw', image=img)

    def wyswietl_liste_nagrod(self):
        lista_nagrod = self.builder.get_object('combobox_lista_nagrod')
        lista_nagrod.config(values=steam_cli.SteamCli.get_installed_games())
        lista_nagrod.bind('<<ComboboxSelected>>', self.on_liste_nagrod_select)

    def on_liste_nagrod_select(self, event):
        if self.logic:
            self.logic.selected_game = self.builder.get_object('combobox_lista_nagrod').get()


if __name__ == '__main__':
    root = tk.Tk()
    app = MyApplication(root)
    app.run()
