from dataclasses import dataclass
from pathlib import Path
import sqlite3

DATABASE_FILE = Path(__file__).parent / "products.db"


@dataclass
class Product:
    name: str
    price: float
    stock: int
    id: int | None = None


def create_connection() -> sqlite3.Connection:
    """Baue Verbindung zur Datenbank auf."""
    return sqlite3.connect(DATABASE_FILE)


def create_table(conn: sqlite3.Connection) -> None:
    """Eine Produkt-Tabelle erstellen."""
    cursor: sqlite3.Cursor = conn.cursor()
    sql = """ 
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price REAL NOT NULL,
        stock INTEGER NOT NULL
    );
    """
    cursor.execute(sql)
    conn.commit()


def insert_product(conn: sqlite3.Connection, product: Product) -> None:
    cursor: sqlite3.Cursor = conn.cursor()
    sql = """ 
        INSERT INTO products (
        name, price, stock
        ) 
        VALUES (?, ?, ?)
    """
    # asdict macht aus einer Dataclass ein Dict. values() macht aus einem Dict
    # eine Werte-Liste. Um den Type-checker zu beruhigen, wird das ganze als tuple
    # ge
    # values = tuple(asdict(product).values())
    cursor.execute(sql, (product.name, product.price, product.stock))
    conn.commit()


def get_product_by_id(conn: sqlite3.Connection, product_id: int) -> Product:
    cursor: sqlite3.Cursor = conn.cursor()
    cursor.execute(
        """
        SELECT
            id,
            name,
            price,
            stock
        FROM products
        WHERE id = ?
        """,
        (product_id,),
    )
    result = cursor.fetchone()
    return Product(result[1], result[2], result[3], result[0])


def main():

    apple = Product(name="Apfel", price=23.2, stock=3)

    # conn = create_connection()
    with sqlite3.connect(DATABASE_FILE) as conn:
        create_table(conn)
        insert_product(conn, product=apple)
        apple: Product = get_product_by_id(conn, product_id=1)
        print(apple)
        # conn.close()


if __name__ == "__main__":
    main()
