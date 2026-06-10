"""
python kennt keine Zugriffsmodifikatoren (public, private, protected)

in Python sind alle Attribute und Methoden public und non_public
(non_public hat einen Unterstrich als Präfix, zb. _name)

Getter und Setter sind in Python als Properties umgesetzt
"""

import os

os.system("cls")


class User:
    def __init__(self, name: str, email: str = "") -> None:
        self.name = name  # public, ruft den Setter @name.setter auf
        self.email = email

    @property
    def name(self) -> str:
        """Getter für das Attribut name"""
        return self._name

    @name.setter
    def name(self, new_name: str) -> None:
        """Setter für das Attribut name"""
        self._name = new_name

    @property
    def email(self) -> str:
        """Getter für das Attribut name"""
        return self._name

    @email.setter
    def email(self, new_email: str) -> None:
        """Setter für das Attribut name"""
        if "@" not in new_email:
            raise ValueError("Kein @ enthalten!")
        self._email = new_email


user = User(name="Bob", email="hallo@example.com")
user.name = "Bobby"
print("id von user:", id(user))
# user._email = ""  VERMEIDEN

# Alle Attribute eines Objekts ausgeben
print(vars(user))  # user.__dict__

print(id(user) == id(user))  # Identitäten vergleichen
print(user is user)  # Kurzschreibweise für Identitätsvergleich mit Identität-Operator

x = None

if x is None:
    print("x ist None")


# Unwahr, weil diese hohen Werte nicht von Python vorbelegt sind
if 10**50 is 10**50:
    print("wahr")
else:
    print("unwahr")
