from typing import Dict, List

class Product:
    def __init__(self, id: int, name: str, description: str, price: float, initial_stock: int, category: str):
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.stock = initial_stock
        self.category = category

    def __repr__(self):
        return f"Product({self.id}, {self.name}, {self.description}, {self.price}, {self.stock}, {self.category})"

class Sale:
    def __init__(self, product: Product, quantity: int):
        self.product = product
        self.quantity = quantity

class InventoryManager:
    def __init__(self):
        self.products: Dict[int, Product] = {}  # Dictionary to map product IDs to Product objects
        self.categories: Dict[str, List[Product]] = {}  # Dictionary to categorize products by category

    def add_product(self, product: Product):
        if product.id in self.products:
            print(f"Product with ID {product.id} already exists.")
            return False
        
        self.products[product.id] = product
        self.categories.setdefault(product.category, []).append(product)
        return True

    def remove_product(self, product_id: int):
        product = self.products.pop(product_id, None)
        if product:
            self.categories[product.category].remove(product)
            if not self.categories[product.category]:
                del self.categories[product.category]
            return True
        else:
            print(f"Product with ID {product_id} does not exist.")
            return False

    def update_product_stock(self, product_id: int, new_stock: int):
        product = self.products.get(product_id)
        if product:
            product.stock = new_stock
            return True
        else:
            print(f"Product with ID {product_id} does not exist.")
            return False

    def list_products(self):
        if not self.products:
            print("No products in inventory.")
            return
        
        for product in self.products.values():
            print(product)

    def list_products_by_category(self, category: str):
        products_in_category = self.categories.get(category)
        if products_in_category:
            for product in products_in_category:
                print(product)
        else:
            print(f"No products found in category: {category}")

# Example usage:

product1 = Product(1, "Latte", "A delicious hot coffee drink", 5.50, 100, "Beverages")
product2 = Product(2, "Cappuccino", "A rich and creamy coffee drink", 6.50, 150, "Beverages")
product3 = Product(3, "Chocolate Croissant", "A flaky and buttery pastry with chocolate", 3.50, 55, "Snacks")

inventory_manager = InventoryManager()

# Adding products to inventory
inventory_manager.add_product(product1)
inventory_manager.add_product(product2)
inventory_manager.add_product(product3)

# Listing all products
print("All Products:")
inventory_manager.list_products()

# Listing products by category
print("\nSnacks:")
inventory_manager.list_products_by_category("Snacks")

# Removing a product
inventory_manager.remove_product(2)

# Updating stock of a product
inventory_manager.update_product_stock(1, 120)

# Listing all products after modifications
print("\nAll Products after modifications:")
inventory_manager.list_products()
