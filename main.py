from fastapi import FastAPI
from app.models.product import Product

app = FastAPI()

products = [
    Product(id=1, name="Tomato", price=40),
    Product(id=2, name="Potato", price=30),
    Product(id=3, name="Onion", price=35)
]

@app.get("/")
def home():
    return {"message": "Vegetable Delivery Backend Running"}

@app.get("/products")
def get_products():
    return products