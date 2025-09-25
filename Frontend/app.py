import streamlit as st
import requests

# Base URL of your FastAPI backend
BASE_URL = "http://localhost:8000"

st.title("Grocery Store Management System")

# --- Helper functions to call API ---

def get_products():
    resp = requests.get(f"{BASE_URL}/store")
    if resp.status_code == 200:
        return resp.json()
    else:
        st.error("Failed to fetch products")
        return []

def add_product(namee, price, quantity):
    payload = {
        "namee": namee,
        "price": price,
        "quantity": quantity
    }
    resp = requests.post(f"{BASE_URL}/store", json=payload)
    return resp

def purchase_product(product_id, purchase_quantity):
    payload = {"purchase_quantity": purchase_quantity}
    resp = requests.post(f"{BASE_URL}/store/{product_id}/purchase", json=payload)
    return resp

def update_product(product_id, namee=None, price=None, quantity=None):
    payload = {}
    if namee:
        payload["namee"] = namee
    if price is not None:
        payload["price"] = price
    if quantity is not None:
        payload["quantity"] = quantity
    resp = requests.put(f"{BASE_URL}/store/{product_id}", json=payload)
    return resp

def delete_product(product_id):
    resp = requests.delete(f"{BASE_URL}/store/{product_id}")
    return resp

def get_total_sales():
    resp = requests.get(f"{BASE_URL}/store/total-sales")
    if resp.status_code == 200:
        return resp.json().get("TotalSales")
    else:
        st.error("Failed to fetch total sales")
        return None

# --- Streamlit UI ---

menu = ["View Products", "Add Product", "Purchase Product", "Update Product", "Delete Product", "View Total Sales"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "View Products":
    st.header("All Products")
    products = get_products()
    if products:
        for p in products:
            st.write(f"ID: {p['product_id']} | Name: {p['namee']} | Price: ${p['price']} | Quantity: {p['quantity']}")

elif choice == "Add Product":
    st.header("Add New Product")
    namee = st.text_input("Product Name")
    price = st.number_input("Price", min_value=0.0, format="%.2f")
    quantity = st.number_input("Quantity", min_value=0, step=1)
    if st.button("Add Product"):
        if not namee or price <= 0 or quantity <= 0:
            st.error("Please provide valid name, price, and quantity")
        else:
            resp = add_product(namee, price, quantity)
            if resp.status_code == 200:
                st.success("Product added successfully!")
            else:
                st.error(f"Failed to add product: {resp.json().get('detail', 'Unknown error')}")

elif choice == "Purchase Product":
    st.header("Purchase Product")
    products = get_products()
    product_options = {f"{p['product_id']} - {p['namee']}": p['product_id'] for p in products} if products else {}
    selected_product = st.selectbox("Select Product", options=list(product_options.keys()))
    purchase_quantity = st.number_input("Purchase Quantity", min_value=1, step=1)
    if st.button("Purchase"):
        product_id = product_options.get(selected_product)
        resp = purchase_product(product_id, purchase_quantity)
        if resp.status_code == 200:
            st.success("Purchase completed successfully!")
        else:
            st.error(f"Purchase failed: {resp.json().get('detail', 'Unknown error')}")

elif choice == "Update Product":
    st.header("Update Product Details")
    products = get_products()
    product_options = {f"{p['product_id']} - {p['namee']}": p for p in products} if products else {}
    selected_product = st.selectbox("Select Product", options=list(product_options.keys()))
    if selected_product:
        p = product_options[selected_product]
        namee = st.text_input("Product Name", value=p['namee'])
        price = st.number_input("Price", min_value=0.0, format="%.2f", value=p['price'])
        quantity = st.number_input("Quantity", min_value=0, step=1, value=p['quantity'])
        if st.button("Update Product"):
            product_id = p['product_id']
            resp = update_product(product_id, namee=namee, price=price, quantity=quantity)
            if resp.status_code == 200:
                st.success("Product updated successfully!")
            else:
                st.error(f"Update failed: {resp.json().get('detail', 'Unknown error')}")

elif choice == "Delete Product":
    st.header("Delete Product")
    products = get_products()
    product_options = {f"{p['product_id']} - {p['namee']}": p['product_id'] for p in products} if products else {}
    selected_product = st.selectbox("Select Product to Delete", options=list(product_options.keys()))
    if st.button("Delete Product"):
        product_id = product_options.get(selected_product)
        resp = delete_product(product_id)
        if resp.status_code == 200:
            st.success("Product deleted successfully!")
        else:
            st.error(f"Delete failed: {resp.json().get('detail', 'Unknown error')}")

elif choice == "View Total Sales":
    st.header("Total Sales")
    total_sales = get_total_sales()
    if total_sales is not None:
        st.write(f"💰 Total Sales: ${total_sales:.2f}")
