from typing import List, Optional
from decimal import Decimal
from Product import Product
from BriefProduct import BriefProduct
from ProductRepositoryStrategy import ProductRepFileStrategy

class ProductRepository:
    def __init__(self, strategy: ProductRepFileStrategy):
        self._data = []
        self._strategy = strategy
        self._valid_sort_fields = {'name', 'price', 'product_code'}
        self.read_data()

    def write_data(self):
        """Записывает данные в хранилище через стратегию"""
        self._strategy.write(self._data)

    def read_data(self):
        """Читает данные из хранилища через стратегию"""
        self._data = self._strategy.read()

    def add_product(self, product: Product):
        """Добавляет новый продукт в репозиторий"""
        product_dict = product.to_dict()
        products = [Product.create_from_dict(prod) for prod in self._data]
        if not self.check_unique_code(product, products):
            raise ValueError(f"Product already exists.")
        self._data.append(product_dict)

    def check_unique_code(self, product, products):
        for product_data in products:
            if product_data == product and product_data.product_id != product.product_id:
                raise ValueError(f"Product already exists.")
        return True

    def get_by_id(self, product_id: int) -> Optional[Product]:
        """Получить продукт по ID"""
        for product in self._data:
            if product['product_id'] == product_id:
                return Product.create_from_dict(product)
        return None

    def get_k_n_short_list(self, k: int, n: int, sort_field: Optional[str] = None, sort_order: str = "ASC") -> List[
        BriefProduct]:
        # Проверка параметров сортировки
        if sort_field and sort_field not in self._valid_sort_fields:
            raise ValueError(f"Invalid sort field. Valid fields are: {', '.join(self._valid_sort_fields)}")
        if sort_order.upper() not in ("ASC", "DESC"):
            raise ValueError("Sort order must be either ASC or DESC")

        # Получаем копию данных для сортировки
        data = self._data.copy()

        # Применяем сортировку, если указано поле
        if sort_field:
            reverse = sort_order.upper() == "DESC"
            if sort_field == 'price':
                data.sort(key=lambda x: Decimal(x['price']), reverse=reverse)
            else:
                data.sort(key=lambda x: x[sort_field], reverse=reverse)

        # Применяем пагинацию
        start_index = (n - 1) * k
        end_index = start_index + k
        page_data = data[start_index:end_index]

        # Преобразуем в BriefProduct
        return [
            BriefProduct(
                product_id=product['product_id'],
                name=product['name'],
                price=Decimal(product['price']),
                product_code=product['product_code']
            )
            for product in page_data
        ]

    def sort_by_field(self, field: str, reverse: bool = False) -> List[Product]:
        """Сортирует продукты по указанному полю"""
        if field not in ['product_id', 'name', 'price', 'stock_quantity', 'material', 'product_code']:
            raise ValueError(f"Invalid field '{field}' for sorting.")
        self._data.sort(key=lambda x: x.get(field), reverse=reverse)
        return [Product.create_from_dict(product) for product in self._data]

    def product_replace_by_id(self, product_id: int, name=None, description=None, price=None,
                               stock_quantity=None, material=None, product_code=None):
        """Заменить данные продукта по ID"""
        product = self.get_by_id(product_id)
        if not product:
            raise ValueError(f"Product with ID {product_id} not found.")

        products = [Product.create_from_dict(prod) for prod in self._data]
        if not self.check_unique_code(product, products):
            raise ValueError(f"Product already exists.")

        if name:
            product.name = name
        if description:
            product.description = description
        if price:
            product.price = price
        if stock_quantity:
            product.stock_quantity = stock_quantity
        if material:
            product.material = material
        if product_code:
            product.product_code = product_code

        for i, p in enumerate(self._data):
            if p['product_id'] == product_id:
                self._data[i] = product.to_dict()
                break

    def product_delete_by_id(self, product_id: int):
        """Удалить продукт по ID"""
        product = self.get_by_id(product_id)
        if not product:
            raise ValueError(f"Product with ID {product_id} not found.")
        self._data = [p for p in self._data if p['product_id'] != product_id]

    def get_count(self) -> int:
        """Получить количество продуктов"""
        return len(self._data)

    def get_all_products(self) -> List[Product]:
        """Получить все продукты"""
        return [Product.create_from_dict(product) for product in self._data]