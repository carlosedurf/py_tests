import requests


class Peaple:
    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name
        self.data_obtained = False

    def get_all_data(self):
        response = requests.get('')

        if response.ok:
            self.data_obtained = True
            return 'CONECTADO'
        else:
            self.data_obtained = False
            return 'ERROR 404'
