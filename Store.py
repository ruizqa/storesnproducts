from Product import Product

class Store:
    def __init__(self,name):
        self.name = name
        self.products = {}
    def add_product(self,new_product=Product):
        self.products[str(new_product.id)] = new_product
        return self
    def sell_product(self,id):
        del self.products[str(id)]
        return self
    def inflation(self,percent_increase):
        for id in self.products:
            self.products[id].update_price(percent_increase, is_increased =True)
        return self
    def set_clearance(self,category,percent_discount):
        for id in self.products:
            if self.products[id].category == category:
                self.products[id].update_price(percent_discount,is_increased=False)
        return self
