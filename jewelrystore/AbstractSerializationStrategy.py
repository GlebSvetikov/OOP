from abc import abstractmethod
from typing import List, Any
import os
from decimal import Decimal
from .SerializationStrategy import SerializationStrategy
from .Product import Product


class AbstractSerializationStrategy(SerializationStrategy):
    def __init__(self):
        pass

    def read_from_file(self, filename: str) -> List[Product]:
        """Read products from file."""
        if not os.path.exists(filename):
            return []
        try:
            with open(filename, 'r') as file:
                data = self.read_data(file)
                if not data:
                    return []
                return [Product.update_existing_product(
                    item.get('_product_id', 0),
                    item.get('_name', ''),
                    item.get('_description', ''),
                    Decimal(str(item.get('_price', 0))),
                    item.get('_stock_quantity', 0),
                    item.get('_material', '')
                ) for item in data]
        except Exception as e:
            print(f"Error reading from file: {e}")
            return []

    def write_to_file(self, filename: str, products: List[Product]) -> None:
        """Write products to file."""
        try:
            data = [{
                '_product_id': product.get_product_id(),
                '_name': product.get_name(),
                '_description': product.description,
                '_price': str(product.get_price()),
                '_stock_quantity': product.stock_quantity,
                '_material': product.material
            } for product in products]

            with open(filename, 'w') as file:
                self.write_data(file, data)
        except Exception as e:
            print(f"Error writing to file: {e}")

    @abstractmethod
    def read_data(self, file) -> List[dict]:
        """Read data from file object."""
        pass

    @abstractmethod
    def write_data(self, file, data: List[dict]) -> None:
        """Write data to file object."""
        pass