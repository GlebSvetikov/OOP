import Adapter
from MainWindow import MainWindow
from ProductRepository import ProductRepository
from AddEditProductWindow import AddEditProductWindow
from ProductDetailsWindow import ProductDetailsWindow
from AddEditProductController import AddEditProductController
from ProductDetailsController import ProductDetailsController
from Observer import Observer

class MainController(Observer):
    def __init__(self, repository: Adapter):
        self.repository = repository
        self.main_window = MainWindow()
        self.repository.add_observer(self)
        self._current_sort_field = None
        self._current_sort_order = "ASC"

        # Привязка обработчиков событий
        self.main_window.set_add_command(self.handle_add)
        self.main_window.set_edit_command(self.handle_edit)
        self.main_window.set_delete_command(self.handle_delete)
        self.main_window.set_view_command(self.handle_view)
        self.main_window.set_sort_command(self.handle_sort)
        self.main_window.set_page_callback(self.handle_page_change)

        # Начальное обновление данных
        self.update()

    def run(self):
        """Запуск главного окна"""
        self.main_window.mainloop()

    def update(self):
        """Обновление данных в представлении (реализация Observer)"""
        self.handle_page_change(self.main_window.current_page)

    def handle_add(self):
        """Обработка добавления нового продукта"""
        add_window = AddEditProductWindow(self.main_window, is_edit=False)
        controller = AddEditProductController(add_window, self.repository)

    def handle_edit(self):
        """Обработка редактирования продукта"""
        selected_item = self.main_window.get_selected_item()
        if not selected_item:
            self.main_window.show_error("Please select a product to edit")
            return

        try:
            product_id = selected_item[0]  # Первый элемент - ID продукта
            product = self.repository.get_by_id(product_id)

            if not product:
                self.main_window.show_error(f"Product with ID {product_id} not found")
                return

            edit_window = AddEditProductWindow(self.main_window, is_edit=True)
            controller = AddEditProductController(edit_window, self.repository, product)
        except Exception as e:
            self.main_window.show_error(f"Error loading product: {str(e)}")

    def handle_delete(self):
        """Обработка удаления продукта"""
        selected_item = self.main_window.get_selected_item()
        if not selected_item:
            self.main_window.show_error("Please select a product to delete")
            return

        try:
            product_id = selected_item[0]
            product_name = selected_item[1]  # Имя продукта для сообщения

            if self.main_window.show_confirmation(f"Are you sure you want to delete product '{product_name}'?"):
                self.repository.product_delete_by_id(product_id)
                self.main_window.show_info("Product deleted successfully")
        except Exception as e:
            self.main_window.show_error(f"Error deleting product: {str(e)}")

    def handle_view(self):
        """Обработка просмотра деталей продукта"""
        selected_item = self.main_window.get_selected_item()
        if not selected_item:
            self.main_window.show_error("Please select a product to view")
            return

        try:
            product_id = selected_item[0]
            product = self.repository.get_by_id(product_id)

            if not product:
                self.main_window.show_error(f"Product with ID {product_id} not found")
                return

            details_window = ProductDetailsWindow(self.main_window)
            controller = ProductDetailsController(details_window, product)
        except Exception as e:
            self.main_window.show_error(f"Error loading product details: {str(e)}")

    def handle_sort(self, event):
        """Обработка сортировки"""
        sort_field = self.main_window.sort_combobox.get().lower()
        field_mapping = {
            'name': 'name',
            'price': 'price',
            'product code': 'product_code'
        }

        try:
            self._current_sort_field = field_mapping.get(sort_field.lower())
            # Обновление произойдет через вызов update
            self.update()
        except ValueError as e:
            self.main_window.show_error(f"Error sorting products: {str(e)}")

    def handle_page_change(self, page_number):
        """Обработка изменения страницы"""
        products = self.repository.get_k_n_short_list(
            self.main_window.items_per_page,
            page_number,
            sort_field=self._current_sort_field,
            sort_order=self._current_sort_order
        )
        total_items = self.repository.get_count()
        self.main_window.update_products(products, total_items)