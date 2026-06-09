"""
Hashmap: dict
Veränderlich
"""

user_info: dict = {
    "name": "Bob",
    "age": 43,
    "hobbies": ["Laufen", "Coding"],
}

user_info["name"] = "Alice"

for key in user_info:
    print(f"Key {key}")

for key, value in user_info.items():
    print(f"Key {key}, Value: {value}")

# print(user_info["weight"]) # KeyError: 'weight'
print(user_info.get("weight", 42))

user_info["city"] = "hh"


def count_words(values: list[str]) -> dict:
    d = {}
    for value in values:
        d[value] = d.get(value, 0) + 1
        # if value in d:
        #     d[value] += 1
        # else:
        #     d[value] = 1
    return d


# Aufgabe: Zählen von Worten
values = ["aa", "aa", "a", "bb", "b", "a"]  # {"aa": 2, "a":2, "bb":1, "b":1}
result = count_words(values)
print(result)

default_config = {
    "timeout": 30,
    "verbose": False,
    "server": "127.0.0.1",
}


def parse_config(response: dict) -> dict:
    """Response Dict überschreibt Default-Config."""
    default_config.update(response)
    print("Überschriebene Default Config:", default_config)


parse_config(
    {
        "timeout": 15,  # überschreibt default_config
        "verbose": True,  # überschreibt default_config
        "test": True,  # neu, wird in default_config eingetragen
    }
)

# mit zip und dict ein Dict erstellen auf Basis von 2 Iterables
# Zip: mehrere Iterables elementweise ausgeben
names = ["Bob", "Alice", "Grumpy"]
grades = [1, 2, 1]

neues_dict: dict = dict(zip(names, grades))
print(neues_dict)


# Dict Comprehension
products = {"apples": 1.2, "cherries": 2.3}
products_cent = {product: price * 100 for product, price in products.items()}
print(products_cent)


def fn(parameter: dict):
    parameter.clear()


# Bei verändlichen Datentypen wird die Referenz übergeben
fn(products)
print(products)
