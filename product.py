class Product:
    def __init__(self, model, final_price, specs):
        self.model = model
        self.final_price = final_price
        self.specs = specs
        
    def to_string(self):
        return "\n" + self.model + " " + self.final_price + "\n\n" + self.specs + "\n=============================================================="
