import json


class JSONDataHandler:
    def __init__(self, filename='hotels.json'):
        self.filename = filename

    def load_data(self):
        with open(self.filename, 'r', encoding='UTF-8') as file:
            return json.load(file)

    def save_data(self, data):
        with open(self.filename, 'w', encoding='UTF-8') as file:
            json.dump(data, file, indent=4)
