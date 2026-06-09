"""
Volcano-Projekte

Die Datei `active_volcanos.csv` einlesen und mit einem Länderfilter nach JSON
geschrieben werden.

csv-Modul: Reader / DictReader | Writer / DictWriter

Die Json-Einträge sollen enthalten:
Name des Vulkans
Risiko
Latitude
Longitude
Country
Region

die Json-Keys sollen folgende Namen haben:
name, risk, lat, long, country, region

python main.py
"""

import sys
from pathlib import Path

from repository import read_volcanos, write_volcanos

print("aktuell geladene Module")
for name, module in sys.modules.items():
    print(name, module)

# Zugriff auf ein Modul names Enum via sys.modules
enum_module = sys.modules["enum"]
print(enum_module.Enum)


def main():
    country = "Italy"
    file = Path(__file__).parent / "active_volcanos.csv"
    volcanos = read_volcanos(file, country=country)

    file = Path(__file__).parent / f"active_volcanos_{country}.json"
    write_volcanos(file, volcanos)


if __name__ == "__main__":
    main()
