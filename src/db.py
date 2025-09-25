# src/db.py
import os
from supabase import create_client
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

supabase = create_client(url, key)

# --- Product operations ---

def add_product(namee, price, quantity):
    return supabase.table("productsss").insert({
        "namee": namee,
        "price": price,
        "quantity": quantity
    }).execute()

def get_all_products():
    return supabase.table("productsss").select("*").order("product_id").execute()

def update_product(product_id, namee=None, price=None, quantity=None):
    # Fetch current product
    product_resp = supabase.table("productsss").select("*").eq("product_id", product_id).single().execute()
    if not product_resp.data:
        return None

    current_quantity = product_resp.data["quantity"]

    data = {}
    if namee is not None:
        data["namee"] = namee
    if price is not None:
        data["price"] = price
    if quantity is not None:
        data["quantity"] = current_quantity + quantity  # <-- add new stock to existing

    if not data:
        return None

    return supabase.table("productsss").update(data).eq("product_id", product_id).execute()


def remove_product(product_id):
    return supabase.table("productsss").delete().eq("product_id", product_id).execute()

# --- Purchase / Sales operations ---

def purchase_product(product_id, purchase_quantity):
    product_resp = supabase.table("productsss").select("*").eq("product_id", product_id).single().execute()
    if not product_resp.data:
        return {"success": False, "error": "Product not found"}

    product = product_resp.data
    if purchase_quantity > product["quantity"]:
        return {"success": False, "error": "Not enough stock"}

    total_price = purchase_quantity * float(product["price"])

    # Update product stock
    supabase.table("productsss").update({
        "quantity": product["quantity"] - purchase_quantity
    }).eq("product_id", product_id).execute()

    # Record sale
    sale_resp = supabase.table("salesss").insert({
        "product_id": product_id,
        "quantity": purchase_quantity,
        "total_price": total_price
    }).execute()

    if sale_resp.data:
        return {"success": True, "sale": sale_resp.data}
    else:
        return {"success": False, "error": "Failed to log sale"}

def get_total_sales():
    sales_resp = supabase.table("salesss").select("total_price").execute()
    if not sales_resp.data:
        return {"Success": True, "TotalSales": 0}
    total = sum(float(sale["total_price"]) for sale in sales_resp.data)
    return {"Success": True, "TotalSales": total}

def get_sales():
    return supabase.table("salesss").select("*").order("sale_id").execute()



