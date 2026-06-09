"""
Dateien öffnen und lesen
"""

from pathlib import Path

# Path-Objekt erlaubt via /-Operatorenübladung diese Syntax
DATA_DIR = Path(__file__).parent / "data.txt"

# oldschool
f = open(DATA_DIR, mode="r", encoding="utf-8")
content = f.read()
print(content)
f.close()


def read_file(directory: Path) -> str:
    # Kontext-Manager schliesst File-Handle automatisch
    with open(directory, mode="r", encoding="utf-8") as f:
        content = f.read()
        return content


content = read_file(DATA_DIR)


with open(DATA_DIR, mode="r", encoding="utf-8") as f:
    for index, line in enumerate(f):
        print(index, line.strip())  # mit strip() die Newlines löschen
