class Product_3:
    def __init__(self, price):
        self.price = price # We change the constructor from "self.price = price" to the set price function

    @property # here we apply the proprety decorator to this method. And renaming the method to the ideal name, in this case price
    def price(self): 
        return self.__price
    
    @price.setter  # Here we also have to add a decorater. The name of the decorater starts with the name of the proprety "price" and the .setter
    def price(self, value): 
        if value < 0:
            raise ValueError("Price can not be negative")
        else:
            self.__price = value


product = Product_3(50)
print(product.price)
product.price = 10 # If we try to set the price to -1 we wiil raise an execption
print(product.price)