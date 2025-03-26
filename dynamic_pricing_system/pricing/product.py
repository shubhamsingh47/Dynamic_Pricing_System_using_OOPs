class Product:
    def __init__(self, name, base_price, category):
        self.name = name
        self.base_price = base_price
        self.category = category

    def get_price(self):
        return self.base_price