from .reader import Reader


class CsvReader(Reader):
    def __init__(self, filename: str):
        self.filename = filename

    def read(self):
        with open(self.filename, 'r') as csv_file:
            text = csv_file.read()
        return text
