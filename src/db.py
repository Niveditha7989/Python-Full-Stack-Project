import os
from supabase import create_client
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

supabase = create_client(url, key)

# Add new product
def add_product(namee, price, quantity):
    return supabase.table("productsss").insert({
        "namee": namee,
        "price": price,
        "quantity": quantity,
    }).execute()

# View all products
def get_all_products():
    return supabase.table("productsss").select("*").order("product_id").execute()

# Purchase product: reduce stock and track sales
def purchase_product(product_id, purchase_quantity):
    product_response = supabase.table("productsss").select("*").eq("product_id", product_id).single().execute()
    if product_response.status_code != 200 or not product_response.data:
        return {"error": "Product not found"}

    product = product_response.data
    current_quantity = product["quantity"]
    price = float(product["price"])

    if purchase_quantity > current_quantity:
        return {"error": "Not enough stock"}

    total_price = price * purchase_quantity

    update_response = supabase.table("productsss").update({
        "quantity": current_quantity - purchase_quantity
    }).eq("product_id", product_id).execute()

    if update_response.status_code != 200:
        return {"error": "Failed to update product stock"}

    sale_response = supabase.table("salesss").insert({
        "product_id": product_id,
        "quantity": purchase_quantity,
        "total_price": total_price
    }).execute()

    if sale_response.status_code != 201:
        return {"error": "Failed to log sale"}

    return {"success": True, "sale": sale_response.data}

# Remove product
def remove_product(product_id):
    return supabase.table("productsss").delete().eq("product_id", product_id).execute()

# View total sales (sum total_price)
def get_total_sales():
    sales_response = supabase.table("salesss").select("total_price").execute()
    if sales_response.status_code != 200:
        return {"error": "Failed to fetch sales"}

    total = sum(float(sale["total_price"]) for sale in sales_response.data)
    return {"total_sales": total}
