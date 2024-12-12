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
            # Валидация и преобразование данных
            price = Decimal(data['price_entry'])
            quantity = int(data['quantity_entry'])

            if price < 0:
                raise ValueError("Price cannot be negative")
            if quantity < 0:
                raise ValueError("Quantity cannot be negative")
            if len(data['product_code_entry']) != 6 or not data['product_code_entry'].isdigit():
                raise ValueError("Product code must be 6 digits")

            # Создание или обновление продукта
            if self.product:  # Редактирование
                updated_product = Product.create_new_product(
                    product_id=self.product.product_id,
                    name=data['name_entry'],
                    description=data['description_entry'],
                    price=price,
                    stock_quantity=quantity,
                    material=data['material_entry'],
                    product_code=data['product_code_entry']
                )
                self.repository_adapter.update_by_id(self.product.product_id, updated_product)
            else:  # Создание нового
                new_product = Product.create_new_product(
                    product_id=None,  # ID будет назначен при сохранении
                    name=data['name_entry'],
                    description=data['description_entry'],
                    price=price,
                    stock_quantity=quantity,
                    material=data['material_entry'],
                    product_code=data['product_code_entry']
                )
                self.repository_adapter.add(new_product)

            self.view.destroy()  # Закрываем окно после успешного сохранения

        except (ValueError, InvalidOperation) as e:
            self.view.show_error(f"Validation error: {str(e)}")
        except Exception as e:
            self.view.show_error(f"Error saving product: {str(e)}")