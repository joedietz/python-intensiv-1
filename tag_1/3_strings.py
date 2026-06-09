"""
String
"""

first_name = "Bob"
print(type(first_name))  # <class 'str'>

multiline_text: str = """
Dies ist ein mehrzeiliger
String, der auch Zeilenumbrüche
enthält."""

print(multiline_text)

# In-Operator
if "auch" in multiline_text:
    print("auch kommt vor")

# String Vergleich
if "aaaa" == "bbbb":
    print("Strings sind gleich")

# Split (Methoden erzeugen entweder neuen String oder neuen Typen)
values = "a,343,343,23"
values_list = values.split(",")
print(values_list)

# len (Länge einer Sequenz)
print("Länge eines Strings:", len(values))
# values.__len__()

# Index-Operator
print("Zeichen an Stelle 3:", values[3])

# Slicing Operation ([start:stop:schrittweite])
print("Index 0-5:", values[0:6])  # index 0 - Index 6 (exclusive)
print("von negativem Index bis Ende:", values[-3:])
print("Schrittweite 2", values[::2])
print("eine Sequenz umdrehen:", values[::-1])
