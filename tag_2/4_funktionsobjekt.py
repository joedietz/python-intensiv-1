"""
Funktionsobjekt
"""


def summe(a, b):
    return a + b


def multiplikation(a, b):
    return a * b


def fn():
    pass


fn()  # Aufruf
x = fn
x()




def controller(operator, a, b):
    print(f"{operator} a+b", operations[operator](a, b))


operations = {
    "+": summe,
    "*": multiplikation,
}

controller(operator="+", 3, 2)
