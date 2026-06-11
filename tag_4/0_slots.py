"""
__slots__ ist ein Python-Mechanismus, der verhindert, dass jede
Instanz automatisch ein eigenes Attribut-Wörterbuch (__dict__) bekommt.
"""


class Robot:
    number = 0
    __slots__ = ("name", "power")

    def __init__(self, name: str, power: int) -> None:
        self.name = name
        self.power = power
        # self.age = 1  # keine Zuweisung von neuen Attributen möglich wegen slots


r2d2 = Robot("R2D2", 43)
# r2d2.age = 3  # keine Zuweisung von neuen Attributen möglich wegen slots
print("Power:", r2d2.power)
r2d2.power = 100
# print(vars(r2d2)) # kein __dict__ zugriff wegen slots

# Statt dict müsste man sowas nutzen, um die aktuell
# Werte auszulesen
for attr in r2d2.__slots__:
    print(attr, getattr(r2d2, attr))
