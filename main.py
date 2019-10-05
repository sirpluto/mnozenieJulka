try:
    import tkinter as tk
    from tkinter import messagebox
except:
    import Tkinter as tk
    import tkMessageBox as messagebox

import pygubu
import logic


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

        # Configure callbacks
        builder.connect_callbacks(self)

        self.logic = logic.Logic()


    def on_entry_wynik_keypress_enter(self, event=None):
        self.click_on_sprawdz()

    def click_on_wyjdz(self, itemid):
        if itemid == 'mopt_wyjdz':
            messagebox.showinfo('Wyjdz', 'Do zobaczenia.')
            self.logic.wyjdz()
            self.quit()

    def click_on_nowa_runda(self, itemid):
        if itemid == 'mopt_nowa_runda':
            self.logic.nowa_runda()
            messagebox.showinfo('Nowa runda', 'Czas rozpoczac nowa runde')
            self.logic.dodaj_przyklady_do_listy()
            self.logic.wczytaj_przyklad_z_listy()
            self.wyczysc_wynik()
            self.wyswietl_label_top(self.logic.komunikat())
            self.wyswietl_label_l(self.logic.pytanie_dzialanie())
            self.logic.set_start_time()

    def click_on_o_programie(self):
        messagebox.showinfo('O programie', 'To jest prgram dla Julki')

    def click_on_nagroda(self):
        self.logic.nagroda()

    def click_on_sprawdz(self):
        self.logic.set_stop_time()
        self.wczytaj_wynik()
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
        wynik_uzytkownika = wynik_var.get()
        self.logic.set_wynik_uzytownika(wynik_uzytkownika)

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

if __name__ == '__main__':
    root = tk.Tk()
    app = MyApplication(root)
    app.run()