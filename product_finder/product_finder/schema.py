from pydantic import BaseModel


class ProductIn(BaseModel):
    name: str
    price: float
    stock: int


class ProductOut(BaseModel):
    id: int
    name: str
    price: float
    stock: int = 3
