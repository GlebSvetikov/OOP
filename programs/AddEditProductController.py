import Adapter
from AddEditProductWindow import AddEditProductWindow
from Product import Product
from decimal import Decimal, InvalidOperation


class AddEditProductController:
    def __init__(self, view: AddEditProductWindow, repository_adapter: Adapter, product=None):
        self.view = view
        self.repository_adapter = repository_adapter
        self.product = product

        # Если редактируем существующий продукт, заполняем поля
        if product:
            self.view.set_product_data(product)

        # Устанавливаем обработчик сохранения
        self.view.set_save_command(self.handle_save)

    def handle_save(self, data):
        """Обработка сохранения продукта"""
        try:
            updated_product = Product.create_new_product(
                product_id=self.product.product_id if self.product else None,
                name=data['name_entry'],
                description=data['description_entry'],
                price=Decimal(data['price_entry']),
                stock_quantity=int(data['quantity_entry']),
                material=data['material_entry'],
                product_code=data['product_code_entry']
            )

            if self.product:
                self.repository_adapter.update_by_id(self.product.product_id, updated_product)
            else:
                self.repository_adapter.add(updated_product)

            self.view.destroy()

        except ValueError as e:
            self.view.show_error(f"Validation error: {str(e)}")
        except Exception as e:
            self.view.show_error(f"Error saving product: {str(e)}")
