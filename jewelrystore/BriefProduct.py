from decimal import Decimal
from .IProduct import IProduct
from .ProductValidator import ProductValidator


class BriefProduct(IProduct):
    def __init__(self, product_id: int, name: str, price: Decimal):
        self._product_id = 0
        self._name = ""
        self._price = Decimal('0')

        self.set_product_id(product_id)
        self.set_name(name)
        self.set_price(price)

    # Properties для доступа к приватным атрибутам
    @property
    def product_id(self) -> int:
        return self._product_id

    @property
    def name(self) -> str:
        return self._name

    @property
    def price(self) -> Decimal:
        return self._price

    def get_product_id(self) -> int:
        return self._product_id

    def set_product_id(self, product_id: int) -> None:
        ProductValidator.validate_product_id(product_id)
        self._product_id = product_id

    def get_name(self) -> str:
        return self._name

    def set_name(self, name: str) -> None:
        ProductValidator.validate_name(name)
        self._name = name

    def get_price(self) -> Decimal:
        return self._price

    def set_price(self, price: Decimal) -> None:
        ProductValidator.validate_price(price)
        self._price = price

    def __eq__(self, other):
        if not isinstance(other, BriefProduct):
            return False
        return (self._product_id == other._product_id and
                self._name == other._name and
                self._price == other._price)

    def __hash__(self):
        return hash((self._product_id, self._name, self._price))

    def __str__(self):
        return f"BriefProduct(product_id={self._product_id}, name='{self._name}', price={self._price})"
