# Frontend/app.py
import streamlit as st
import os, sys
from datetime import datetime

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.logic import GroceryStore

store = GroceryStore()
st.set_page_config(page_title="Grocery Store Management", page_icon="🛒")
st.title("Grocery Store Management System")

menu = ["View Products", "Add Product", "Purchase Product", "Update Product", "Delete Product", "View Sales", "View Total Sales"]
choice = st.sidebar.selectbox("Menu", menu)

# --- View Products ---
if choice == "View Products":
    st.header("All Products")
    products = store.get_products()
    if products:
        for p in products:
            st.write(f"ID: {p['product_id']} | Name: {p['namee']} | Price: ${p['price']} | Quantity: {p['quantity']}")
    else:
        st.info("No products available")

# --- Add Product ---
elif choice == "Add Product":
    st.header("Add New Product")
    namee = st.text_input("Product Name")
    price = st.number_input("Price", min_value=0.0, format="%.2f")
    quantity = st.number_input("Quantity", min_value=0, step=1)
    if st.button("Add Product"):
        result = store.add_products(namee, price, quantity)
        if result.get("Success"):
            st.success(result.get("Message"))
        else:
            st.error(result.get("Message"))

# --- Purchase Product ---
elif choice == "Purchase Product":
    st.header("Purchase Product")
    products = store.get_products()
    product_options = {f"{p['product_id']} - {p['namee']}": p['product_id'] for p in products} if products else {}
    selected = st.selectbox("Select Product", list(product_options.keys()))
    purchase_qty = st.number_input("Quantity to Purchase", min_value=1, step=1)
    if st.button("Purchase"):
        pid = product_options.get(selected)
        result = store.mark_completed(pid, purchase_qty)
        if result.get("Success"):
            st.success(result.get("Message"))
        else:
            st.error(result.get("Message"))

# --- Update Product ---
elif choice == "Update Product":
    st.header("Update Product")
    products = store.get_products()
    product_options = {f"{p['product_id']} - {p['namee']}": p for p in products} if products else {}
    selected = st.selectbox("Select Product", list(product_options.keys()))
    if selected:
        p = product_options[selected]
        namee = st.text_input("Product Name", value=p['namee'])
        price = st.number_input("Price", value=p['price'], format="%.2f")
        quantity = st.number_input("Quantity", value=p['quantity'], min_value=0, step=1)
        if st.button("Update Product"):
            result = store.update_product(p['product_id'], namee, price, quantity)
            if result.get("Success"):
                st.success(result.get("Message"))
            else:
                st.error(result.get("Message"))

# --- Delete Product ---
elif choice == "Delete Product":
    st.header("Delete Product")
    products = store.get_products()
    product_options = {f"{p['product_id']} - {p['namee']}": p['product_id'] for p in products} if products else {}
    selected = st.selectbox("Select Product", list(product_options.keys()))
    if st.button("Delete Product"):
        pid = product_options.get(selected)
        result = store.delete_products(pid)
        if result.get("Success"):
            st.success(result.get("Message"))
        else:
            st.error(result.get("Message"))

# --- View Sales ---
elif choice == "View Sales":
    st.header("Sales Table")
    sales = store.get_sales_table()
    if sales:
        for s in sales:
            st.write(f"Sale ID: {s['sale_id']} | Product ID: {s['product_id']} | Quantity: {s['quantity']} | Total: ${s['total_price']:.2f}")
    else:
        st.info("No sales yet")

# --- View Total Sales ---
elif choice == "View Total Sales":
    st.header("Total Sales")
    total = store.get_total_sales()
    st.write(f"💰 Total Sales: ${total.get('TotalSales', 0):.2f}")


