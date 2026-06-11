"""
Funktionalitäten aus Klassen via (Mehrfach-)Vererbung nutzen (Mixin)
"""


class JsonExporter:
    def to_json(self):
        print("Exportiere nach Json:", self.data)


class CsvExporter:
    def to_csv(self):
        print("Exportiere nach Json:", self.data)


class DataManager(JsonExporter, CsvExporter):
    def __init__(self, data: list):
        self.data = data


d = DataManager(data=[1, 2])
d.to_json()

# Method Resolution Order
print(DataManager.mro())
