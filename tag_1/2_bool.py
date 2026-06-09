"""
Bedingte Anweisungen

Truth und False
"""

x: int = 42
print(type(x > 24))  # <class 'bool'>

if x > 34:
    print("x größer als 34")
elif x == 100:
    print("x ist 100")
else:
    print("irgendwas")


# Datentyp Liste
numbers = []
if numbers:
    print("Sind WErte enthalten")

# Ternary Operator
result = 42 if 3 > 4 else 5
print(result)
