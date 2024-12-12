from decimal import Decimal
from typing import List, Optional
from Product import Product
from Observer import Observable
from BriefProduct import BriefProduct
from pymysql import MySQLError
from DBConnection import DBConnection

class ProductRepDB(Observable):
    def __init__(self, host, user, password, database, port=3306):
        super().__init__()
        self.db = DBConnection(host, user, password, database, port).get_connection()
        self._valid_sort_fields = {'name', 'price', 'product_code'}

    def get_by_id(self, product_id: int) -> Product:
        with self.db.cursor() as cursor:
            sql = "SELECT * FROM products WHERE product_id = %s"
            cursor.execute(sql, (product_id,))
            result = cursor.fetchone()
            if result:
                return Product(
                    product_id=result['product_id'],
                    name=result['name'],
                    description=result['description'],
                    price=Decimal(str(result['price'])),
                    stock_quantity=result['stock_quantity'],
                    material=result['material'],
                    product_code=result['product_code']
                )
            return None

    def get_k_n_short_list(self, k: int, n: int, sort_field: Optional[str] = None, sort_order: str = "ASC") -> List[
        BriefProduct]:
        offset = (n - 1) * k

        # Проверка корректности параметров сортировки
        if sort_field and sort_field not in self._valid_sort_fields:
            raise ValueError(f"Invalid sort field. Valid fields are: {', '.join(self._valid_sort_fields)}")
        if sort_order.upper() not in ("ASC", "DESC"):
            raise ValueError("Sort order must be either ASC or DESC")

        with self.db.cursor() as cursor:
            sql = """
                SELECT product_id, name, price, product_code 
                FROM products 
                {order_clause}
                LIMIT %s OFFSET %s
            """
            order_clause = f"ORDER BY {sort_field} {sort_order}" if sort_field else ""
            sql = sql.format(order_clause=order_clause)

            cursor.execute(sql, (k, offset))
            results = cursor.fetchall()
            return [
                BriefProduct(
                    product_id=row['product_id'],
                    name=row['name'],
                    price=Decimal(str(row['price'])),
                    product_code=row['product_code']
                ) for row in results
            ]

    def add(self, product: Product):
        try:
            query = """
                INSERT INTO products (name, description, price, stock_quantity, material, product_code)
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            values = (product.name, product.description, str(product.price), product.stock_quantity,
                     product.material, product.product_code)

            with self.db.cursor() as cursor:
                cursor.execute(query, values)
                self.db.commit()
                # Получаем ID вставленной записи
                product.product_id = cursor.lastrowid
            self.notify_observers()
        except MySQLError as e:
            if e.args[0] == 1062:  # Duplicate entry
                raise ValueError(f"Product with code {product.product_code} already exists.")
            raise Exception("An unexpected error occurred while adding the product.")

    def update_by_id(self, product_id: int, product: Product) -> bool:
        try:
            with self.db.cursor() as cursor:
                sql = """
                    UPDATE products
                    SET name = %s, description = %s, price = %s, 
                        stock_quantity = %s, material = %s, product_code = %s
                    WHERE product_id = %s
                """
                cursor.execute(sql, (
                    product.name,
                    product.description,
                    str(product.price),
                    product.stock_quantity,
                    product.material,
                    product.product_code,
                    product_id
                ))
                self.db.commit()
                success = cursor.rowcount > 0
                if success:
                    self.notify_observers()
                return success
        except MySQLError as e:
            if e.args[0] == 1062:  # Duplicate entry
                raise ValueError(f"Product with code {product.product_code} already exists.")
            raise Exception("An unexpected error occurred while updating the product.")


    def product_delete_by_id(self, product_id: int) -> bool:
        with self.db.cursor() as cursor:
            sql = "DELETE FROM products WHERE product_id = %s"
            cursor.execute(sql, (product_id,))
            self.db.commit()
            success = cursor.rowcount > 0
            if success:
                self.notify_observers()
            return success

    def get_count(self) -> int:
        with self.db.cursor() as cursor:
            sql = "SELECT COUNT(*) AS count FROM products"
            cursor.execute(sql)
            result = cursor.fetchone()
            return result['count'] if result else 0

    def close(self):
        self.db.close()

    def sort_by_field(self, field: str, reverse: bool = False) -> List[Product]:
        """Сортирует продукты по указанному полю"""
        order = "DESC" if reverse else "ASC"
        with self.db.cursor() as cursor:
            sql = f"SELECT * FROM products ORDER BY {field} {order}"
            cursor.execute(sql)
            results = cursor.fetchall()
            products = [
                Product(
                    product_id=row['product_id'],
                    name=row['name'],
                    description=row['description'],
                    price=Decimal(str(row['price'])),
                    stock_quantity=row['stock_quantity'],
                    material=row['material'],
                    product_code=row['product_code']
                ) for row in results
            ]
            return products