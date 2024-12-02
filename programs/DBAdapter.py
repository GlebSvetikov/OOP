from decimal import Decimal
from ProductRepDB import ProductRepDB
from ProductRepository import ProductRepository
from Product import Product

class ProductRepDBAdapter(ProductRepository):
    def __init__(self, host, user, password, database, port):
        self._product_rep_db = ProductRepDB(host, user, password, database, port)

    def _read_all(self):
        self.products = self._product_rep_db.get_k_n_short_list(1, self._product_rep_db.get_count())

    def _write_all(self):
        pass

    def get_by_id(self, product_id: int):
        return self._product_rep_db.get_by_id(product_id)

    def get_k_n_short_list(self, k: int, n: int):
        return self._product_rep_db.get_k_n_short_list(k, n)

    def add_product(self, product: Product):
        return self._product_rep_db.add(product)

    def replace_product_by_id(self, product_id: int, new_product: Product):
        return self._product_rep_db.update_by_id(product_id, new_product)

    def delete_product_by_id(self, product_id: int):
        return self._product_rep_db.delete_by_id(product_id)

    def get_count(self):
        return self._product_rep_db.get_count()

    def close(self):
        self._product_rep_db.close()

if __name__ == "__main__":
    host = "localhost"
    user = "root"
    password = "11062003"
    database = "products"
    port = 3306

    db_adapter = ProductRepDBAdapter(host, user, password, database, port)

    new_product = Product.create_new_product(
        name="Серебряное кольцо",
        description="Кольцо из серебра высокого качества",
        price=Decimal("5000.00"),
        stock_quantity=20,
        material="Серебро",
        product_code="123456"
    )

    db_adapter.add_product(new_product)
    print(f"Всего продуктов (DB): {db_adapter.get_count()}")
    print("Список продуктов (DB):")
    for product in db_adapter.get_k_n_short_list(10, 1):
        print(product)

    db_adapter.close()