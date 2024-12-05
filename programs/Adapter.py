from ProductRepository import  ProductRepository

class ProductRepositoryAdapter:

    def __init__(self, product_repository: ProductRepository):
        self._product_repository = product_repository

    def get_k_n_short_list(self, k, n):
        return self._product_repository.get_k_n_short_list(k, n)

    def get_by_id(self, product_id):
        return self._product_repository.get_by_id(product_id)

    def delete_by_id(self, product_id):
        self._product_repository.product_delete_by_id(product_id)
        self._product_repository.write_data()

    def update_by_id(self, product_id, name, description, price, stock_quantity, material, product_code):
        self._product_repository.product_replace_by_id(product_id, name, description, price, stock_quantity, material, product_code)
        self._product_repository.write_data()

    def add(self, product):
        self._product_repository.add_product(product)
        self._product_repository.write_data()

    def get_count(self):
        return self._product_repository.get_count()
