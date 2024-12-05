import json
import os
from ProductRepository import ProductRepository
from ProductRepositoryStrategy import ProductRepFileStrategy

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

    def add(self, product):
        data = self.read()
        data.append(product.to_dict())
        self.write(data)

    def display(self):
        data = self.read()
        for item in data:
            print(item)

# Определяем путь к файлу JSON
strategy = JsonProductRepFileStrategy('products.json')

print("Current products in JSON file:")
strategy.display()

# Создание репозитория с использованием стратегии JSON
json_repository = ProductRepository(strategy)

print(json_repository.get_by_id(4))
print("\n12312312:")
print(json_repository.get_count())
for product in json_repository.sort_products("price", reverse=False):
    print(product)

print("\nFirst 5 products:")
for product in json_repository.get_k_n_short_list(2, 5):
    print(product)


# Отображение обновленного списка продуктов
print("\nUpdated products in JSON file:")
strategy.display()