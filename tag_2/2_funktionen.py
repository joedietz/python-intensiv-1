"""
Funktionsparameter / Argumente
*args: unbestimmte Anzahl an positionellen Argumenten
**kwargs: unbestimmte Anzahl an Keyword Argumenten
"""


def volume(a: int, b: int, c: int = 0) -> None:
    """c ist ein Parameter mit Defaultwert."""
    print(a, b)


volume(1, 2)  # positionelle Argumente
volume(b=2, a=1)
volume(a=2, b=1, c=11)  # keyword args


def catchall(a, b, *args):
    print("a,b:", a, b)
    print(type(args), args)


catchall(1, 2, 3, 4, 5)


def load_config(volume, *, system, **kwargs):
    """Alles rechts von dem * muss per Keyword-Arg übergeben werden."""
    print(kwargs)
    if "load_config" in kwargs:
        print(kwargs["load_config"])


load_config(100, system=True, load_config="config.txt", verbose=False)
