# Frontend --->API----->logic ------>db ------>Response
# api/main.py

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import sys
import os

# Import GroceryStore from src
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.logic import GroceryStore
#----------------------------App SetUp----------------
app = FastAPI(title="Grocery Store Management System", version="1.0")


#------------------------Allow forntend (Stremlit/React) or call the API----------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Creating a GroceryStore Instance(business logic)
grocery_store = GroceryStore()  # Instantiate your logic class

# ---------Data Models----------
class ProductCreate(BaseModel):
    namee: str
    price: float
    quantity: int

class PurchaseRequest(BaseModel):
    purchase_quantity: int

class ProductUpdate(BaseModel):
    namee: str 
    price: float 
    quantity: int 

@app.get("/")
def home():
    """Check if the api is running"""
    return {"message": "Grocery Store Management System API is running"}

@app.get("/store")
def get_products():
    """get all products"""
    return grocery_store.get_products()

@app.post("/store")
def create_products(product: ProductCreate):
    """Add a new product"""
    result = grocery_store.add_products(product.namee, product.price, product.quantity)
    if not result.get("Success"):
        raise HTTPException(status_code=400, detail=result.get("Message"))
    return result

@app.post("/store/{product_id}/purchase")
def purchase_product(product_id: int, purchase: PurchaseRequest):
    result = grocery_store.mark_completed(product_id, purchase.purchase_quantity)
    if not result.get("Success"):
        raise HTTPException(status_code=400, detail=result.get("Message"))
    return result

@app.put("/store/{product_id}")
def update_product(product_id: int, product: ProductUpdate):
    result = grocery_store.update_product(product_id, product.namee, product.price, product.quantity)
    if not result.get("Success"):
        raise HTTPException(status_code=400, detail=result.get("Message"))
    return result

@app.delete("/store/{product_id}")
def delete_product(product_id: int):
    result = grocery_store.delete_products(product_id)
    if not result.get("Success"):
        raise HTTPException(status_code=400, detail=result.get("Message"))
    return result

@app.get("/store/total-sales")
def total_sales():
    result = grocery_store.get_total_sales()
    if not result.get("Success"):
        raise HTTPException(status_code=400, detail=result.get("Message"))
    return result

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
