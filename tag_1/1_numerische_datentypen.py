"""
Numerische Datentypen
- Integer (unbegrenzt groß)
- Floats (float, 64 bit IEEE 754)
- Komplexe Zahlen 4i

arithmetische Operatoren
x + y   Summe von x und y
x - y   Differenz von x und y
x * y   Produkt von x und y
x / y   Quotient von x und y
x % y   Rest beim Teilen von x durch y*
+x  positives Vorzeichen
-x  negatives Vorzeichen
x ** y  x hoch y
x // y  abgerundeter Quotient von x und y*

type gibt den Datentyp eines Objekts
"""

x: int = 2348
y: float = 34.2

# Leerzeichen vor und nach dem OPerator, mit Ausnahme von **
result = x + y
z = x**2  # hoch zwei

# Division erzeugt immer ein Float
res = 4 / 2
print(type(res))  # <class 'float'>


res = int(res)
print(type(res))

# Floor Division rundet negativ richtung negativ Unendlich
print("8/3:", 8 // 3, 8 / 3)
print("-8/3:", -8 // 3, -8 / 3)

# String multiplizieren
print("*" * 40)

# INcrement
x = 1
# x++ Syntax Fehler
x += 1
