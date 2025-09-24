# Grocery Store Management System
The Grocery Store Management System is a console-based application designed to help small grocery store owners efficiently manage their product inventory, sales, and stock levels. It simplifies daily store operations by automating tasks like adding new products, tracking stock, processing purchases, and generating sales summaries.
## Features
> Add new products to the Database

> View all available products

> Purchase products (reduce stock and track sales)

> Remove products

> View total sales

# Add Product:
Add new products to the inventory with unique product IDs, names, prices, and stock quantities.

# View Products:
Display all available products along with details such as price and current stock.

# Purchase Product:
Process product sales by selecting a product ID and quantity. Automatically updates stock and tracks total sales amount.

# Remove Product:
Delete a product from the inventory using its product ID.

# View Total Sales:
Show the cumulative amount of money generated from all sales transactions.

## Project Structure

Grocery Store Management System/
|
|---src/             #core application logic
|     |---logic.py   #Business logic and task
operations
|     |__db.py       #Database operations
|
|----API/            #Backend API
|     |__main.py     #FastAPI endpoints
|
|----Frontend/       #Frontend application
|      |__app.py     #Streamlit web interface
|
|___requirements.txt  #Python Dependencies
|
|___README.md        #Project decumentation
|
|___.env             #Python Variables


## Quick Start

## Prerequisites

-Python 3.8 or higher
-A Supabase account
-Git(Push,cloning)

### 1.clone or Download the project
# option 1:clone with Git
git clone https://github.com/Niveditha7989/Python-Full-Stack-Project.git

# option 2:Download and extract the ZIP file

### 2.Install Dependencies

# Install all required Python packages
pip install -r requirements.txt

### 3.Set Up Supabase Database

1.Create a Supabase Project:
2.Create the Task Table:

-Go to the SQL Edition in your Supabase dashboard
-Run this SQL command:
``` sql
CREATE TABLE  Products (
    product_id SERIAL PRIMARY KEY,        
    namee VARCHAR(100) NOT NULL,
    price NUMERIC(10, 2) NOT NULL,
    quantity INTEGER NOT NULL
);


CREATE TABLE Sales (
    sale_id SERIAL PRIMARY KEY,       
    product_id INTEGER NOT NULL REFERENCES Products(product_id),
    quantity INTEGER NOT NULL,
    total_price NUMERIC(10, 2) NOT NULL,
    sale_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

```
3. **Get your Credentials:

### 4.Configure Environment Variables

1. Create a `.env` file in the Project root

2. Add your Supabase credentials to `.env` 
SUPABASE_URL=your_project_url_here
SUPABASE_KEY=your_anon_key_here

**Example:**
SUPABASE_URL="https://ympcewkbqmcnizeskpsq.supabase.co"
SUPABASE_KEY="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InltcGNld2ticW1jbml6ZXNrcHNxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTgwODM1NTIsImV4cCI6MjA3MzY1OTU1Mn0.DMnicaYE4VvnTRtcV3LeR6CniqHoJ6WooGN24cZJON0"


### 5.Run the Application

## Streamlit Frontend
streamlit run frontend/app.py


The app will open in your browser at `http://localhost:3000`

## FASTAPI Backend

cd API
python main.py

The API will be available at `http://localhost:8000`

# How to Use

## Technical Details

### Technologies Used

-**Frontend**:Streamlit(Python web framework)
-**Backend**:FastAPI(Python REST API framework)
-**Database**:Supabase(PostgreSQL-based backend-as-a-service)
-**Language**:Python 3.8+

### Key Components

1. **`src/db.py`**:Database operations
    -Handles all CRUD operations with Supabase

2. **`src/logic.py`**:Business logic
    -Task validation and processing



## TroubleShooting

## Common Issues

1. **"Module not found" errors**
    -Make sure you've installed all dependencies:`pip install -r requirements.txt`
    -Check that you're running commands from the correct directory

## Future Enhancements

Ideas for extending this project:

- **User Authentication and Role Management**:
Add login/signup functionality with different user roles (e.g., admin, cashier, inventory manager) to control access and permissions within the system.

- **Product Categorization and Search**:
Organize products into categories and subcategories with search and filter options to help users find items quickly.

- **Real-Time Stock Alerts**;
Implement notifications (email/SMS/app alerts) for low stock or expired products to prevent shortages and losses.

- **Database Integration and Persistence**:
Integrate a robust database (e.g., PostgreSQL, SQLite) to persist all product and sales data across sessions, supporting larger inventories and historical sales data.

- **Sales Reports and Analytics**:
Generate detailed sales reports and analytics (daily, weekly, monthly) including trends, best-selling products, and revenue forecasts to aid business decisions.

- **Supplier Management**:
Add modules to manage supplier information, purchase orders, and deliveries to streamline inventory replenishment.

- **Multi-Store Support**:
Extend the system to manage multiple store locations with consolidated reporting.

- **Graphical User Interface (GUI)**:
Develop a desktop or web-based GUI for improved usability compared to the command-line interface.

- **Mobile Application**:
Build a mobile app for on-the-go inventory management and sales tracking.

- **Barcode Scanning Integration**:
Integrate barcode scanning to speed up product entry, stock updates, and sales processing.

- **Backup and Restore**:
Implement automatic backup and easy data restore options to secure data against loss.

- **Promotions and Discounts Management**:
Add functionality to create discounts, offers, and loyalty programs for customers.

- **Multi-Currency and Tax Handling**:
Support multiple currencies and automatic tax calculations based on location.


## Suppport

If you encounter any issues or have questions:
Mail id:chunduruniveditha6@gmail.com
Phone:7989836115
