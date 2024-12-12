from MainController import MainController
from ProductRepDB import ProductRepDB
from ProductRepository import ProductRepository
from Adapter import ProductRepositoryAdapter
from Product_rep_json import JsonProductRepFileStrategy


def main():
    # Выбор типа хранилища (можно вынести в конфиг или аргументы командной строки)
    storage_type = "filee"  # или "file" для файлового хранилища

    if storage_type == "file":
        # Инициализация репозитория с JSON стратегией
        strategy = JsonProductRepFileStrategy('products123.json')
        repository = ProductRepository(strategy)
        # Создание адаптера
        adapter = ProductRepositoryAdapter(repository)
    else:
        # Инициализация репозитория с базой данных
        repository = ProductRepDB(
            host='localhost',
            user='root',
            password='11062003',
            database='products',
            port=3306
        )
        # ProductRepDB уже реализует Observable, поэтому адаптер не нужен
        adapter = repository

    # Создание и запуск главного контроллера
    controller = MainController(adapter)
    controller.run()

if __name__ == "__main__":
    main()