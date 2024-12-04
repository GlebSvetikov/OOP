from typing import List, Optional
from Product import Product


class ProductRepository:
    def __init__(self, strategy):
        self.strategy = strategy

    def read_all(self) -> List[Product]:
        data = self.strategy.read()
        return [Product.create_from_dict(item) for item in data]

    def write_all(self, products: List[Product]) -> None:
        data = [product.to_dict() for product in products]
        self.strategy.write(data)

    def get_by_id(self, product_id: int) -> Optional[Product]:
        products = self.read_all()
        for product in products:
            if product.product_id == product_id:
                return product
        return None

    def add_product(self, product: Product) -> None:
        products = self.read_all()
        if not Product.is_product_code_unique(product.product_code, products):
            raise ValueError(f"Product with code {product.product_code} already exists.")
        products.append(product)
        self.write_all(products)

    def replace_product_by_id(self, product_id: int, new_product: Product):
        products = self.read_all()
        for i, product in enumerate(products):
            if product.product_id == product_id:
                products[i] = new_product
                new_product.product_id = product_id
                self.write_all(products)
                return
        raise ValueError(f"Продукт с ID {product_id} не найден.")

    def delete_product_by_id(self, product_id: int):
        products = self.read_all()
        products = [product for product in products if product.product_id != product_id]
        self.write_all(products)
