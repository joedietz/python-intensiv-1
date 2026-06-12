"""

Parse list

1. Schreibe eine Funktion list_parse(), die eine Liste von Strings
entgegennimmt und versucht, die Elemente dieser Liste
in Floats zu konvertieren.

Es finden sich auch Strings in der Liste, die das Komma als
Dezimaltrennzeichen nutzen. Diese Werte gelten als legale Eingabe,
allerdings muss die Funktion die Kommas vorab durch Punkte ersetzen.

2.  Alle Strings, die nach Float konvertierbar sind, sollen
in einer Liste namens "cleaned" gespeichert werden.


3. Alle nicht zu Float konvertiereben Eingabestrings werden
in einer Fehlerliste "errors" gesammelt.
Diese muss die Originalstrings enthalten.

3. Der Rückgabewert der Funktion soll ein Tupel sein aus den Listen
cleaned und errors


Beispiel:
a = ["2", "a3", "0.2", "0,4", "a01", "3", ",", "a.a", "a,"]
cleaned, errors = list_parse(a)


Result:
cleaned = [2.0, 0.2, 0.4, 3.0]
errors = ['a3', 'a01', ',', 'a.a', 'a,']

"""

a = ["2", "a3", "0.2", "0,4", "a01", "3", ",", "a.a", "a,"]

from typing import Sequence


def list_parse(values: Sequence[str]) -> tuple[list[float], list[str]]:
    cleaned: list[float] = []
    errors: list[str] = []

    for value in values:
        try:
            cleaned.append(float(value.replace(",", ".")))
        except ValueError:
            errors.append(value)

    return cleaned, errors


a = ["2", "a3", "0.2", "0,4", "a01", "3", ",", "a.a", "a,"]

cleaned, errors = list_parse(a)

print(cleaned)
print(errors)
