import tkinter as tk
from tkinter import ttk
from Product import Product
from sale import Sale, SalesManager

class InventoryManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Bullywug Group Inventory Management System")
        
        self.inventory = []
        self.sales_manager = SalesManager()
        self.product_id_counter = 1
        
        self.notebook = ttk.Notebook(root)
        
        self.inventory_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.inventory_tab, text='Inventory Management')
        self.create_inventory_tab()
        
        self.sales_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.sales_tab, text='Sales Tracking')
        self.create_sales_tab()
        
        self.restocking_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.restocking_tab, text='Restocking Management')
        self.create_restocking_tab()
        
        self.reporting_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.reporting_tab, text='Reporting')
        self.create_reporting_tab()
        
        self.notebook.pack(expand=True, fill='both')
    
    def create_inventory_tab(self):
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
        
        products_frame.grid_rowconfigure(0, weight=1)
        products_frame.grid_columnconfigure(0, weight=1)
    
    def add_product(self):
        name = self.product_name_entry.get()
        description = self.product_description_entry.get()
        quantity = int(self.product_quantity_entry.get())
        cost_price = float(self.product_cost_entry.get())
        category = "Uncategorized"  
        
        new_product = Product(self.product_id_counter, name, description, cost_price, quantity, category)
        self.inventory.append(new_product)
        
        self.products_tree.insert("", "end", text=self.product_id_counter, values=(name, description, quantity, cost_price))
        self.product_id_counter += 1
        
        self.product_name_entry.delete(0, tk.END)
        self.product_description_entry.delete(0, tk.END)
        self.product_quantity_entry.delete(0, tk.END)
        self.product_cost_entry.delete(0, tk.END)
    
    def create_sales_tab(self):
        label = ttk.Label(self.sales_tab, text="Sales Tracking Tab")
        label.pack(padx=10, pady=10)
        
        record_sale_label = ttk.Label(self.sales_tab, text="Record Sale:")
        record_sale_label.pack(padx=10, pady=(20, 5), anchor='w')
        
        self.sale_product_id_label = ttk.Label(self.sales_tab, text="Product ID:")
        self.sale_product_id_label.pack(padx=10, pady=5, anchor='w')
        
        self.sale_product_id_entry = ttk.Entry(self.sales_tab, width=10)
        self.sale_product_id_entry.pack(padx=10, pady=5)
        
        self.sale_quantity_label = ttk.Label(self.sales_tab, text="Quantity:")
        self.sale_quantity_label.pack(padx=10, pady=5, anchor='w')
        
        self.sale_quantity_entry = ttk.Entry(self.sales_tab, width=10)
        self.sale_quantity_entry.pack(padx=10, pady=5)
        
        record_button = ttk.Button(self.sales_tab, text="Record Sale", command=self.record_sale)
        record_button.pack(padx=10, pady=10)
    
    def record_sale(self):
        product_id = int(self.sale_product_id_entry.get())
        quantity = int(self.sale_quantity_entry.get())
        
        product = next((p for p in self.inventory if p.product_id == product_id), None)
        if product:
            sale = Sale(product, quantity)
            self.sales_manager.add_sale(sale)
            product.update_stock(-quantity)
            
            for item in self.products_tree.get_children():
                item_values = self.products_tree.item(item, "values")
                if int(self.products_tree.item(item, "text")) == product_id:
                    self.products_tree.item(item, values=(item_values[0], item_values[1], product.stock, item_values[3]))
                    break
    
    def create_restocking_tab(self):
        label = ttk.Label(self.restocking_tab, text="Restocking Management Tab")
        label.pack(padx=10, pady=10)
        
        restock_label = ttk.Label(self.restocking_tab, text="Restock Product:")
        restock_label.pack(padx=10, pady=(20, 5), anchor='w')
        
        self.restock_product_id_label = ttk.Label(self.restocking_tab, text="Product ID:")
        self.restock_product_id_label.pack(padx=10, pady=5, anchor='w')
        
        self.restock_product_id_entry = ttk.Entry(self.restocking_tab, width=10)
        self.restock_product_id_entry.pack(padx=10, pady=5)
        
        self.restock_quantity_label = ttk.Label(self.restocking_tab, text="Quantity:")
        self.restock_quantity_label.pack(padx=10, pady=5, anchor='w')
        
        self.restock_quantity_entry = ttk.Entry(self.restocking_tab, width=10)
        self.restock_quantity_entry.pack(padx=10, pady=5)
        
        restock_button = ttk.Button(self.restocking_tab, text="Restock", command=self.restock_product)
        restock_button.pack(padx=10, pady=10)
    
    def restock_product(self):
        product_id = int(self.restock_product_id_entry.get())
        quantity = int(self.restock_quantity_entry.get())
        
        product = next((p for p in self.inventory if p.product_id == product_id), None)
        if product:
            product.update_stock(quantity)
            
            for item in self.products_tree.get_children():
                item_values = self.products_tree.item(item, "values")
                if int(self.products_tree.item(item, "text")) == product_id:
                    self.products_tree.item(item, values=(item_values[0], item_values[1], product.stock, item_values[3]))
                    break
    
    def create_reporting_tab(self):
        label = ttk.Label(self.reporting_tab, text="Reporting Tab")
        label.pack(padx=10, pady=10)
        
        sales_report_button = ttk.Button(self.reporting_tab, text="Generate Sales Report", command=self.generate_sales_report)
        sales_report_button.pack(padx=10, pady=10)
        
        inventory_report_button = ttk.Button(self.reporting_tab, text="Generate Inventory Report", command=self.generate_inventory_report)
        inventory_report_button.pack(padx=10, pady=10)
        
        low_stock_report_button = ttk.Button(self.reporting_tab, text="Generate Low Stock Report", command=self.generate_low_stock_report)
        low_stock_report_button.pack(padx=10, pady=10)
        
        best_selling_button = ttk.Button(self.reporting_tab, text="Best Selling Products", command=self.generate_best_selling_report)
        best_selling_button.pack(padx=10, pady=10)
        
        category_performance_button = ttk.Button(self.reporting_tab, text="Category Performance", command=self.generate_category_performance_report)
        category_performance_button.pack(padx=10, pady=10)
    
    def generate_sales_report(self):
        self.sales_manager.generate_sales_report()
    
    def generate_inventory_report(self):
        self.sales_manager.generate_inventory_report(self.inventory)
    
    def generate_low_stock_report(self):
        threshold = 50  
        self.sales_manager.identify_low_stock(self.inventory, threshold)
    
    def generate_best_selling_report(self):
        top_n = 5 
        self.sales_manager.best_selling_products(top_n)
    
    def generate_category_performance_report(self):
        self.sales_manager.category_performance()

if __name__ == "__main__":
    root = tk.Tk()
    app = InventoryManagementApp(root)
    root.mainloop()
