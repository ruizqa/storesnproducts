class Product:
    id=1
    def __init__(self,name,price,category):
        self.name = name
        self.price = price
        self.category = category
        self.id = Product.id
        Product.id +=1
    def update_price(self, percent_change, is_increased):
        if is_increased:
            self.price = self.price * (1+percent_change/100)
        else:
            self.price = self.price * (1-percent_change/100)
        return self
    def print_info(self):
        print(f"Product: {self.name} \nCategory: {self.category} \nPrice: {self.price}")
    
