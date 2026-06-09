"""
1. Vokale zählen (MITTEL)
Schreibe eine Funktion count_vowels() die einen String als Parameter erwartet,
und alle Vokale  in diesem String zählt. Der Rückgabewert der Funktion ist die
Anzahl der Vokale (int). Als Vokale zählen im deutschen: aeiouüäö
Beachte Groß- und Kleinschreibung! Auge hat 3 Vokale

Beispiel:
number_of_vowels = count_vowels("teleport").
print(number_of_vowels)
// 3

number_of_vowels = count_vowels("Ööll").
print(number_of_vowels)
// 2
"""

"""
3. Liste filtern (MITTEL)
Schreibe eine Funktion filter_input(), die eine Liste A entgegennimmt und
anhand einer weiteren Liste B mit erlaubten Werten prüft, ob diese Werte
zulässig sind. Rückgabewert der Funktion ist eine Liste mit Werten, die
mithilfe B geprüft worden ist.

Beispiel
input_filtered = filter_input([1, 3, 4, 5, 3], [3, 4])
print(input_filtered)
// [3, 4, 3]

input_filtered = filter_input([1, 3, 4, 5, 3], [])
print(input_filtered)
// []

input_filtered = filter_input(["gold", "gelb", "gelb", "rot", "gelb"], ["gelb", "rot"])
// ["gelb", "gelb", "rot", "gelb"]
"""

"""
4. Rückwärts (SCHWER)
Schreibe eine Funktion reverse_cutter(), die einen String entgegennimmt, diesen
zu Kleinbuchstaben transformiert, den ersten und letzten Index abschneidet und
das Ergebnis umgedreht zurückgibt. Ein Input kleiner gleich Länge zwei gibt
einen leeren String zurück.  Beispiel:
reversed = reverse_cutter("Petersburg")
// rubsrete
"""


def reverse_cutter(value: str) -> str:
    """Schneide 1. und letzen Index ab und transformiere zu Kleinbuchstaben."""
    s = value[1:-1]
    return s[::-1].lower()


reverse_cutter("PeterSburg")


"""
5. Max (MITTEL)
Implementiere die Funktion max. Diese soll aus einer gegebenen Liste von
Integerwerten den größten Wert zurückgeben. Nutze dazu nicht die Built-In
Funktion max oder max aus dem Numpy-Modul! Die Funktion soll None zurückgeben,
wenn eine leere Liste übergeben wurde.  

Beispiel:
values = [3, 2, 4]
x_max = max(values)
// 4

values = []
x_max = max(values)
// None
"""
