from decimal import Decimal
import json
import uuid

class BriefProduct:
    def __init__(self, product_id, name, price):
        self._product_id = product_id
        self._name = name
        self._price = price

    def get_product_id(self):
        return self._product_id

    def get_name(self):
        return self._name

    def get_price(self):
        return self._price

    def __str__(self):
        return f"BriefProduct(id={self._product_id}, name={self._name}, price={self._price})"


class Product(BriefProduct):
    def __init__(self, product_id, name, description, price, stock_quantity, material):
        super().__init__(product_id, name, price)
        self._unique_id = self._generate_unique_id()
        self._description = None
        self._stock_quantity = None
        self._material = None

        self.set_description(description)
        self.set_stock_quantity(stock_quantity)
        self.set_material(material)

    def _generate_unique_id(self):
        return uuid.uuid4().hex[:8]

    def _validate_and_set(self, field_name, value, validation_method):
        if validation_method(value):
            setattr(self, field_name, value)

    @staticmethod
    def validate_product_id(product_id):
        if isinstance(product_id, int) and product_id > 0:
            return True
        raise ValueError("Invalid product ID")

    @staticmethod
    def validate_name(name):
        if isinstance(name, str) and len(name) > 0:
            return True
        raise ValueError("Invalid name")

    @staticmethod
    def validate_description(description):
        if isinstance(description, str):
            return True
        raise ValueError("Invalid description")

    @staticmethod
    def validate_price(price):
        if isinstance(price, Decimal) and price >= 0:
            return True
        raise ValueError("Invalid price")

    @staticmethod
    def validate_stock_quantity(stock_quantity):
        if isinstance(stock_quantity, int) and stock_quantity >= 0:
            return True
        raise ValueError("Invalid stock quantity")

    @staticmethod
    def validate_material(material):
        if isinstance(material, str) and len(material) > 0:
            return True
        raise ValueError("Invalid material")

    def set_product_id(self, product_id):
        self._validate_and_set('_product_id', product_id, self.validate_product_id)

    def set_name(self, name):
        self._validate_and_set('_name', name, self.validate_name)

    def set_description(self, description):
        self._validate_and_set('_description', description, self.validate_description)

    def set_price(self, price):
        self._validate_and_set('_price', price, self.validate_price)

    def set_stock_quantity(self, stock_quantity):
        self._validate_and_set('_stock_quantity', stock_quantity, self.validate_stock_quantity)

    def set_material(self, material):
        self._validate_and_set('_material', material, self.validate_material)

    @classmethod
    def from_string(cls, data_str):
        data = json.loads(data_str)
        return cls(
            data['product_id'],
            data['name'],
            data['description'],
            Decimal(data['price']),
            data['stock_quantity'],
            data['material']
        )

    @classmethod
    def from_json(cls, json_str):
        return cls.from_string(json_str)

    def __str__(self):
        return f"Product(id={self.get_product_id()}, name={self.get_name()}, description={self._description}, " \
               f"price={self.get_price()}, stock_quantity={self._stock_quantity}, material={self._material}, " \
               f"unique_id={self._unique_id})"

    def brief(self):
        return super().__str__()

    def __eq__(self, other):
        if isinstance(other, Product):
            return self.get_product_id() == other.get_product_id() and self._unique_id == other._unique_id
        return False


# Пример использования
product = Product(1, "1234", "A beautiful gold ring", Decimal("399.99"), 1, "Gold")
print(product)
print(product.brief())

json_str = '{"product_id": 2, "name": "Silver Necklace", "description": "Elegant silver necklace", "price": "199.99", "stock_quantity": 30, "material": "Silver"}'
product_from_json = Product.from_json(json_str)
print(product_from_json)
