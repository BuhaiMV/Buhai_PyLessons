# 1
import csv
import json


class JsonConvertor:
    def __init__(self):
        self.__lines = []

    def read_file(self, filename: str):
        with open(filename, 'r') as json_file:
            lines = json.load(json_file)
            for line in lines:
                self.__lines.append((line))

    def write_to_file(self, filename: str):
        with open(filename, 'w') as writer:
            file_fieldnames = list(self.__lines[0].keys())
            file_writer = csv.DictWriter(writer, fieldnames=file_fieldnames)
            file_writer.writeheader()
            file_writer.writerows(self.__lines)
        self.cleanup()

    def cleanup(self):
        self.__lines = []


convertor = JsonConvertor()
convertor.read_file('example.json')
convertor.write_to_file('example.csv')
