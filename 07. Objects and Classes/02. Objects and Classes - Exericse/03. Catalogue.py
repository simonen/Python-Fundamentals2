class Catalogue:
    def __init__(self, name: str):
        self.name = name
        self.products = []

    def add_product(self, product_name: str):
        self.products.append(product_name)

    def get_by_letter(self, first_letter: str):
        sorted_list = [x for x in self.products if x[0] == first_letter]
        return sorted_list

    def __repr__(self):
        joined = '\n'.join(sorted(self.products))
        return f"Items in the {self.name} catalogue:\n{joined}"


catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)
