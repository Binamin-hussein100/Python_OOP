# OOP 

# products

# class
# attributes
# methods
# instance
# decorators @

def log_transaction(func):
    def wrapper(*args, **kwargs):
        print(f"Log:Running {func.__name__} method")
        results = func(*args, **kwargs)
        print(f"Log:Completed {func.__name__} method")
        return results
    return wrapper

class Product:
    def __init__(self, name="product", price=100, quantity=10):
        self.name = name
        self.price = price
        self._quantity = quantity

    @property
    def stock(self):
        return self._quantity

    # sell
    @log_transaction
    def sell(self, amount):
        if amount > self._quantity:
            print(f"Insufficient stock. Only {self._quantity} available.")
            
            return 0
        self._quantity -= amount
        total_price = amount * self.price
        print(f'{self.name} sold: {amount} units for ${total_price}')
        print(f"(test):Log: Running restock method {self.name}")
        return total_price
    
    @log_transaction
    def restock(self, amount):
        self._quantity += amount
        print(f"{self.name} has been restocked. New quantity = {self._quantity}")


class DiscountProduct(Product):
        def __init__(self, name, price, quantity, discount):
            super().__init__(name, price,quantity)
            self.discount = discount

        @log_transaction
        def sell(self,amount):
            if amount > self._quantity:
                print(f"Insufficient stock. Only {self._quantity} available.")
                return 0
            discount_price = self.price * (1 - self.discount) 
            self._quantity -= amount

            total_price = amount * discount_price
            print(f"{self.name} sold with discount: {amount} units for ${total_price}")
            
            return total_price

        def show_discount(self):
            print(f"{self.name} has a {self.discount * 100}% discount")



# instances

product1 = Product("Arial", 100,100)
product2 = DiscountProduct("Arial", 100, 100, 0.15)

print(product1.sell(10))
print("---------------------------")
print(product2.sell(10))

