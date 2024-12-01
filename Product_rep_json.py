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
