from typing import List, Optional
from .IProductRepository import IProductRepository
from .Product import Product
from .BriefProduct import BriefProduct
from .SerializationStrategy import SerializationStrategy


class AbstractProductRepository(IProductRepository):
    def __init__(self, filename: str, strategy: SerializationStrategy):
        self.products: List[Product] = []
        self.filename = filename
        self.serialization_strategy = strategy
        self.read_from_file()

    def read_from_file(self) -> None:
        """Read all products from file."""
        self.products = self.serialization_strategy.read_from_file(self.filename)

    def write_to_file(self) -> None:
        """Write all products to file."""
        self.serialization_strategy.write_to_file(self.filename, self.products)

    def get_by_id(self, id: int) -> Optional[Product]:
        """Get product by ID."""
        self.read_from_file()  # Ensure data is up to date
        return next((product for product in self.products if product.get_product_id() == id), None)

    def get_k_n_short_list(self, k: int, n: int, sort_field: str) -> List[BriefProduct]:
        """Get k-th page of n products in brief format."""
        self.read_from_file()  # Ensure data is up to date

        # Sort products if sort_field is specified
        if sort_field:
            self.sort_by_field(sort_field)

        # Calculate start and end indices
        start_idx = (k - 1) * n
        end_idx = start_idx + n

        # Convert selected products to BriefProduct
        selected_products = self.products[start_idx:end_idx]
        return [BriefProduct(
            product.get_product_id(),
            product.get_name(),
            product.get_price()
        ) for product in selected_products]

    def add_product(self, product: Product) -> None:
        """Add a new product."""
        self.read_from_file()  # Ensure data is up to date

        # Generate new ID
        new_id = self._generate_new_id()

        # Create new product with generated ID
        new_product = Product.update_existing_product(
            new_id,
            product.get_name(),
            product.description,
            product.get_price(),
            product.stock_quantity,
            product.material
        )

        self.products.append(new_product)
        self.write_to_file()

    def replace_product(self, id: int, new_product: Product) -> None:
        """Replace product with given ID."""
        self.read_from_file()  # Ensure data is up to date

        for i, product in enumerate(self.products):
            if product.get_product_id() == id:
                self.products[i] = new_product
                self.write_to_file()
                return

        raise ValueError(f"Product with id {id} not found")

    def delete_product(self, id: int) -> None:
        """Delete product with given ID."""
        self.read_from_file()  # Ensure data is up to date

        initial_length = len(self.products)
        self.products = [p for p in self.products if p.get_product_id() != id]

        if len(self.products) == initial_length:
            raise ValueError(f"Product with id {id} not found")

        self.write_to_file()

    def get_count(self) -> int:
        """Get total number of products."""
        self.read_from_file()  # Ensure data is up to date
        return len(self.products)

    def sort_by_field(self, field: str) -> None:
        """Sort products by specified field."""
        if not self.products:
            return

        def get_field_value(product: Product):
            match field:
                case "id":
                    return product.get_product_id()
                case "name":
                    return product.get_name()
                case "price":
                    return product.get_price()
                case "material":
                    return product.material
                case "stock":
                    return product.stock_quantity
                case _:
                    raise ValueError(f"Invalid sort field: {field}")

        self.products.sort(key=get_field_value)

    def _generate_new_id(self) -> int:
        """Generate new unique ID."""
        if not self.products:
            return 1
        return max(product.get_product_id() for product in self.products) + 1