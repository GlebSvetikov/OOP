import json
import os
from Product import Product
from decimal import Decimal
from ProductRepository import ProductRepository
from ProductRepositoryStrategy import ProductRepFileStrategy
from DBAdapter import  ProductRepositoryAdapter

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

# Определяем путь к файлу JSON
strategy = JsonProductRepFileStrategy('products.json')


# Создание репозитория с использованием стратегии JSON
json_repository = ProductRepository(strategy)


new_product = Product.create_new_product(
    product_id= 3,
    name="Продук",
    description="Описание продукта",
    price=Decimal('19.99'),
    stock_quantity=100,
    material="Пластик",
    product_code="5890"
)
adapter = ProductRepositoryAdapter(json_repository)

adapter.update_by_id(1,"govno","mamy",Decimal("15000.00"),2000,"mazut","579762")
for product in json_repository.sort_by_field("stock_quantity",reverse=True):
    print (product)


# Отображение обновленного списка продуктов
print("\nUpdated products in JSON file:")
strategy.display()