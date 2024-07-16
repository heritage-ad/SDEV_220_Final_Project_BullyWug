import csv
import os
from datetime import datetime

class Product:
    def __init__(self, product_id, name, description, price, stock, category, max_stock=300):
        self.product_id = product_id
        self.name = name
        self.description = description
        self.price = price
        self.stock = stock
        self.category = category
        self.max_stock = max_stock

    def update_stock(self, quantity):
        self.stock += quantity
        if self.stock > self.max_stock:
            self.stock = self.max_stock
        elif self.stock < 0:
            self.stock = 0
        return self.stock

    def set_price(self, new_price):
        self.price = new_price

    def is_low_stock(self, threshold):
        return self.stock < threshold

    def __str__(self):
        return (f"Product ID: {self.product_id}\n"
                f"Name: {self.name}\n"
                f"Description: {self.description}\n"
                f"Price: ${self.price:.2f}\n"
                f"Stock: {self.stock}\n"
                f"Category: {self.category}\n")


class Sale:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity
        self.date = datetime.now()
        self.total_amount = self.calculate_total()

    def calculate_total(self):
        return self.quantity * self.product.price

    def record_sale(self):
        if self.product.stock >= self.quantity:
            self.product.update_stock(-self.quantity)
            self.save_to_csv()
            return True
        return False

    def display_sale(self):
        print(f"Date: {self.date.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Product: {self.product.name}")
        print(f"Quantity: {self.quantity}")
        print(f"Price per unit: ${self.product.price:.2f}")
        print(f"Total amount: ${self.total_amount:.2f}")

    def save_to_csv(self):
        filename = "sales_record.csv"
        file_exists = os.path.isfile(filename)

        with open(filename, 'a', newline='') as file:
            writer = csv.writer(file)
            if not file_exists:
                writer.writerow([
                    'Date', 'Product ID', 'Product Name', 'Quantity', 'Price',
                    'Total'
                ])
            writer.writerow([
                self.date, self.product.product_id, self.product.name,
                self.quantity, self.product.price, self.total_amount
            ])


class SalesManager:
    def __init__(self):
        self.sales = []

    def add_sale(self, sale):
        if sale.record_sale():
            self.sales.append(sale)
            return True
        return False

    def get_total_revenue(self):
        return sum(sale.total_amount for sale in self.sales)

    def get_product_sales(self):
        product_sales = {}
        for sale in self.sales:
            if sale.product.name in product_sales:
                product_sales[sale.product.name] += sale.quantity
            else:
                product_sales[sale.product.name] = sale.quantity
        return product_sales

    def generate_sales_report(self):
        print("Sales Report")
        print("=" * 30)
        print(f"Total Revenue: ${self.get_total_revenue():.2f}")
        print("\nProduct Sales:")
        for product, quantity in self.get_product_sales().items():
            print(f"- {product}: {quantity}")

    def generate_inventory_report(self, products):
        print("\nInventory Report")
        print("=" * 30)
        for product in products:
            print(f"{product.name}: {product.stock} in stock")

    def identify_low_stock(self, products, threshold):
        low_stock = [
            product for product in products if product.is_low_stock(threshold)
        ]
        if low_stock:
            print("\nLow Stock Alert")
            print("=" * 30)
            for product in low_stock:
                print(
                    f"{product.name} is low on stock. Current stock: {product.stock}"
                )
        else:
            print("\nAll products are sufficiently stocked.")

    def best_selling_products(self, top_n=5):
        product_sales = self.get_product_sales()
        sorted_sales = sorted(product_sales.items(),
                              key=lambda x: x[1],
                              reverse=True)
        print(f"\nTop {top_n} Best-Selling Products")
        print("=" * 30)
        for product, quantity in sorted_sales[:top_n]:
            print(f"{product}: {quantity} sold")

    def category_performance(self):
        category_sales = {}
        for sale in self.sales:
            category = sale.product.category
            if category in category_sales:
                category_sales[category] += sale.total_amount
            else:
                category_sales[category] = sale.total_amount

        print("\nCategory Performance")
        print("=" * 30)
        for category, total in category_sales.items():
            print(f"{category}: ${total:.2f}")


class InventoryManager:
    def __init__(self, products):
        self.products = {product.product_id: product for product in products}

    def add_product(self, product):
        if product.product_id not in self.products:
            self.products[product.product_id] = product
            print(f"Product '{product.name}' added to inventory.")
        else:
            print(f"Product with ID {product.product_id} already exists.")

    def remove_product(self, product_id):
        if product_id in self.products:
            del self.products[product_id]
            print(f"Product with ID {product_id} removed from inventory.")
        else:
            print(f"Product with ID {product_id} not found.")

    def update_product(self, product_id, new_product):
        if product_id in self.products:
            self.products[product_id] = new_product
            print(f"Product with ID {product_id} updated.")
        else:
            print(f"Product with ID {product_id} not found.")

    def get_product_by_id(self, product_id):
        return self.products.get(product_id)

    def get_all_products(self):
        return list(self.products.values())


def load_products():
    return [
        Product(1, "Latte", "A delicious hot coffee drink", 5.50, 100, "Beverages"),
        Product(2, "Cake pop", "A delicious cake styled lollipop", 3.00, 80, "Snacks"),
        Product(3, "Cappuccino", "A rich and creamy coffee drink", 6.50, 150, "Beverages"),
        Product(4, "Espresso", "A strong and bold coffee shot", 4.50, 245, "Beverages"),
        Product(5, "Brown Sugar Tea", "A delicious shaken brown sugar infused tea", 4.50, 120, "Beverages"),
        Product(6, "Butter Croissant", "A flaky and buttery pastry", 2.50, 60, "Snacks"),
        Product(7, "Ham and Cheese Croissant", "A flaky and buttery pastry with ham and cheese", 3.75, 55, "Snacks"),
        Product(8, "Chocolate Croissant", "A flaky and buttery pastry with chocolate", 3.50, 55, "Snacks"),
        Product(9, "Blueberry Muffin", "A soft and moist baked good dazzled with blueberries", 3.00, 70, "Snacks"),
        Product(10, "French Toast Muffin", "A soft and moist baked good with cinnamon", 3.00, 70, "Snacks"),
        Product(11, "Creme Brulee Muffin", "A soft and moist baked good with toasted sugar", 3.00, 70, "Snacks"),
        Product(12, "Iced Americano", "A strong and bold coffee with ice", 5.00, 245, "Beverages"),
        Product(13, "Caramel Frappe", "A delicious blended caramel caffeinated drink", 5.00, 200, "Beverages"),
        Product(14, "Mango Pineapple Smoothie", "A healthy blend of mangos and pineapple deliciousness", 6.50, 100, "Beverages"),
        Product(15, "Iced Tea", "A simple delicious tea", 3.50, 300, "Beverages"),
        Product(16, "Hot Chocolate", "A taste of Grandma's chocolate drink", 3.50, 245, "Beverages"),
        Product(17, "Iced Chai", "A delicious blend of tea, cinnamon, and other warming spices", 5.00, 240, "Beverages"),
        Product(18, "Cold Brew", "A stronger and bolder coffee drink", 5.00, 230, "Beverages"),
        Product(19, "Macchiato", "A delicious espresso with steamed milk", 5.50, 120, "Beverages"),
        Product(20, "Mocha", "A delicious chocolate drink", 5.50, 250, "Beverages")
    ]

# Example usage
products = load_products()
inventory_manager = InventoryManager(products)
sales_manager = SalesManager()

# Add a new product
new_product = Product(21, "Vanilla Latte", "A sweet and creamy vanilla latte", 5.50, 100, "Beverages")
inventory_manager.add_product(new_product)

# Make a sale
product_to_sell = inventory_manager.get_product_by_id(1)  # Assuming product ID 1 is "Latte"
sale = Sale(product_to_sell, 3)
sales_manager.add_sale(sale)

# Generate reports
sales_manager.generate_sales_report()
sales_manager.generate_inventory_report(inventory_manager.get_all_products())
sales_manager.identify_low_stock(inventory_manager.get_all_products(), 50)
sales_manager.best_selling_products(5)
sales_manager.category_performance()
