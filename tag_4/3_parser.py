""" """


class Parser:
    def __init__(self, filename: str):
        self.filename = filename


class JsonParser(Parser):
    def parse(self):
        print("Parse json")


class CvsParser(Parser):
    def parse(self):
        print("Parse CSV")


json_parser = JsonParser(filename="xzy.json")
json_parser.parse()


def daten_verarbeiten(parser: Parser):
    parser.parse()


daten_verarbeiten(json_parser)
