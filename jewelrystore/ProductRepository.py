from .AbstractProductRepository import AbstractProductRepository
from .SerializationStrategy import SerializationStrategy

class ProductRepository(AbstractProductRepository):
    def __init__(self, filename: str, strategy: SerializationStrategy):
        """Initialize ProductRepository with file name and serialization strategy."""
        super().__init__(filename, strategy)