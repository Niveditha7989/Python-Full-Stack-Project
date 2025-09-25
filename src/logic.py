from src.db import DatabaseManager

class GroceryStore:
    def __init__(self):
        self.db = DatabaseManager()

    def add_products(self, namee, price, quantity):
        if not namee or not price or not quantity:
            return {"Success": False, "Message": "Product name, price and quantity are required"}
        
        result = self.db.add_product(namee, price, quantity)
        if result.status_code == 201:
            return {"Success": True, "Message": "Product added successfully"}
        else:
            return {"Success": False, "Message": "Failed to add product"}

    def get_products(self):
        result = self.db.get_all_products()
        if result.status_code == 200:
            return result.data
        else:
            return {"Success": False, "Message": "Failed to fetch products"}

    def mark_completed(self, product_id, purchase_quantity):
        if not product_id or not purchase_quantity:
            return {"Success": False, "Message": "Product ID and purchase quantity are required"}

        result = self.db.purchase_product(product_id, purchase_quantity)
        if result.get("success"):
            return {"Success": True, "Message": "Purchase completed successfully"}
        else:
            return {"Success": False, "Message": result.get("error", "Failed to complete purchase")}

    def delete_products(self, product_id):
        result = self.db.remove_product(product_id)
        if result.status_code == 200:
            return {"Success": True, "Message": "Product deleted successfully"}
        else:
            return {"Success": False, "Message": "Failed to delete product"}

    def get_total_sales(self):
        result = self.db.get_total_sales()
        if "total_sales" in result:
            return {"Success": True, "TotalSales": result["total_sales"]}
        else:
            return {"Success": False, "Message": "Failed to fetch total sales"}
    def update_product(self, product_id, namee=None, price=None, quantity=None):
        if not product_id:
            return {"Success": False, "Message": "Product ID is required"}
        # You can optionally validate inputs here, e.g., price > 0 etc.
        result = self.db.update_product(product_id, namee, price, quantity)
        if result.get("success"):
            return {"Success": True, "Message": "Product updated successfully"}
        else:
            return {"Success": False, "Message": result.get("error", "Failed to update product")}