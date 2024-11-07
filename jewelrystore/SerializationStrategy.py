from abc import ABC, abstractmethod
from typing import List
from .Product import Product

class SerializationStrategy(ABC):
    @abstractmethod
    def read_from_file(self, filename: str) -> List[Product]:
        """Read products from file."""
        pass

    @abstractmethod
    def write_to_file(self, filename: str, products: List[Product]) -> None:
        """Write products to file."""
        pass