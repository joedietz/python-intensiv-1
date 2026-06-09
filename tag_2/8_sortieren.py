"""
Sortieren von Sequenzen:

list.sort() => Sortiert eine Liste inplace
sorted() => Sortiert eine Datenstruktur, Rückgabe ist eine Liste
"""

# Sortieren mit der .sort()-Methode
values = [3, 1, 9]
values.sort()
print(values)

# Sortieren mit sorted()
values = [3, 1, 9]
values = sorted(values)
print(values)

# Liste sortieren
chars = ["A", "a", "f", "b", "B", "A", "d", "e"]
chars = sorted(chars, key=lambda e: e.lower())
print(chars)

# Aufgabe
ids = ["id5", "idx1", "id2", "idy5", "id4", "id3"]
ids_sorted = sorted(ids, key=lambda e: int(e[-1]))  # [5, 1, 2, 5, 4, 3]
print(ids_sorted)

# Sortiere nach Preis
snacks = {"Milka": 3.30, "Kekse": 5.20, "Snickers": 1.50}
result = sorted(snacks.items(), key=lambda e: e[1])
print(result)

# Nach Preis sortieren
snacks = {
    1: {"name": "Erdnüsse", "price": 200, "amount": 50, "pos": {"x": 10}},
    2: {"name": "Milka", "price": 400, "amount": 20, "pos": {"x": 30}},
    3: {"name": "Snickers", "price": 100, "amount": 10, "pos": {"x": 50}},
}

snacks_preis = sorted(snacks.items(), key=lambda e: e[1]["price"])
