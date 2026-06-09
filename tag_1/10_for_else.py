"""
for-else:
Else wird immer ausgeführt, wenn NICHT mit break
abgebrochen wurde.
"""

found = False

rabbits = [
    "fiver34",
    "hazel29",
    "bigwig89",
    "blackberry32",
]

for rabbit in rabbits:
    if "fivver" in rabbit:
        print("Fiver wurde gefunden")
        found = True
        break


if not found:
    print("wurde nicht gefunden")

print("*" * 40)

############ Pythonische Lösung ##########
for rabbit in rabbits:
    if "fivver" in rabbit:
        print("Fiver wurde gefunden")
        break
else:
    # wenn nicht break mit abgerochen
    print("wurde nicht gefunden")
