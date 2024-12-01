import yaml
import json
from decimal import Decimal
from typing import List
from Product import Product
from ProductRepository import ProductRepository

class ProductRepYaml(ProductRepository):
    def __init__(self, filename: str):
        super().__init__()
        self.filename = filename
        self.products = self._read_all()

    def _read_all(self) -> List[Product]:
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                data = yaml.safe_load(file)
                return [Product.create_from_json(json.dumps(product)) for product in data]
        except FileNotFoundError:
            return []

    def _write_all(self):
        with open(self.filename, 'w', encoding='utf-8') as file:
            yaml.dump([json.loads(product.to_json()) for product in self.products], file, allow_unicode=True, default_flow_style=False)