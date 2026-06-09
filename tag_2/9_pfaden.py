"""
mit Pfaden arbeiten
Mit Pfad-Objekt lässt sich die Existenz von Dateien und Verzeichnissen prüfen,
rekursiv Dateibäume
"""

from pathlib import Path

print(__file__)  # absoluter Pfad zur aktuellem Skript (String)

current_path = Path(__file__)  # erstellt ein Path-Objekt

# in dem path kann ich mit parent nach oben gehen im Directory-Tree
print(type(current_path), current_path.parent / "data" / "geo")

if current_path.exists():
    print("Der Pfad existiert")
