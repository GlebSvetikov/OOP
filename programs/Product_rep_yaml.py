import os
import yaml
from decimal import Decimal
from ProductRepository import ProductRepository
from ProductRepositoryStrategy import ProductRepFileStrategy
from Product import Product  # Импортируем класс Product

class YamlProductRepFileStrategy(ProductRepFileStrategy):
    def __init__(self, file_path: str):
        self.file_path = file_path

    def read(self):
        if not os.path.exists(self.file_path):
            return []
        with open(self.file_path, 'r', encoding='utf-8') as file:
            return yaml.safe_load(file) or []

    def write(self, data):
        with open(self.file_path, 'w', encoding='utf-8') as file:
            yaml.dump(data, file, allow_unicode=True, default_flow_style=False)

    def add(self, product):
        data = self.read()
        data.append(product.to_dict())
        self.write(data)

    def display(self):
        data = self.read()
        for item in data:
            print(item)

# Инициализация стратегии YAML
strategy = YamlProductRepFileStrategy('products.yaml')

# Чтение данных из файла и отображение их
print("Current products in YAML file:")
strategy.display()

# Создание репозитория с использованием стратегии YAML
yaml_repository = ProductRepository(strategy)

# Создание нового продукта
new_product = Product.create_new_product(
    product_id= 3,
    name="Продук",
    description="Описание продукта",
    price=Decimal('19.99'),
    stock_quantity=100,
    material="Пластик",
    product_code="5890000"
)


yaml_repository.add_product(new_product)

yaml_repository.write_data()

# Отображение обновленного списка продуктов
print("\nUpdated products in YAML file:")
strategy.display()
