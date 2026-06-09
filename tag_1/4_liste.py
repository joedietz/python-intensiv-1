"""
Liste: Container für unterschiedliche Datentypen
verändlicher Datentypen
für LinkedLists Daten deque aus dem Modul collections
"""

values: list[int] = [1, 2, 3, 4]
values[0] = 42

print("Datentype Liste:", type(values))
values.append(5)

# Slicing, Länge einer Sequenz
print(values[0:3], len(values))

a = [1, 2]
b = [3, 4]
c = a + b
print("Neue Liste c:", c)

if 1 in a:
    print("1 ist in a enthalten")


def print_values(values: list) -> None:
    for value in values:
        print(value)


values = [2, 3, 4]
print_values(values)

# Aufgabe: Funktion bekommt weiteren Parameter a.
# print_values soll eine Liste erstellen, mit Werten die > a sdind
# print_values(values, 3)  # soll eine Liste erzeugen, mit Werten, die > a sind
# print_values([1, 2, 3, 4], 2) => [3, 4]


def filter_values_oldschool(values: list, a: int) -> list:
    filtered_values: list = []
    for value in values:
        if value > a:
            filtered_values.append(value)
    return filtered_values


def filter_values(values: list, a: int) -> list:
    # als List Comprehension
    return [value for value in values if value > a]


result = filter_values([1, 2, 3, 4], 2)
print(result)

# Enumerate: Zugriff auf Name und Note
names = ["Bob", "Alice", "Grumpy"]
grades = [1, 2, 1]


enum = enumerate(names)
print(list(enum))  # [(0, 'Bob'), (1, 'Alice'), (2, 'Grumpy')]
a, b = [1, 2]  # unpacking

for index, name in enumerate(names):
    print(name, grades[index])


# Zip: mehrere Iterables elementweise ausgeben
names = ["Bob", "Alice", "Grumpy"]
grades = [1, 2, 1]
cities = ["Nürnberg", "Hamburg", "Berlin"]


# im Modul itertools zip_longest
for name, grade, city in zip(names, grades, cities):
    print(name, grade, city)

# Range (Schleife a la C)
for i in range(4):
    print("i:", i)
