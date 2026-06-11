"""
Enum: Modul für Enums (StrEnum, IntEnum)
"""

from enum import StrEnum, Enum


class DoorState(StrEnum):
    OPEN = "open"
    CLOSED = "closed"
    LOCKED = "locked"


print("Tür ist offen:", type(DoorState.OPEN), DoorState.OPEN)


class Door:
    def __init__(self, initial_state: DoorState) -> None:
        self.state = initial_state


door = Door(initial_state=DoorState.CLOSED)
print(isinstance(DoorState.CLOSED, Enum))
