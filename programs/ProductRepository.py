from typing import List, Optional
from Product import Product


class ProductRepository:
    def __init__(self, strategy):
        self.products = []
        self.strategy = strategy  # Стратегия для чтения и записи данных

    def read_all(self) -> List[Product]:
        """Чтение всех продуктов с использованием стратегии."""
        data = self.strategy.read()
        return [Product.create_from_dict(item) for item in data]

    def write_all(self, products: List[Product]) -> None:
        """Запись всех продуктов с использованием стратегии."""
        data = [product.to_dict() for product in products]
        self.strategy.write(data)

    def get_by_id(self, product_id: int) -> Optional[Product]:
        """Получение продукта по ID."""
        for product in self.products:
            if product.product_id == product_id:
                return product
        return None

    def add_product(self, product: Product) -> None:
        products = self.read_all()
        if any(p.product_code == product.product_code for p in products):
            raise ValueError(f"Продукт с кодом {product.product_code} уже существует.")
        products = self.read_all()
        products.append(product)
        self.write_all(products)

    def replace_product_by_id(self, product_id: int, new_product: Product):
        """Заменить продукт по ID."""
        for i, product in enumerate(self.products):
            if product.product_id == product_id:
                self.products[i] = new_product
                new_product.product_id = product_id
                self.write_all(self.products)
                return
        raise ValueError(f"Продукт с ID {product_id} не найден.")

    def delete_product_by_id(self, product_id: int):
        """Удалить продукт по ID."""
        self.products = [product for product in self.products if product.product_id != product_id]
        self.write_all(self.products)

    def get_count(self) -> int:
        """Получить количество продуктов в репозитории."""
        return len(self.products)
