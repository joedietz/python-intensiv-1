"""
Tuple, unveränderlich
"""

INTERVAL = (0, 3)


def fn() -> tuple:
    return 42, 43


# Tuple mit 3 Elementen, Klammer ist optional
x = (1, 2, 3)
y = 1, 2, 3

a, b = fn()

values = tuple([1])
z = (1,)  # Tuple mit 1 Element, (1) => Integer in der Klammer

person = ("Tom", 43, "Nürnberg")
