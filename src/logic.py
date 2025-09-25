# src/logic.py
from src.db import add_product, get_all_products, update_product, remove_product, purchase_product, get_total_sales, get_sales

class GroceryStore:
    # --- Products ---
    def add_products(self, namee, price, quantity):
        if not namee or price <= 0 or quantity <= 0:
            return {"Success": False, "Message": "Invalid input"}
        resp = add_product(namee, price, quantity)
        if resp.data:
            return {"Success": True, "Message": "Product added successfully"}
        return {"Success": False, "Message": "Failed to add product"}

    def get_products(self):
        resp = get_all_products()
        if resp.data is not None:
            return resp.data
        return []

    def update_product(self, product_id, namee=None, price=None, quantity=None):
        resp = update_product(product_id, namee, price, quantity)
        if resp and resp.data is not None:
            return {"Success": True, "Message": "Product updated successfully"}
        return {"Success": False, "Message": "Failed to update product"}

    def delete_products(self, product_id):
        resp = remove_product(product_id)
        if resp.data is not None:
            return {"Success": True, "Message": "Product deleted successfully"}
        return {"Success": False, "Message": "Failed to delete product"}

    # --- Purchase ---
    def mark_completed(self, product_id, purchase_quantity):
        resp = purchase_product(product_id, purchase_quantity)
        if resp.get("success"):
            return {"Success": True, "Message": "Purchase completed successfully"}
        return {"Success": False, "Message": resp.get("error", "Failed")}

    # --- Sales ---
    def get_total_sales(self):
        return get_total_sales()

    def get_sales_table(self):
        resp = get_sales()
        if resp.data is not None:
            return resp.data
        return []




