import tkinter as tk
from tkinter import ttk


class ProductDetailsWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Product Details")
        self.geometry("400x500")

        # Делаем окно модальным
        self.transient(parent)
        self.grab_set()

        # Создаем и размещаем элементы интерфейса
        self.create_widgets()

        # Центрируем окно относительно родительского
        self.center_window()

    def create_widgets(self):
        # Основной контейнер
        main_frame = ttk.Frame(self, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Создаем и размещаем лейблы для всех полей
        fields = [
            ("ID:", "id_label"),
            ("Name:", "name_label"),
            ("Description:", "description_label"),
            ("Price:", "price_label"),
            ("Stock Quantity:", "quantity_label"),
            ("Material:", "material_label"),
            ("Product Code:", "product_code_label")
        ]

        for i, (text, attr_name) in enumerate(fields):
            ttk.Label(main_frame, text=text).grid(row=i, column=0, sticky=tk.W, pady=5)
            value_label = ttk.Label(main_frame, text="")
            value_label.grid(row=i, column=1, sticky=tk.W, pady=5, padx=5)
            setattr(self, attr_name, value_label)

        # Кнопка закрытия
        self.close_button = ttk.Button(main_frame, text="Close", command=self.destroy)
        self.close_button.grid(row=len(fields), column=0, columnspan=2, pady=20)

    def center_window(self):
        """Центрирование окна относительно родительского"""
        self.update_idletasks()
        parent = self.master
        x = parent.winfo_x() + (parent.winfo_width() - self.winfo_width()) // 2
        y = parent.winfo_y() + (parent.winfo_height() - self.winfo_height()) // 2
        self.geometry(f"+{x}+{y}")

    def display_product(self, product):
        """Отображение информации о продукте"""
        self.id_label.config(text=str(product.product_id))
        self.name_label.config(text=product.name)
        self.description_label.config(text=product.description)
        self.price_label.config(text=f"${float(product.price):.2f}")
        self.quantity_label.config(text=str(product.stock_quantity))
        self.material_label.config(text=product.material)
        self.product_code_label.config(text=product.product_code)