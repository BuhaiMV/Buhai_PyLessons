import csv


class CsvManager:
    def __init__(self):
        self.__lines = []
        self.filename = 'example.csv'

    def __read_file(self):
        with open(self.filename, 'r') as csv_file:
            lines = csv.DictReader(csv_file)
            for line in lines:
                self.__lines.append((line))

    def count_lines(self):
        with open(self.filename, 'r') as csv_file:
            lines = csv.DictReader(csv_file)
            __lines = []
            for line in lines:
                __lines.append((line))
            return len(__lines)

    def __write_to_file(self):
        with open(self.filename, 'w') as writer:
            file_fieldnames = list(self.__lines[0].keys())
            file_writer = csv.DictWriter(writer, fieldnames=file_fieldnames)
            file_writer.writeheader()
            file_writer.writerows(self.__lines)
        self.cleanup()

    def add_line(self, line):
        self.__read_file()
        self.__lines.append(line)
        self.__write_to_file()

    def delete_line(self):
        self.__read_file()
        self.__lines.pop()
        self.__write_to_file()

    def cleanup(self):
        self.__lines = []
