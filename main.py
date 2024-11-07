from decimal import Decimal
from typing import List
from jewelrystore import (
    Product,
    IProductRepository,
    JsonSerializationStrategy,
    YamlSerializationStrategy,
    ProductRepository,
    ProductRepositoryAdapter,
    Product_rep_DB
)


class RepositoryTester:
    @staticmethod
    def test_repository(repo: IProductRepository, repo_name: str) -> None:
        print(f"\n{'=' * 20} Testing {repo_name} {'=' * 20}")

        try:
            test_products = [
                Product.create_new_product(
                    name="Diamond Ring",
                    description="18K Gold Ring with Diamond",
                    price=Decimal("1999.99"),
                    stock_quantity=5,
                    material="Gold"
                ),
                Product.create_new_product(
                    name="Pearl Necklace",
                    description="Freshwater Pearl Necklace",
                    price=Decimal("599.99"),
                    stock_quantity=8,
                    material="Pearl"
                ),
                Product.create_new_product(
                    name="Ruby Earrings",
                    description="14K Gold Earrings with Rubies",
                    price=Decimal("899.99"),
                    stock_quantity=3,
                    material="Gold"
                )
            ]

            print("\nAdding products...")
            for product in test_products:
                repo.add_product(product)
                print(f"Added: {product.get_name()}")

            count = repo.get_count()
            print(f"\nTotal products in repository: {count}")

            print("\nTesting different sorting options:")

            sort_fields = ["name", "price", "material"]
            for field in sort_fields:
                print(f"\nProducts sorted by {field}:")
                products = repo.get_k_n_short_list(1, 10, field)
                for product in products:
                    if field == "price":
                        print(f"- {product.get_name()}: ${product.get_price()}")
                    else:
                        print(f"- {product.get_name()}")

            if products:
                first_product_id = products[0].get_product_id()
                print(f"\nRetrieving product with ID {first_product_id}:")
                product = repo.get_by_id(first_product_id)
                print(f"Found: {product}")

                print("\nUpdating product...")
                updated_product = Product.update_existing_product(
                    first_product_id,
                    product.get_name(),
                    product.description,
                    product.get_price() + Decimal("100.00"),
                    product.stock_quantity - 1,
                    product.material
                )
                repo.replace_product(first_product_id, updated_product)

                updated = repo.get_by_id(first_product_id)
                print(f"Updated product: {updated}")

                print("\nDeleting product...")
                repo.delete_product(first_product_id)
                print(f"Product with ID {first_product_id} deleted")

                count_after = repo.get_count()
                print(f"Products remaining: {count_after}")

        except Exception as e:
            print(f"Error in {repo_name}: {str(e)}")
            raise


def main():

    repositories = [
        (
            ProductRepositoryAdapter(
                ProductRepository("products.json", JsonSerializationStrategy())
            ),
            "JSON Repository"
        ),
        (
            ProductRepositoryAdapter(
                ProductRepository("products.yaml", YamlSerializationStrategy())
            ),
            "YAML Repository"
        ),
        (
            Product_rep_DB(),
            "Database Repository"
        )
    ]

    for repo, name in repositories:
        try:
            RepositoryTester.test_repository(repo, name)
        except Exception as e:
            print(f"Failed to test {name}: {e}")
            continue
        print(f"\nSuccessfully tested {name}")


if __name__ == "__main__":
    main()