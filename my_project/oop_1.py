"""
OOP in Python
"""


class User:
    city = "Nürnberg"

    def __init__(self, name: str) -> None:
        self.name = name
        self.age = None

    def __str__(self) -> str:
        """String-Repräsentation von dem Objekt.
        Dunder-String."""
        return self.name

    def __repr__(self) -> str:
        """Zum Nachstellen eines Objekts im Ist-Zustand. repr()
        User('name')
        """
        return f"User({repr(self.name)})"

    def __len__(self) -> int:
        return 42


user = User(name="Bob")  # x = int(3)
user2 = User(name="Alice")
print(dir(user))  # Alle Attribute und Methoden dieses Objekts
print(user.__class__)
user.city = "Fürth"  # hier erstelle ich ein neues Attribut
print("User Objekt Stadt:", user.city, vars(user))
print("Alice Objekt Stadt:", user2.city, vars(user2))
# Negativ-Beispiel: dynamisch Attribute hinzufügen
# user.age = 42
# print(user.age)

print(user)
user_string = str(user)  # ruft __str__ auf, len => __len__
print(f"User String: {user_string}")
print(f"Len von User: {len(user)}")
print(f"Repr von User: {repr(user)}")
