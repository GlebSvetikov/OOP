from abc import ABC, abstractmethod
from decimal import Decimal


class IProduct(ABC):
    @abstractmethod
    def get_product_id(self) -> int:
        pass

    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_price(self) -> Decimal:
        pass