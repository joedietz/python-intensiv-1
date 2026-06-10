"""
Yield funktionen: Funktionen, die kein return zurückgeben, sondern einen Iterator
"""

import csv
from pathlib import Path
from typing import Generator


def infinite_counter():
    x = 0
    while True:
        yield x
        x += 1


# c = infinite_counter()
# print(next(c))
# print(next(c))
# print(next(c))
# for el in c:
#     print(el)


def read_volcanos(file: str) -> Generator:
    """Lese die aktiven Vulkane ein."""

    with open(file, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for entry in reader:
            yield entry


for entry in read_volcanos("active_volcanos.csv"):
    print(entry)
