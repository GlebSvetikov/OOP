import pymysql
from decimal import Decimal
from Product import Product

class ProductRepDB:
    def __init__(self, host, user, password, database):
        self.connection = pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            cursorclass=pymysql.cursors.DictCursor
        )

    def get_by_id(self, product_id):
        with self.connection.cursor() as cursor:
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

    def get_k_n_short_list(self, k, n):
            offset = (n - 1) * k  # Вычисление смещения для пагинации
            with self.connection.cursor() as cursor:
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

    def add(self, product):
        with self.connection.cursor() as cursor:
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
            self.connection.commit()  # Подтверждаем изменения
            product.product_id = cursor.lastrowid  # Получаем ID добавленного продукта
            return product.product_id