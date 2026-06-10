"""
Datencontainer, hat __repr__ und __eq__ implementiert
"""

from __future__ import annotations
from dataclasses import dataclass


@dataclass(frozen=True)
class Vector3D:
    x: int
    y: int
    z: int

    @classmethod
    def from_string(cls, csv_string: str) -> Vector3D:
        return cls(*[int(el) for el in csv_string.split(",")])
        # return cls(*map(int, csv_string.split(",")))


v1 = Vector3D(1, 2, 3)
print(v1.x)
v2 = Vector3D.from_string("1,2,3")
print(v2)
