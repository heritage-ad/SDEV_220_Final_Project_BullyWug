#This is the product class that handle details about each product. 
#It will implement methods for adding, updating, and displaying product details.


class Product:
    def __init__(self, product_id, name, description, price, stock, category):
        self.product_id = product_id
        self.name = name
        self.description = description
        self.price = price
        self.stock = stock
        self.category = category

    def update_stock(self, quantity) :
        """Update the stock level of the product."""
        self.stock += quantity
        return self.stock
    
    def set_price(self, new_price):
        """Update the price of the product."""
        self.price = new_price

    def is_low_stock(self, threshold):
        """Check if the stock level is below the given threshold."""
        return self.stock < threshold
    
    def __str__(self):
        """Return a string representation of the product."""
        return (f"Product ID: {self.product_id}\n"
                f"Name: {self.name}\n"
                f"Description: {self.description}\n"
                f"Price: ${self.price:.2f}\n"
                f"Stock: {self.stock}\n"
                f"Category: {self.category}\n")