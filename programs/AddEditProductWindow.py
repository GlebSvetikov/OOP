import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from decimal import Decimal


class AddEditProductWindow(tk.Toplevel):
    def __init__(self, parent, is_edit=False):
        super().__init__(parent)
        self.title("Edit Product" if is_edit else "Add Product")
        self.geometry("400x600")

        # Делаем окно модальным
        self.transient(parent)
        self.grab_set()

        self.is_edit = is_edit
        self.result = None

        # Создаем и размещаем элементы интерфейса
        self.create_widgets()

        # Центрируем окно относительно родительского
        self.center_window()

    def create_widgets(self):
        # Основной контейнер
        main_frame = ttk.Frame(self, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Создаем поля ввода
        fields = [
            ("Name:", "name_entry"),
            ("Description:", "description_entry", True),  # True означает многострочное поле
            ("Price:", "price_entry"),
            ("Stock Quantity:", "quantity_entry"),
            ("Material:", "material_entry"),
            ("Product Code:", "product_code_entry")
        ]

        self.entries = {}

        for i, field_info in enumerate(fields):
            label_text = field_info[0]
            entry_name = field_info[1]
            is_multiline = len(field_info) > 2 and field_info[2]

            ttk.Label(main_frame, text=label_text).grid(row=i * 2, column=0, sticky=tk.W, pady=(10, 0))

            if is_multiline:
                entry = tk.Text(main_frame, height=4, width=40)
                entry.grid(row=i * 2 + 1, column=0, columnspan=2, sticky=tk.EW, pady=(5, 10))
            else:
                entry = ttk.Entry(main_frame, width=40)
                entry.grid(row=i * 2 + 1, column=0, columnspan=2, sticky=tk.EW, pady=(5, 10))

            self.entries[entry_name] = entry

        # Фрейм для кнопок
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=len(fields) * 2, column=0, columnspan=2, pady=20)

        # Кнопки
        self.save_button = ttk.Button(button_frame, text="Save", command=self.on_save)
        self.save_button.pack(side=tk.LEFT, padx=5)

        self.cancel_button = ttk.Button(button_frame, text="Cancel", command=self.destroy)
        self.cancel_button.pack(side=tk.LEFT, padx=5)

    def center_window(self):
        """Центрирование окна относительно родительского"""
        self.update_idletasks()
        parent = self.master
        x = parent.winfo_x() + (parent.winfo_width() - self.winfo_width()) // 2
        y = parent.winfo_y() + (parent.winfo_height() - self.winfo_height()) // 2
        self.geometry(f"+{x}+{y}")

    def set_save_command(self, command):
        """Установка команды для кнопки сохранения"""
        self._save_command = command

    def get_product_data(self):
        """Получение данных из полей ввода"""
        data = {}
        for name, entry in self.entries.items():
            if isinstance(entry, tk.Text):
                data[name] = entry.get("1.0", tk.END).strip()
            else:
                data[name] = entry.get().strip()
        return data

    def set_product_data(self, product):
        """Заполнение полей данными продукта"""
        field_mapping = {
            'name_entry': product.name,
            'description_entry': product.description,
            'price_entry': str(product.price),
            'quantity_entry': str(product.stock_quantity),
            'material_entry': product.material,
            'product_code_entry': product.product_code
        }

        for entry_name, value in field_mapping.items():
            entry = self.entries[entry_name]
            if isinstance(entry, tk.Text):
                entry.delete("1.0", tk.END)
                entry.insert("1.0", value)
            else:
                entry.delete(0, tk.END)
                entry.insert(0, value)

    def on_save(self):
        """Обработка нажатия кнопки сохранения"""
        if hasattr(self, '_save_command'):
            self._save_command(self.get_product_data())

    def show_error(self, message):
        """Отображение сообщения об ошибке"""
        messagebox.showerror("Error", message, parent=self)

    def show_info(self, message):
        """Отображение информационного сообщения"""
        messagebox.showinfo("Information", message, parent=self)

    def show_warning(self, message):
        """Отображение предупреждения"""
        messagebox.showwarning("Warning", message, parent=self)