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
    

if __name__ == "__main__":
        #Products
        products = [
             Product(1,"Latte", "A delicious hot coffee drink", 5.50, 100, "Beverages" ),
             Product(2, "Cake pop", "A delicious cake styled lollipop", 3.00, 80, "Snacks"),
             Product(3, "Cappuccino", "A rich and creamy coffee drink", 6.50, 150, "Beverages" ),
             Product(4, "Espresso", "A strong and bold coffee shot", 4.50, 245, "Beverages" ),
             Product(5, "Brown Sugar Tea", "A delicious shaken brown sugar infused tea", 4.50, 120, "Beverages" ),
             Product(6, "Butter Croissant", "A flaky and buttery pastry", 2.50, 60, "Snacks"),
             Product(7, "Ham and Cheese Croissant", "A flaky and buttery pastry with ham and cheese", 3.75, 55, "Snacks" ),
             Product(8, "Chocolate Croissant", "A flaky and buttery pastry with chocolate", 3.50, 55, "Snacks"),
             Product(9, "Bluberry Muffin", "A soft and moist baked good dazzled with blueberries", 3.00, 70, "Snacks"),
             Product(10, "French Toast Muffin", "A soft and moist baked good with cinammon", 3.00, 70, "Snacks" ),
             Product(11, "Creme Brulee Muffin", "A soft and moist baked good with toasted sugar", 3.00, 70, "Snacks"),
             Product(12, "Iced Americano", "A strong and bold coffee with ice", 5.00, 245, "Beverages"),
             Product(13, "Caramel Frappe", "A delicious blended caramel caffeinated drink", 5.00, 200, "Beverages"),
             Product(14, "Mango Pineapple Smoothie", "A healthy blend of mangos and pineapple deliciousness", 6.50, 100, "Beverages"),
             Product(15, "Iced Tea", "A simple delicious tea", 3.50, 300, "Beverages"),
             Product(16, "Hot Chocolate", "A taste of Grandma's chocolate drink", 3.50, 245, "Beverages"),
             Product(17, "Iced Chai", "A delicious blend of tea, cinnamon, and other warming spices", 5.00, 240, "Beverages"),
             Product(18, "Cold Brew", "A stronger and bolder coffee drink", 5.00, 230, "Beverages"),
             Product(19, "Macchiato", "A delicious espresso with steamed milk", 5.50, 120, "Beverages"),
             Product(20, "Mocha", "A delicious chocolate drink", 5.50, 250, "Beverages"), 
             Product(21, "Cookies", "A fresh baked oeey gooey sweetness", 2.00, 300, "Snacks"),
             Product(22, "Brownnies", "A fresh baked fudgy dessert bar", 2.50, 250, "Snacks" ),
             Product(23, "Cupcakes", "A fresh baked moist cake", 3.75, 250, "Snacks" ),
             Product(24, "Bagels", "A fresh, delicious, soft baked good", 4.00, 200, "Snacks" ),
             Product(25, "Cream Cheese", "The perfect spread", 1.50, 400, "Snacks" ),
             Product(26, "Turkey Sandwich", "Homemade croissant with turkey and cheese", 4.50, 200, "Snacks" ),
             Product(27, "Veggie Sandwich", "Homemade croissant with veggies", 4.50, 100, "Snacks" ),
             Product(28, "Quiche", "A delicious freshly baked pie", 3.50, 75, "Snacks"),
             Product(29, "Yogurt", "Sourced from the local farm", 3.00, 100, "Snacks"),
             Product(30, "Fruit", "Freshly sourced from the local farm", 2.50, 240, "Snacks"),

        ]
        
        #printing details of products
        for product in products:
             print(product)
             print("_" * 30)

        #updating stock & price
        products[17].update_stock(20) #adding 20 more to product 18
        products[20].set_price(2.50) #updating the price of product 21


        #print updated details
        print("\nAfter Updates:")
        for product in products: 
             print(product)
             print("_" * 30)


        #checking for low stock
        threshold = 50
        for product in products: 
             if product.is_low_stock(threshold):
                  print(f"Stock is low for {product.name}. Current stock: {product.stock}")


             
    




    
    




    
