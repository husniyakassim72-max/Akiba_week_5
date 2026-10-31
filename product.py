class Product:
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity
    def __str__(self):
        return f"the product name is {self.name} the pric is {self.price} and the quantity is {self.quantity}"
p1=Product("Milk",180,"100ml")   
p2=Product("Sweets",250,"80kg")
p3=Product("flour",1000,"15kg")
print(p1.name,p1.price,p1.quantity)
print(p2.name,p2.price,p2.quantity)
print(p3.name,p3.price,p3.quantity)
print(p1)
print(p2)
print (p3)