import json


class Config():

    config_data = None

    default_config = {
        'max_mnozenie_li_a': 14,
        'min_mnozenie_li_a': 2,
        'max_mnozenie_li_b': 14,
        'min_mnozenie_li_b': 2,

        'max_dzielenie_li_a': 100,
        'min_dzielenie_li_a': 2,
        'max_dzielenie_li_b': 9,
        'min_dzielenie_li_b': 2,

        'ile_pkt_nagroda': 200,
        'ile_pkt_szybka_odpowiedz': 5,
        'czas_szybka_odpowiedz': 10,
        'roznica_duzy_blad': 3,
        'ile_pkt_duzy_blad': 4
    }

    def __init__(self):
        self.load()

    def load(self):
        try:
            with open('config.json') as json_file:
                self.config_data = json.load(json_file)
        except (ValueError, FileNotFoundError):
            self.save_default()
            self.load()

    def save_default(self):
        with open('config.json', 'w') as json_file:
            json.dump(self.default_config, json_file)

    def save(self):
        with open('config.json', 'w') as json_file:
            json.dump(self.config_data, json_file)

    def add_default_element(self, element, value):
        self.config_data.append({element: value})

    def get_element(self, element):
        value = self.config_data[element]
        if not value:
            value = self.default_config[element]
            self.add_default_element(element, value)
        return value

    def get_ile_pkt_nagroda(self):
        return self.get_element('ile_pkt_nagroda')

    def get_ile_pkt_szybka_odpowiedz(self):
        return self.get_element('ile_pkt_szybka_odpowiedz')

    def get_czas_szybka_odpowiedz(self):
        return self.get_element('czas_szybka_odpowiedz')

    def get_roznica_duzy_blad(self):
        return self.get_element('roznica_duzy_blad')

    def get_ile_pkt_duzy_blad(self):
        return self.get_element('ile_pkt_duzy_blad')

    def get_max_mnozenie_li_a(self):
        return self.get_element('max_mnozenie_li_a')

    def get_min_mnozenie_li_a(self):
        return self.get_element('min_mnozenie_li_a')

    def get_max_mnozenie_li_b(self):
        return self.get_element('max_mnozenie_li_b')

    def get_min_mnozenie_li_b(self):
        return self.get_element('min_mnozenie_li_b')

    def get_max_dzielenie_li_a(self):
        return self.get_element('max_dzielenie_li_a')

    def get_min_dzielenie_li_a(self):
        return self.get_element('min_dzielenie_li_a')

    def get_max_dzielenie_li_b(self):
        return self.get_element('max_dzielenie_li_b')

    def get_min_dzielenie_li_b(self):
        return self.get_element('min_dzielenie_li_b')


