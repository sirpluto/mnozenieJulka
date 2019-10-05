import random
import os


class Emoticon:

    def __init__(self, czy_wynik_ok):
        self.curdir = os.path.dirname(__file__)
        self.happy = "happy"
        self.sad = "sad"
        self.happy_folder = "images/" + self.happy + "/"
        self.sad_folder = "images/" + self.sad + "/"
        self.min_number = 1
        self.max_number = 5
        self.czy_wynik_ok = czy_wynik_ok

    def file_name(self):

        if self.czy_wynik_ok:
            file = self.happy_folder + self.gen_random_name()
        else:
            file = self.sad_folder + self.gen_random_name()
        return os.path.join(self.curdir, file)

    def gen_random_name(self):
        if self.czy_wynik_ok:
            first_part = self.happy + "_"
        else:
            first_part = self.sad + "_"

        file_number = random.randint(self.min_number, self.max_number)
        return '{}{}.gif'.format(first_part, file_number)