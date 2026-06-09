"""
Lambda Funktionen (anonyme Funktionen), Wegwerf-Funktionen
Lambda erzeugt eine Funktionsreferenz

Schema:
lambda <PARAMETER>: EXPRESSION (ist auch die Rückgabe)
"""


def f(a, b):
    return a + b


p = lambda a, b: a + b
print(type(p))

print(p(2, 4))
