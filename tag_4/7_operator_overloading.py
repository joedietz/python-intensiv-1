"""
Operatoren überladen

Klasse Produkt == (zwei Produkte sind gleich, wenn sie selben preis haben)

Dunder-Methode:
__gt__, __eq__, __add__
"""


class Product:
    def __init__(self, name: str, price: int) -> None:
        self.name = name
        self.price = price

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Product):
            return NotImplemented
        return self.price == other.price


p1 = Product("Milka", 200)
p2 = Product("Snickers", 200)
print(p1 == p2)

print(dir(p1))
