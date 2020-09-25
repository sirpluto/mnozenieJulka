import json
import przyklad
import numpy


class Statisctic:

    errors_str = 'errors'
    total_str = 'total'
    json_extend_str = '.json'
    dim = 100

    matrix_errors = None

    matrix_total = None

    base_matrix = []

    def __init__(self, config, login, dzialanie):
        self. matrix_errors_name = "{}_{}_{}{}".format(self.errors_str, login, dzialanie, self.json_extend_str)
        self. matrix_total_name = "{}_{}_{}{}".format(self.total_str, login, dzialanie, self.json_extend_str)
        self.load_errors(config)
        self.load_total(config)

    def create_base_one_row(self):
        element = 0
        one_row = []
        while element <= self.dim:
            one_row.append(0)
            element += 1
        return one_row

    def create_base_matrix(self, config):
        raw = 0
        self.base_matrix = []
        one_row = self.create_base_one_row()
        while raw <= self.dim:
            self.base_matrix.append(one_row)
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
        if dzialanie.czy_mnozenie() or dzialanie.czy_dodawanie or dzialanie.czy_odejmowanie:
            index_a = dzialanie.a
            index_b = dzialanie.b
        elif dzialanie.czy_dzielenie:
            dzielna = int(max(dzialanie.a, dzialanie.b))
            dzielnik = int(min(dzialanie.a, dzialanie.b))
            iloraz = int(dzielna / dzielnik)
            index_a = dzielnik
            index_b = iloraz
        if not dzialanie.czy_odejmowanie:
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
