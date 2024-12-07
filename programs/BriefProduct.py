
from decimal import Decimal
from typing import Optional

class BriefProduct:
    def __init__(self, product_id: Optional[int] = None, name: str = "", price: Decimal = Decimal(0), product_code: str = ""):
        self._product_id = product_id
        self._name = name
        self._price = price
        self._product_code = product_code

    @property
    def product_id(self):
        return self._product_id

    @product_id.setter
    def product_id(self, value: Optional[int]):
        if value is not None and (not isinstance(value, int) or value < 0):
            raise ValueError("Product ID must be a non-negative integer or None.")
        self._product_id = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        if not isinstance(value, str) or not value:
            raise ValueError("Name must be a non-empty string.")
        self._name = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value: Decimal):
        if not isinstance(value, Decimal) or value < 0:
            raise ValueError("Price must be a non-negative decimal.")
        self._price = value

    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value: str):
        if not (isinstance(value, str) and value.isdigit() and len(value) == 6):
            raise ValueError("Product code must be a string of 6 digits.")
        self._product_code = value

    def __eq__(self, other):
        if not isinstance(other, BriefProduct):
            return False
        return self.product_code == other.product_code

    def __str__(self):
        return f"Product(name={self.name}, price={self.price}, product_code={self.product_code})"

    def brief(self):
        return f"BriefProduct(product_id={self.product_id}, name={self.name}, price={self.price})"