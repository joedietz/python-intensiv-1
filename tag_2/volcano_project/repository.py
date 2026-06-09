"""
Stellt Funktionen zum Lesen und Schreiben bereit
"""

import csv
import json

from pathlib import Path


def read_volcanos(file: Path, country: str) -> list[dict]:
    """Lese die aktiven Vulkane ein."""
    volcanos: list[dict] = []
    with open(file, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for entry in reader:
            if entry["Country"] == country and entry["risk"] != "NULL":
                volcanos.append(
                    {
                        "name": entry["V_Name"],
                        "risk": entry["risk"],
                        "lat": entry["Latitude"],
                        "long": entry["Longitude"],
                        "country": entry["Country"],
                        "region": entry["Region"],
                    }
                )
        return volcanos


def write_volcanos(file: Path, volcanos: list[dict]) -> None:
    """Schreibe eine Liste von Dictionaties in eine Json-Datei."""
    with open(file, mode="w", encoding="utf-8") as f:
        json.dump(volcanos, f, indent=4)


# __name__ ist __main__, wenn das Modul direkt aufgerufen
# wird. Ansonsten ist der Name `repository`
if __name__ == "__main__":
    print("Name von Repositry:", __name__)
