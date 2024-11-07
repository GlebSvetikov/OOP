from decimal import Decimal
import json
from .BriefProduct import BriefProduct
from .ProductValidator import ProductValidator


class Product(BriefProduct):
    def __init__(self, product_id: int, name: str, price: Decimal, description: str,
                 stock_quantity: int, material: str):
        super().__init__(product_id, name, price)
        self._description = description
        self._stock_quantity = stock_quantity
        self._material = material
        ProductValidator.validate_product(self)

    @property
    def description(self) -> str:
        return self._description

    @property
    def stock_quantity(self) -> int:
        return self._stock_quantity

    @property
    def material(self) -> str:
        return self._material

    @classmethod
    def create_new_product(cls, name: str, description: str, price: Decimal,
                           stock_quantity: int, material: str) -> 'Product':
        return cls(0, name, price, description, stock_quantity, material)

    @classmethod
    def update_existing_product(cls, product_id: int, name: str, description: str,
                                price: Decimal, stock_quantity: int, material: str) -> 'Product':
        return cls(product_id, name, price, description, stock_quantity, material)

    @classmethod
    def create_from_string(cls, product_string: str) -> 'Product':
        parts = product_string.split(',')
        if len(parts) != 6:
            raise ValueError("Invalid product string format. Expected 6 comma-separated values.")
        try:
            return cls(
                product_id=int(parts[0].strip()),
                name=parts[1].strip(),
                description=parts[2].strip(),
                price=Decimal(parts[3].strip()),
                stock_quantity=int(parts[4].strip()),
                material=parts[5].strip()
            )
        except (ValueError, IndexError) as e:
            raise ValueError(f"Invalid number format in product string: {str(e)}")

    @classmethod
    def create_from_json(cls, json_str: str) -> 'Product':
        try:
            data = json.loads(json_str)
            return cls(
                product_id=data['product_id'],
                name=data['name'],
                description=data['description'],
                price=Decimal(str(data['price'])),
                stock_quantity=data['stock_quantity'],
                material=data['material']
            )
        except (json.JSONDecodeError, KeyError) as e:
            raise ValueError(f"Invalid JSON format: {str(e)}")

    def to_json(self) -> str:
        return json.dumps({
            'product_id': self._product_id,
            'name': self._name,
            'description': self._description,
            'price': str(self._price),
            'stock_quantity': self._stock_quantity,
            'material': self._material
        })

    def is_same_brief_product(self, other: BriefProduct) -> bool:
        return super().__eq__(other)

    def __eq__(self, other):
        if not isinstance(other, Product):
            return False
        return (super().__eq__(other) and
                self._description == other._description and
                self._stock_quantity == other._stock_quantity and
                self._material == other._material)

    def __hash__(self):
        return hash((super().__hash__(), self._description,
                     self._stock_quantity, self._material))

    def __str__(self):
        return (f"Product(product_id={self._product_id}, name='{self._name}', "
                f"description='{self._description}', price={self._price}, "
                f"stock_quantity={self._stock_quantity}, material='{self._material}')")
