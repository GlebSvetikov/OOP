from ProductRepository import ProductRepository
from Observer import Observable


class ProductRepositoryAdapter(Observable):
    def __init__(self, product_repository: ProductRepository):
        super().__init__()
        self._product_repository = product_repository
        self._product_repository.read_data()  # Читаем начальные данные при создании адаптера

    def get_k_n_short_list(self, k, n, sort_field=None, sort_order="ASC"):
        return self._product_repository.get_k_n_short_list(k, n, sort_field, sort_order)

    def get_by_id(self, product_id):
        return self._product_repository.get_by_id(product_id)

    def delete_by_id(self, product_id):
        self._product_repository.product_delete_by_id(product_id)
        self._product_repository.write_data()  # Записываем изменения в файл
        self.notify_observers()

    def update_by_id(self, product_id, product):
        self._product_repository.product_replace_by_id(product_id,
                                                       name=product.name,
                                                       description=product.description,
                                                       price=product.price,
                                                       stock_quantity=product.stock_quantity,
                                                       material=product.material,
                                                       product_code=product.product_code
                                                       )
        self._product_repository.write_data()  # Записываем изменения в файл
        self.notify_observers()

    def add(self, product):
        # Генерируем новый ID перед добавлением
        if not self._product_repository._data:
            new_id = 1
        else:
            max_id = max(p.get('product_id', 0) for p in self._product_repository._data)
            new_id = max_id + 1

        # Устанавливаем ID для нового продукта
        product.product_id = new_id

        # Добавляем продукт через репозиторий
        self._product_repository.add_product(product)
        self._product_repository.write_data()
        self.notify_observers()

    def get_count(self):
        return self._product_repository.get_count()
