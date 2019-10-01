import json
import przyklad
import numpy


class Statisctic():

    matrix_errors_name = 'errors.json'

    matrix_errors = None

    matrix_total_name = 'total.json'

    matrix_total = None

    base_matrix = []

    matrix_one_row = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    def __init__(self, config):
        self.load_errors(config)
        self.load_total(config)

    def create_base_matrix(self, config):
        raw = 0
        while raw <= config.get_max_mnozenie_li_b():
            self.base_matrix.append(self.matrix_one_row)
            raw += 1

    def load(self, config, file_name):
        matrix_data = None
        try:
            with open(file_name) as json_file:
                matrix_data = json.load(json_file)
        except (ValueError, FileNotFoundError):
            self.save_default(config, file_name)
            matrix_data = self.load(config, file_name)
        return matrix_data

    def load_errors(self, config):
        self.matrix_errors = self.load(config, self.matrix_errors_name)

    def load_total(self, config):
        self.matrix_total = self.load(config, self.matrix_total_name)

    def save_default(self, config, file_name):
        self.create_base_matrix(config)
        with open(file_name, 'w') as json_file:
            json.dump(self.base_matrix, json_file)

    def save_default_errors(self, config):
        self.save_default(config, self.matrix_errors_name)

    def save_default_total(self, config):
        self.save_default(config, self.matrix_total_name)

    def save(self):
        with open(self.matrix_total_name, 'w') as json_file:
            json.dump(self.matrix_total, json_file)
        with open(self.matrix_errors_name, 'w') as json_file:
            json.dump(self.matrix_errors, json_file)

    def update_matrix_data(self, matrix_data, dzialanie):
        if dzialanie.czy_mnozenie():
            index_a = dzialanie.a
            index_b = dzialanie.b
        elif dzialanie.czy_dzielenie:
            dzielna = int(max(dzialanie.a, dzialanie.b))
            dzielnik = int(min(dzialanie.a, dzialanie.b))
            iloraz = int(dzielna / dzielnik)
            index_a = dzielnik
            index_b = iloraz
        self.correct_data_integrity(index_a, index_b)
        matrix_data[index_a][index_b] += 1
        matrix_data[index_b][index_a] += 1


    def correct_data_integrity(self, index_a, index_b):
        if self.matrix_errors[index_a][index_b] != self.matrix_errors[index_b][index_a]:
            max_value = max(self.matrix_errors[index_a][index_b], self.matrix_errors[index_b][index_a])
            self.matrix_errors[index_a][index_b] = max_value
            self.matrix_errors[index_b][index_a] = max_value


    def update_all_matrix(self, dzialanie, czy_wynik_ok):
        self.update_matrix_data(self.matrix_total, dzialanie)
        if not czy_wynik_ok:
            self.update_matrix_data(self.matrix_errors, dzialanie)

    def generuj_skladniki_dzialania(self, config):
        max_value, index_a, index_b = max((x, i, j)
                                        for i, row in enumerate(self.matrix_errors)
                                        for j, x in enumerate(row))

        self.correct_data_integrity(index_a, index_b)
        if max_value > config.get_ilosc_bledow_przyklad():
            self.matrix_errors[index_a][index_b] -= 1
            self.matrix_errors[index_b][index_a] -= 1
            return index_a, index_b
        else:
            return -1, -1











