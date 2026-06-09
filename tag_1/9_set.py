"""
Datentyp set (Menge)
veränderlicher Datentyp, darf auch nur unveränderliche Werte enthalten
"""

d = {}  # leeres Dict!
t = ()
ll = []  # leeres
print("Type von t:", type(t))

s = set()  # Leeres Set

#
namen = list(set(["Bob", "Bob", "Alice"]))
print(namen)

# Iteration über Set
s = {"a", "b", "c"}
s = iter(s)
print("Next von s:", next(s))

print(type(s))  # set_iterator
for element in s:
    print(element)


# Prüfen, ob zwei Listen ein gemeinsames Element haben
alfa = [1, 3, 5, 6]
beta = [99, 3, 2, 6]

# & => Schnittmengen-Operator ({3, 6})
if set(alfa) & set(beta):
    print("alfa und beta haben min. ein gemeinsames Element")
    print(set(alfa) & set(beta))


values = frozenset([2, 1, 1, 1, 1, 2, 2, 2])  # {1,2}
d = {}
d[(1, 2)] = 42
d[values] = 44
print(d[frozenset([2, 1, 1, 1])])
