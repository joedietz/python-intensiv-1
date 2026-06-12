from fastapi import FastAPI
from .schema import ProductIn, ProductOut
from .db import get_products


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/products", response_model=list[ProductOut])
def products() -> list[ProductOut]:
    return get_products()


@app.post("/products")
def save_product(product: ProductIn) -> ProductOut:
    return ProductOut(
        id=2,
        name=product.name,
        price=product.price,
    )
