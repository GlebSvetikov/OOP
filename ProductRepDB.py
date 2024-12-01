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