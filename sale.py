import csv
import os
from datetime import datetime


class Product:

    def __init__(self,
                 product_id,
                 name,
                 description,
                 price,
                 stock,
                 category,
                 max_stock=300):
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


def load_products():
    return [
        Product(1, "Latte", "A delicious hot coffee drink", 5.50, 100,
                "Beverages"),
        Product(2, "Cake pop", "A delicious cake styled lollipop", 3.00, 80,
                "Snacks"),
        Product(3, "Cappuccino", "A rich and creamy coffee drink", 6.50, 150,
                "Beverages"),
        Product(4, "Espresso", "A strong and bold coffee shot", 4.50, 245,
                "Beverages"),
        Product(5, "Brown Sugar Tea",
                "A delicious shaken brown sugar infused tea", 4.50, 120,
                "Beverages"),
        Product(6, "Butter Croissant", "A flaky and buttery pastry", 2.50, 60,
                "Snacks"),
        Product(7, "Ham and Cheese Croissant",
                "A flaky and buttery pastry with ham and cheese", 3.75, 55,
                "Snacks"),
        Product(8, "Chocolate Croissant",
                "A flaky and buttery pastry with chocolate", 3.50, 55,
                "Snacks"),
        Product(9, "Blueberry Muffin",
                "A soft and moist baked good dazzled with blueberries", 3.00,
                70, "Snacks"),
        Product(10, "French Toast Muffin",
                "A soft and moist baked good with cinnamon", 3.00, 70,
                "Snacks"),
        Product(11, "Creme Brulee Muffin",
                "A soft and moist baked good with toasted sugar", 3.00, 70,
                "Snacks"),
        Product(12, "Iced Americano", "A strong and bold coffee with ice",
                5.00, 245, "Beverages"),
        Product(13, "Caramel Frappe",
                "A delicious blended caramel caffeinated drink", 5.00, 200,
                "Beverages"),
        Product(14, "Mango Pineapple Smoothie",
                "A healthy blend of mangos and pineapple deliciousness", 6.50,
                100, "Beverages"),
        Product(15, "Iced Tea", "A simple delicious tea", 3.50, 300,
                "Beverages"),
        Product(16, "Hot Chocolate", "A taste of Grandma's chocolate drink",
                3.50, 245, "Beverages"),
        Product(
            17, "Iced Chai",
            "A delicious blend of tea, cinnamon, and other warming spices",
            5.00, 240, "Beverages"),
        Product(18, "Cold Brew", "A stronger and bolder coffee drink", 5.00,
                230, "Beverages"),
        Product(19, "Macchiato", "A delicious espresso with steamed milk",
                5.50, 120, "Beverages"),
        Product(20, "Mocha", "A delicious chocolate drink", 5.50, 250,
                "Beverages"),
        Product(21, "Cookies", "A fresh baked oeey gooey sweetness", 2.00, 300,
                "Snacks"),
        Product(22, "Brownies", "A fresh baked fudgy dessert bar", 2.50, 250,
                "Snacks"),
        Product(23, "Cupcakes", "A fresh baked moist cake", 3.75, 250,
                "Snacks"),
        Product(24, "Bagels", "A fresh, delicious, soft baked good", 4.00, 200,
                "Snacks"),
        Product(25, "Cream Cheese", "The perfect spread", 1.50, 400, "Snacks"),
        Product(26, "Turkey Sandwich",
                "Homemade croissant with turkey and cheese", 4.50, 200,
                "Snacks"),
        Product(27, "Veggie Sandwich", "Homemade croissant with veggies", 4.50,
                100, "Snacks"),
        Product(28, "Quiche", "A delicious freshly baked pie", 3.50, 75,
                "Snacks"),
        Product(29, "Yogurt", "Sourced from the local farm", 3.00, 100,
                "Snacks"),
        Product(30, "Fruit", "Freshly sourced from the local farm", 2.50, 240,
                "Snacks"),
    ]


def make_sale(products, sales_manager):
    sale_items = []
    total_amount = 0

    while True:
        print("\nAvailable Products:")
        for i, product in enumerate(products, 1):
            print(f"{i}. {product.name} - ${product.price:.2f}")

        try:
            product_index = int(
                input("Enter the product number (0 to finish): ")) - 1

            if product_index == -1:
                if not sale_items:
                    print("No items found...")
                    return
                break

            if 0 <= product_index < len(products):
                quantity = int(input("Enter the quantity: "))
                if quantity <= 0:
                    print("Error - enter a valid number")
                    continue

                product = products[product_index]
                if product.stock >= quantity:
                    sale_item = Sale(product, quantity)
                    sale_items.append(sale_item)
                    total_amount += sale_item.total_amount
                    print(f"Added {quantity} {product.name}(s) to the sale.")
                else:
                    print(
                        f"Error - Insufficient stock for {product.name}. Available: {product.stock}"
                    )
            else:
                print("Error - enter a valid number")
        except ValueError:
            print("Error - enter a valid number")

    # Complete the sale
    print("\nSale Summary:")
    for item in sale_items:
        print(
            f"{item.product.name}: {item.quantity} x ${item.product.price:.2f} = ${item.total_amount:.2f}"
        )
    print(f"Total Amount: ${total_amount:.2f}")

    confirm = input("Confirm sale? (y/n): ").lower()
    if confirm == 'y':
        for item in sale_items:
            sales_manager.add_sale(item)
        print("Sale completed.")
    else:
        print("Sale cancelled.")


def restock_products(products):
    print("\nProducts Not at Maximum Stock:")
    print("=" * 30)
    restock_options = []
    for i, product in enumerate(products, 1):
        if product.stock < product.max_stock:
            print(
                f"{i}. {product.name} - Current Stock: {product.stock}/{product.max_stock}"
            )
            restock_options.append(product)

    if not restock_options:
        print("All products are at maximum stock!")
        return

    while True:
        try:
            choice = int(
                input(
                    "\nEnter the number of the product you want to restock or 0 exit: "
                )) - 1
            if choice == -1:
                print("exiting...")
                return
            if 0 <= choice < len(restock_options):
                product = restock_options[choice]
                max_restock = product.max_stock - product.stock
                restock_amount = int(
                    input(
                        f"Enter the amount to restock for {product.name} (max {max_restock}): "
                    ))
                if 0 < restock_amount <= max_restock:
                    new_stock = product.update_stock(restock_amount)
                    print(
                        f"{product.name} restocked. New stock level: {new_stock}"
                    )
                    break
                else:
                    print(
                        f"Please enter a number between 1 and {max_restock}.")
            else:
                print("Error - enter a valid number")
        except ValueError:
            print("Error - enter a valid number")


def main():
    products = load_products()
    sales_manager = SalesManager()

    while True:
        print("\nCoffee Shop Inventory Management System")
        print("1. Make a sale")
        print("2. View inventory")
        print("3. Generate sales report")
        print("4. Check low stock")
        print("5. View best-selling products")
        print("6. View category performance")
        print("7. Restock products")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ")

        if choice == '1':
            make_sale(products, sales_manager)
        elif choice == '2':
            sales_manager.generate_inventory_report(products)
        elif choice == '3':
            sales_manager.generate_sales_report()
        elif choice == '4':
            try:
                threshold = int(
                    input("Enter the reorder point for products: "))
                sales_manager.identify_low_stock(products, threshold)
            except ValueError:
                print("Error - enter a valid number")
        elif choice == '5':
            sales_manager.best_selling_products()
        elif choice == '6':
            sales_manager.category_performance()
        elif choice == '7':
            restock_products(products)
        elif choice == '8':
            print(
                "Thank you for using the Coffee Shop Inventory Management System!"
            )
            break
        else:
            print("Error - enter a valid number")


if __name__ == "__main__":
    main()
