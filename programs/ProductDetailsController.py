from ProductDetailsWindow import ProductDetailsWindow
from Product import Product

class ProductDetailsController:
    def __init__(self, view: ProductDetailsWindow, product: Product):
        self.view = view
        self.product = product
        self.display_product()

    def display_product(self):
        """Отображение информации о продукте"""
        self.view.display_product(self.product)