from decimal import Decimal
import re
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .Product import Product


class ProductValidator:
    NAME_PATTERN = re.compile(r"^[\w\s.,'-]+$")
    MATERIAL_PATTERN = re.compile(r"^[A-Za-z\s]+$")

    @staticmethod
    def validate_product_id(product_id: int) -> None:
        if product_id < 0:
            raise ValueError("Product ID must be a non-negative integer.")

    @staticmethod
    def validate_name(name: str) -> None:
        if not name or not ProductValidator.NAME_PATTERN.match(name.strip()):
            raise ValueError(
                "Product name must contain only letters, numbers, spaces, and basic punctuation, and cannot be empty.")

    @staticmethod
    def validate_price(price: Decimal) -> None:
        if price is None or price <= Decimal('0'):
            raise ValueError("Price must be a positive number.")

    @staticmethod
    def validate_stock_quantity(stock_quantity: int) -> None:
        if stock_quantity < 0:
            raise ValueError("Stock quantity must be a non-negative integer.")

    @staticmethod
    def validate_material(material: str) -> None:
        if not material or not ProductValidator.MATERIAL_PATTERN.match(material.strip()):
            raise ValueError("Material must contain only letters and spaces, and cannot be empty.")

    @staticmethod
    def validate_description(description: str) -> None:
        if not description or not description.strip():
            raise ValueError("Description cannot be empty.")
        if len(description) > 1000:
            raise ValueError("Description must not exceed 1000 characters.")

    @staticmethod
    def validate_product(product: 'Product') -> None:
        ProductValidator.validate_product_id(product.get_product_id())
        ProductValidator.validate_name(product.get_name())
        ProductValidator.validate_price(product.get_price())
        ProductValidator.validate_stock_quantity(product.stock_quantity)
        ProductValidator.validate_material(product.material)
        ProductValidator.validate_description(product.description)