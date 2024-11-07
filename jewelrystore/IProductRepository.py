from abc import ABC, abstractmethod
from typing import List
from .Product import Product
from .BriefProduct import BriefProduct

class IProductRepository(ABC):
    @abstractmethod
    def get_by_id(self, id: int) -> Product:
        """Get product by ID."""
        pass

    @abstractmethod
    def get_k_n_short_list(self, k: int, n: int, sort_field: str) -> List[BriefProduct]:
        """Get k-th page of n products in brief format."""
        pass

    @abstractmethod
    def add_product(self, product: Product) -> None:
        """Add a new product."""
        pass

    @abstractmethod
    def replace_product(self, id: int, new_product: Product) -> None:
        """Replace product with given ID."""
        pass

    @abstractmethod
    def delete_product(self, id: int) -> None:
        """Delete product with given ID."""
        pass

    @abstractmethod
    def get_count(self) -> int:
        """Get total number of products."""
        pass

    @abstractmethod
    def sort_by_field(self, field: str) -> None:
        """Sort products by specified field."""
        pass
