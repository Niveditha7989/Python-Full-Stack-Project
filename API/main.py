# api/main.py
import sys, os, datetime
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.logic import GroceryStore

app = FastAPI(title="Grocery Store Management System", version="1.0")

# Allow frontend (Streamlit/React)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

store = GroceryStore()

# --- Data Models ---
from pydantic import BaseModel

class ProductCreate(BaseModel):
    namee: str
    price: float
    quantity: int

class ProductUpdate(BaseModel):
    namee: str | None = None
    price: float | None = None
    quantity: int | None = None

class PurchaseRequest(BaseModel):
    purchase_quantity: int

# --- Routes ---
@app.get("/")
def home():
    return {"message": "API running"}

@app.get("/store")
def get_products():
    return store.get_products()

@app.post("/store")
def create_products(product: ProductCreate):
    result = store.add_products(product.namee, product.price, product.quantity)
    if not result.get("Success"):
        raise HTTPException(status_code=400, detail=result.get("Message"))
    return result

@app.put("/store/{product_id}")
def update_product(product_id: int, product: ProductUpdate):
    result = store.update_product(product_id, product.namee, product.price, product.quantity)
    if not result.get("Success"):
        raise HTTPException(status_code=400, detail=result.get("Message"))
    return result

@app.delete("/store/{product_id}")
def delete_product(product_id: int):
    result = store.delete_products(product_id)
    if not result.get("Success"):
        raise HTTPException(status_code=400, detail=result.get("Message"))
    return result

@app.post("/store/{product_id}/purchase")
def purchase(product_id: int, purchase: PurchaseRequest):
    result = store.mark_completed(product_id, purchase.purchase_quantity)
    if not result.get("Success"):
        raise HTTPException(status_code=400, detail=result.get("Message"))
    return result

@app.get("/store/total-sales")
def total_sales():
    result = store.get_total_sales()
    if not result.get("Success"):
        raise HTTPException(status_code=400, detail="Failed to fetch total sales")
    return result

@app.get("/store/sales")
def view_sales():
    return store.get_sales_table()


