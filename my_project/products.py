class Produkt:
    def __init__(self, name, preis, verfuegbarkeit):
        # Hier müssen die privaten Instanzvariablen initialisiert werden
        self.name = name
        self.preis = preis
        self.verfuegbarkeit = verfuegbarkeit

    @property
    def preis(self):
        return self._preis

    @preis.setter
    def preis(self, preis):
        if not all([isinstance(preis, (float, int)), preis >= 0]):
            raise ValueError("Ungültiger Preis")
        self._preis = preis

    @property
    def verfuegbarkeit(self):
        return self._verfuegbarkeit

    @verfuegbarkeit.setter
    def verfuegbarkeit(self, verfuegbarkeit):
        if verfuegbarkeit not in ["in stock", "out of stock"]:
            raise ValueError("Ungültige verfuegbarkeit")
        self._verfuegbarkeit = verfuegbarkeit

    def __str__(self) -> str:
        return self.name


def test(products):
    for product in products:
        try:
            # p = Produkt(*product)
            name, preis, verfuegbarkeit = product
            p = Produkt(name, preis, verfuegbarkeit)
        except ValueError as e:
            print(e, product)
        else:
            print(f"{p} ist ein gültiges Produkt.")


if __name__ == "__main__":
    products = [
        ("Maggi", 23.2, "in stock"),
        ("Snickers", 4, "out of stock"),
        ("Petersilie", 1.9, "stock"),  # muss scheitern
        ("Gouda Käse", -12.50, "out of stock"),  # muss scheitern
        ("Za", 23.2, "inn stock"),  # muss scheitern.
    ]

    test(products)


### all-Funktion: wahr, wenn alle Elemente des Iterables truthy sind
### any-Funktion: wahr, wenn ein Elemeent des Iterables truthy ist
print(all([12, "test", {3, 4}, 32]))

x = 4
if all(
    [
        x > 3,
        x == 3,
        x < 34,
    ]
):
    print("alle Bedingngen sind wahr")


if any(
    [
        x > 3,
        x == 3,
        x < 34,
    ]
):
    print("eine Bedingngen sind wahr")
