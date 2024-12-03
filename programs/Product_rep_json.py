import json
import os
from decimal import Decimal
from ProductRepository import ProductRepository
from ProductRepositoryStrategy import ProductRepFileStrategy
from Product import Product

class JsonProductRepFileStrategy(ProductRepFileStrategy):
    def __init__(self, file_path: str):
        self.file_path = file_path

    def read(self):
        if not os.path.exists(self.file_path):
            return []
        with open(self.file_path, 'r', encoding='utf-8') as file:
            return json.load(file)

    def write(self, data):
        with open(self.file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def display(self):
        data = self.read()
        for item in data:
            print(item)

strategy = JsonProductRepFileStrategy('products.json')

print("Current products in JSON file:")
strategy.display()

# Создание репозитория с использованием стратегии JSON
json_repository = ProductRepository(strategy)

# Создание нового продукта
new_product = Product.create_new_product(
    name="Продукт 1",
    description="Описание продукта",
    price=Decimal('19.99'),
    stock_quantity=100,
    material="Пластик",
    product_code="P123478900"
)

try:
    json_repository.add_product(new_product)
    print("Продукт добавлен.")
except ValueError as e:
    print(e)

# Отображение обновленного списка продуктов
print("\nUpdated products in JSON file:")
strategy.display()