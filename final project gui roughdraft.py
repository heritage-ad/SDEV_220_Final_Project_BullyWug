import tkinter as tk
from tkinter import ttk

class InventoryManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Bullywug Group Inventory Management System")
        
        # Create a Notebook (Tabbed Interface)
        self.notebook = ttk.Notebook(root)
        
        # Inventory Management Tab
        self.inventory_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.inventory_tab, text='Inventory Management')
        self.create_inventory_tab()
        
        # Sales Tracking Tab
        self.sales_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.sales_tab, text='Sales Tracking')
        self.create_sales_tab()
        
        # Restocking Management Tab
        self.restocking_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.restocking_tab, text='Restocking Management')
        self.create_restocking_tab()
        
        # Reporting Tab
        self.reporting_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.reporting_tab, text='Reporting')
        self.create_reporting_tab()
        
        self.notebook.pack(expand=True, fill='both')
    
    def create_inventory_tab(self):
        # Example: Add Product Form
        add_product_label = ttk.Label(self.inventory_tab, text="Add Product:")
        add_product_label.grid(row=0, column=0, padx=10, pady=(20, 5), sticky='w')
        
        self.product_name_label = ttk.Label(self.inventory_tab, text="Product Name:")
        self.product_name_label.grid(row=1, column=0, padx=10, pady=5, sticky='w')
        
        self.product_name_entry = ttk.Entry(self.inventory_tab, width=30)
        self.product_name_entry.grid(row=1, column=1, padx=10, pady=5)
        
        self.product_description_label = ttk.Label(self.inventory_tab, text="Description:")
        self.product_description_label.grid(row=2, column=0, padx=10, pady=5, sticky='w')
        
        self.product_description_entry = ttk.Entry(self.inventory_tab, width=30)
        self.product_description_entry.grid(row=2, column=1, padx=10, pady=5)
        
        self.product_quantity_label = ttk.Label(self.inventory_tab, text="Quantity:")
        self.product_quantity_label.grid(row=3, column=0, padx=10, pady=5, sticky='w')
        
        self.product_quantity_entry = ttk.Entry(self.inventory_tab, width=10)
        self.product_quantity_entry.grid(row=3, column=1, padx=10, pady=5)
        
        self.product_cost_label = ttk.Label(self.inventory_tab, text="Cost Price:")
        self.product_cost_label.grid(row=4, column=0, padx=10, pady=5, sticky='w')
        
        self.product_cost_entry = ttk.Entry(self.inventory_tab, width=10)
        self.product_cost_entry.grid(row=4, column=1, padx=10, pady=5)
        
        add_button = ttk.Button(self.inventory_tab, text="Add Product", command=self.add_product)
        add_button.grid(row=5, column=1, padx=10, pady=10)
        
        # Example: Product Table/Grid (Replace with a real table/grid widget for displaying products)
        products_frame = ttk.Frame(self.inventory_tab)
        products_frame.grid(row=6, column=0, columnspan=2, padx=10, pady=10, sticky='nsew')
        
        self.products_tree = ttk.Treeview(products_frame, columns=("Name", "Description", "Quantity", "Cost Price"))
        self.products_tree.heading("#0", text="ID")
        self.products_tree.heading("Name", text="Name")
        self.products_tree.heading("Description", text="Description")
        self.products_tree.heading("Quantity", text="Quantity")
        self.products_tree.heading("Cost Price", text="Cost Price")
        
        self.products_tree.column("#0", width=50)
        self.products_tree.column("Name", width=150)
        self.products_tree.column("Description", width=200)
        self.products_tree.column("Quantity", width=100)
        self.products_tree.column("Cost Price", width=100)
        
        self.products_tree.grid(row=0, column=0, sticky='nsew')
        
        # Example data (replace with your actual data management logic)
        self.products_tree.insert("", "end", text="1", values=("Product A", "Description A", "10", "$50"))
        self.products_tree.insert("", "end", text="2", values=("Product B", "Description B", "5", "$30"))
        self.products_tree.insert("", "end", text="3", values=("Product C", "Description C", "15", "$20"))
        
        products_frame.grid_rowconfigure(0, weight=1)
        products_frame.grid_columnconfigure(0, weight=1)
    
    def add_product(self):
        # Get values from entry fields
        name = self.product_name_entry.get()
        description = self.product_description_entry.get()
        quantity = self.product_quantity_entry.get()
        cost_price = self.product_cost_entry.get()
        
        # Insert new row in the Treeview
        self.products_tree.insert("", "end", text="4", values=(name, description, quantity, cost_price))
        
        # Clear entry fields after adding product
        self.product_name_entry.delete(0, tk.END)
        self.product_description_entry.delete(0, tk.END)
        self.product_quantity_entry.delete(0, tk.END)
        self.product_cost_entry.delete(0, tk.END)
    
    def create_sales_tab(self):
        # Placeholder for Sales Tracking Tab
        label = ttk.Label(self.sales_tab, text="Sales Tracking Tab")
        label.pack(padx=10, pady=10)
        
        # Example: Record Sale Form
        record_sale_label = ttk.Label(self.sales_tab, text="Record Sale:")
        record_sale_label.pack(padx=10, pady=(20, 5), anchor='w')
        
        # Example: Sales History Table/Grid
        # Replace with a real table/grid widget for displaying sales history
    
    def create_restocking_tab(self):
        # Placeholder for Restocking Management Tab
        label = ttk.Label(self.restocking_tab, text="Restocking Management Tab")
        label.pack(padx=10, pady=10)
        
        # Example: Create Restocking Order Form
        restock_order_label = ttk.Label(self.restocking_tab, text="Create Restocking Order:")
        restock_order_label.pack(padx=10, pady=(20, 5), anchor='w')
        
        # Example: Order Status Table/Grid
        # Replace with a real table/grid widget for displaying order status
    
    def create_reporting_tab(self):
        # Placeholder for Reporting Tab
        label = ttk.Label(self.reporting_tab, text="Reporting Tab")
        label.pack(padx=10, pady=10)
        
        # Example: Select Report Type Dropdown
        report_type_label = ttk.Label(self.reporting_tab, text="Select Report Type:")
        report_type_label.pack(padx=10, pady=(20, 5), anchor='w')
        
        # Example: Date Range Selector
        date_range_label = ttk.Label(self.reporting_tab, text="Select Date Range:")
        date_range_label.pack(padx=10, pady=(10, 5), anchor='w')
        
        # Example: Report Display Area
        # Replace with a real display area for generated reports
    
def main():
    root = tk.Tk()
    app = InventoryManagementApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
