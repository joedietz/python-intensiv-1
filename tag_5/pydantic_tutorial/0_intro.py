from pathlib import Path
import json
from typing import Literal

import pydantic

file = Path(__file__).parent / "data.json"
with open(file, encoding="utf-8") as f:
    data = json.load(f)
    print(data)


class Wizard(pydantic.BaseModel):
    id: int
    name: str
    age: int
    magic: int
    origin: str | None = None
    history: list[int]  # StrictInt
    type: Literal["wizard", "witcher"]

    @pydantic.field_validator("age")
    @classmethod
    def validate_age(cls, value: int) -> int:
        if value > 1300:
            raise ValueError("Wizard ist zu alt")
        return value


# Ein Objekt erstellen
# d = Wizard(id="3", name="Bob")
# print(d.id, type(d.id))

wizards = [Wizard(**entry) for entry in data]
print(wizards)
