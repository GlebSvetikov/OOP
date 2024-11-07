from typing import List, Optional
from decimal import Decimal
import psycopg2
from psycopg2.extras import RealDictCursor
from .IProductRepository import IProductRepository
from .Product import Product
from .BriefProduct import BriefProduct
from .PostgreSQLConnection import PostgreSQLConnection


class Product_rep_DB(IProductRepository):
    def __init__(self):
        """Initialize database repository."""
        self.db_connection = PostgreSQLConnection.get_instance()

    def get_by_id(self, id: int) -> Optional[Product]:
        """Get product by ID."""
        query = """
            SELECT product_id, name, description, price, stock_quantity, material
            FROM products
            WHERE product_id = %s
        """

        with self.db_connection.get_connection() as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cursor:
                cursor.execute(query, (id,))
                result = cursor.fetchone()

                if result:
                    return Product.update_existing_product(
                        result['product_id'],
                        result['name'],
                        result['description'],
                        Decimal(str(result['price'])),
                        result['stock_quantity'],
                        result['material']
                    )
        return None

    def get_k_n_short_list(self, k: int, n: int, sort_field: str) -> List[BriefProduct]:
        """Get k-th page of n products in brief format."""
        # Map Python field names to database column names
        field_mapping = {
            'id': 'product_id',
            'name': 'name',
            'price': 'price',
            'material': 'material',
            'stock': 'stock_quantity'
        }

        db_field = field_mapping.get(sort_field, 'product_id')

        query = f"""
            SELECT product_id, name, price
            FROM products
            ORDER BY {db_field}
            LIMIT %s OFFSET %s
        """

        with self.db_connection.get_connection() as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cursor:
                cursor.execute(query, (n, (k - 1) * n))
                results = cursor.fetchall()

                return [
                    BriefProduct(
                        row['product_id'],
                        row['name'],
                        Decimal(str(row['price']))
                    )
                    for row in results
                ]

    def add_product(self, product: Product) -> None:
        """Add a new product."""
        query = """
            INSERT INTO products (name, description, price, stock_quantity, material)
            VALUES (%s, %s, %s, %s, %s)
            RETURNING product_id
        """

        with self.db_connection.get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, (
                    product.get_name(),
                    product.description,
                    product.get_price(),
                    product.stock_quantity,
                    product.material
                ))
                conn.commit()

    def replace_product(self, id: int, new_product: Product) -> None:
        """Replace product with given ID."""
        query = """
            UPDATE products
            SET name = %s,
                description = %s,
                price = %s,
                stock_quantity = %s,
                material = %s
            WHERE product_id = %s
        """

        with self.db_connection.get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, (
                    new_product.get_name(),
                    new_product.description,
                    new_product.get_price(),
                    new_product.stock_quantity,
                    new_product.material,
                    id
                ))
                if cursor.rowcount == 0:
                    raise ValueError(f"Product with id {id} not found")
                conn.commit()

    def delete_product(self, id: int) -> None:
        """Delete product with given ID."""
        query = "DELETE FROM products WHERE product_id = %s"

        with self.db_connection.get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, (id,))
                if cursor.rowcount == 0:
                    raise ValueError(f"Product with id {id} not found")
                conn.commit()

    def get_count(self) -> int:
        """Get total number of products."""
        query = "SELECT COUNT(*) FROM products"

        with self.db_connection.get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query)
                return cursor.fetchone()[0]

    def sort_by_field(self, field: str) -> None:
        """
        Note: In database implementation, sorting is handled in get_k_n_short_list
        This method is kept for interface compatibility
        """
        pass  # Sorting is handled in get_k_n_short_list for database implementation