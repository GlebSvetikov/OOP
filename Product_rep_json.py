import json
from decimal import Decimal
from typing import List, Optional, Any
from Product import Product

class ProductRepJson:
    def __init__(self, filename: str):
        self.filename = filename
        self.products = self._read_all()

    def _read_all(self) -> List[Product]:
        try:
            with open(self.filename, 'r', encoding='cp1251') as file:
                data = json.load(file)
                return [Product.create_from_json(json.dumps(product)) for product in data]
        except FileNotFoundError:
            return []
            
    def _write_all(self):
        with open(self.filename, 'w', encoding='cp1251') as file:
            json.dump([json.loads(product.to_json()) for product in self.products], file, ensure_ascii=False, indent=4)

   def get_by_id(self, product_id: int) -> Optional[Product]:
        for product in self.products:
            if product.product_id == product_id:
                return product
        return None

    def get_k_n_short_list(self, k: int, n: int) -> List[Product]:
        start_index = k * n
        end_index = start_index + n
        return self.products[start_index:end_index]

    def sort_by_field(self, field_name: str):
        self.products.sort(key=lambda x: getattr(x, field_name))

    def add_product(self, product: Product):
        max_id = max((p.product_id for p in self.products if p.product_id is not None), default=0)
        product.product_id = max_id + 1
        self.products.append(product)
        self._write_all()

    def replace_product_by_id(self, product_id: int, new_product: Product):
        for i, product in enumerate(self.products):
            if product.product_id == product_id:
                self.products[i] = new_product
                new_product.product_id = product_id
                self._write_all()
                return
        raise ValueError(f"Product with ID {product_id} not found.")

    def delete_product_by_id(self, product_id: int):
        self.products = [product for product in self.products if product.product_id != product_id]
        self._write_all()

    def get_count(self) -> int:
        return len(self.products)
