from typing import List
from .IProductRepository import IProductRepository
from .AbstractProductRepository import AbstractProductRepository
from .Product import Product
from .BriefProduct import BriefProduct

class ProductRepositoryAdapter(IProductRepository):
    def __init__(self, file_repository: AbstractProductRepository):
        """Initialize adapter with file repository."""
        self.file_repository = file_repository

    def get_by_id(self, id: int) -> Product:
        """Get product by ID."""
        return self.file_repository.get_by_id(id)

    def get_k_n_short_list(self, k: int, n: int, sort_field: str) -> List[BriefProduct]:
        """Get k-th page of n products in brief format."""
        return self.file_repository.get_k_n_short_list(k, n, sort_field)

    def add_product(self, product: Product) -> None:
        """Add a new product."""
        self.file_repository.add_product(product)

    def replace_product(self, id: int, new_product: Product) -> None:
        """Replace product with given ID."""
        self.file_repository.replace_product(id, new_product)

    def delete_product(self, id: int) -> None:
        """Delete product with given ID."""
        self.file_repository.delete_product(id)

    def get_count(self) -> int:
        """Get total number of products."""
        return self.file_repository.get_count()

    def sort_by_field(self, field: str) -> None:
        """Sort products by specified field."""
        self.file_repository.sort_by_field(field)