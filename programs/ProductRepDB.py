from decimal import Decimal
from typing import List
from Product import Product
from DBConnection import DBConnection

class ProductRepDB:
    def __init__(self, host, user, password, database, port=3306):
        self.db = DBConnection(host, user, password, database, port).get_connection()

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
                    price=Decimal(result['price']),
                    stock_quantity=result['stock_quantity'],
                    material=result['material'],
                    product_code=result['product_code']
                )
            return None

    def get_k_n_short_list(self, k: int, n: int) -> List[Product]:
        offset = (n - 1) * k
        with self.db.cursor() as cursor:
            sql = "SELECT product_id, name, price, product_code FROM products LIMIT %s OFFSET %s"
            cursor.execute(sql, (k, offset))
            results = cursor.fetchall()
            return [
                Product(
                    product_id=row['product_id'],
                    name=row['name'],
                    price=Decimal(row['price']),
                    product_code=row['product_code']
                ) for row in results
            ]

    def add(self, product: Product) -> int:

        if self.is_product_code_unique(product.product_code):
            raise ValueError(f"Product with code {product.product_code} already exists.")

        with self.db.cursor() as cursor:
            sql = """
                INSERT INTO products (name, description, price, stock_quantity, material, product_code)
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            cursor.execute(sql, (
                product.name,
                product.description,
                str(product.price),
                product.stock_quantity,
                product.material,
                product.product_code
            ))
            self.db.commit()
            product.product_id = cursor.lastrowid
            return product.product_id

    def is_product_code_unique(self, product_code: str) -> bool:
        sql = "SELECT COUNT(*) FROM products WHERE product_code = %s"
        with self.db.cursor() as cursor:
            cursor.execute(sql, (product_code,))
            result = cursor.fetchone()
            return result['COUNT(*)'] > 0

    def update_by_id(self, product_id: int, product: Product) -> bool:
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
            return cursor.rowcount > 0

    def delete_by_id(self, product_id: int) -> bool:
        with self.db.cursor() as cursor:
            sql = "DELETE FROM products WHERE product_id = %s"
            cursor.execute(sql, (product_id,))
            self.db.commit()
            return cursor.rowcount > 0

    def get_count(self) -> int:
        with self.db.cursor() as cursor:
            sql = "SELECT COUNT(*) AS count FROM products"
            cursor.execute(sql)
            result = cursor.fetchone()
            return result['count'] if result else 0

    def close(self):
        self.db.close()