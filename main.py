import json
from decimal import Decimal
from itertools import product
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
        return (
                self.product_code == other.product_code)

    def brief(self):
        return f"BriefProduct(product_id={self.product_id}, name={self.name}, price={self.price})"

class Product(BriefProduct):
    def __init__(self, product_id: Optional[int] = None, name: str = "", description: str = "", price: Decimal = Decimal(0), stock_quantity: int = 0, material: str = "", product_code: str = ""):
        super().__init__(product_id, name, price, product_code)
        self._description = description
        self._stock_quantity = stock_quantity
        self._material = material

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value: str):
        if not isinstance(value, str) or not value:
            raise ValueError("Description must be a non-empty string.")
        self._description = value

    @property
    def stock_quantity(self):
        return self._stock_quantity

    @stock_quantity.setter
    def stock_quantity(self, value: int):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Stock quantity must be a non-negative integer.")
        self._stock_quantity = value

    @property
    def material(self):
        return self._material

    @material.setter
    def material(self, value: str):
        if not isinstance(value, str) or not value:
            raise ValueError("Material must be a non-empty string.")
        self._material = value

    @classmethod
    def create_new_product(cls, product_id: Optional[int] = None, name: str = "", description: str = "", price: Decimal = Decimal(0), stock_quantity: int = 0, material: str = "", product_code: str = ""):
        return cls(product_id=product_id, name=name, description=description, price=price, stock_quantity=stock_quantity, material=material, product_code=product_code)

    @classmethod
    def create_from_string(cls, product_string: str):
        parts = product_string.split(",")
        if len(parts) != 7:
            raise ValueError("Invalid product string format. Expected 7 comma-separated values.")
        try:
            return cls(
                product_id=int(parts[0].strip()) if parts[0].strip() else None,
                name=parts[1].strip(),
                description=parts[2].strip(),
                price=Decimal(parts[3].strip()),
                stock_quantity=int(parts[4].strip()),
                material=parts[5].strip(),
                product_code=parts[6].strip()
            )
        except ValueError as e:
            raise ValueError("Invalid number format in product string.") from e

    @classmethod
    def create_from_json(cls, json_string: str):
        data = json.loads(json_string)
        return cls(
            product_id=data.get('product_id'),
            name=data['name'],
            description=data['description'],
            price=Decimal(data['price']),
            stock_quantity=data['stock_quantity'],
            material=data['material'],
            product_code=data['product_code']
        )

    def to_json(self) -> str:
        return json.dumps({
            'product_id': self.product_id,
            'name': self.name,
            'description': self.description,
            'price': str(self.price),
            'stock_quantity': self.stock_quantity,
            'material': self.material,
            'product_code': self.product_code
        }, ensure_ascii=False)

    def __str__(self):
        return (f"Product(product_id={self.product_id}, name='{self.name}', description='{self.description}', "
                f"price={self.price}, stockQuantity={self.stock_quantity}, material='{self.material}', productCode='{self.product_code}')")

if __name__ == "__main__":
    try:
        product1 = Product.create_new_product(
            name="Gold ring",
            description="abc",
            price=Decimal("15000.00"),
            stock_quantity=1,
            material="Gold",
            product_code="123456"
        )
        product2 = Product.create_new_product(
            product_id=2,
            name="Silver ring",
            description="bdc",
            price=Decimal("10000.00"),
            stock_quantity=2,
            material="Silver",
            product_code="123456"
        )
        product1.price = Decimal("100000.00")
        print(product1 == product2)
        print(product1.brief())
        print(product1)
        print(product2.brief())
        print(product2)
    except ValueError as e:
        print("Error:", e)
