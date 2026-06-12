from pathlib import Path
from .schema import ProductOut
import sqlite3

from typing import NamedTuple


class Product(NamedTuple):
    id: int
    name: str
    price: float
    stock: int


DATABASE_FILE = Path(__file__).parent / "products.db"


def get_products() -> list[dict]:
    with sqlite3.connect(DATABASE_FILE) as conn:
        cursor: sqlite3.Cursor = conn.cursor()
        cursor.execute(
            """
            SELECT
                id,
                name,
                price,
                stock
            FROM products
            """
        )
        rows = cursor.fetchall()

        return [
            {
                "id": row[0],
                "name": row[1],
                "price": row[2],
                "stock": row[3],
            }
            for row in rows
        ]
