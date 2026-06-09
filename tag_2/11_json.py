"""
json Modul zum Einlesen und Schreiben von JSON-Dateien


https://www.json.org/json-en.html


Python                  JSON
-----------------------------------------
dict                =>  object
list, tuple         =>  array
str                 =>  string
int, float          =>  number
True                =>  true
False               =>  false
None                =>  null
"""

import json
from pathlib import Path

DATA_DIR = Path(__file__).parent / "result.json"

d = {
    "name": "Bob",
    "hobbies": ("Cöding", "Essen"),
    "age": 4,
}

json_string = json.dumps(d)  # erzeugt einen JSON-String
print(json_string)
print("*" * 40)
print(d)
print("*" * 40)
# Json String konvertieren nach Python
d2 = json.loads(json_string)
print(d2)

# konvertiere dict d nach JSON und speicher in Datei
with open(DATA_DIR, mode="w", encoding="utf-8", newline="\n") as f:
    json.dump(d, f)
