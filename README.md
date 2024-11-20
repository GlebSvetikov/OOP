## ER-диаграмма ювелирного магазина

```mermaid
erDiagram
    CUSTOMER ||--o{ PURCHASE : "совершает"
    PRODUCT ||--o{ PURCHASE : "приобретается в"

    CUSTOMER {
        int customer_id PK
        string last_name
        string first_name
        string middle_name
        date birth_date
    }

    PRODUCT {
        int product_id PK
        string name
        string description
        decimal price
        int stock_quantity
        string material
    }

    PURCHASE {
        int purchase_id PK
        int customer_id FK
        int product_id FK
        date purchase_date
        int quantity
        decimal total_cost
        int product_code
    }
```

## Описание таблиц

1. **CUSTOMER (Клиент)**:
   - customer_id: уникальный идентификатор клиента (первичный ключ)
   - last_name, first_name, middle_name: ФИО клиента
   - birth_date: дата рождения клиента

2. **PRODUCT (Товар)**:
   - product_id: первичный ключ
   - name: название товара
   - description: описание товара
   - price: цена товара
   - stock_quantity: количество товара на складе
   - material: материал изделия
   - product_code: уникальный номер товара (6 символов)

3. **PURCHASE (Покупка)**:
   - purchase_id: уникальный идентификатор покупки (первичный ключ)
   - customer_id: внешний ключ, связывающий с таблицей CUSTOMER
   - product_id: внешний ключ, связывающий с таблицей PRODUCT
   - purchase_date: дата покупки
   - quantity: количество приобретенного товара
   - total_cost: общая стоимость покупки

## Выбранная таблица для дальнейшей работы:
**Таблица PRODUCT - Товар**

## Диаграмма классов
```mermaid
classDiagram
    class IProduct {
        <<interface>>
        +getProductId() int
        +getName() String
        +getPrice() BigDecimal
    }

    class BriefProduct {
        #int productId
        #String name
        #BigDecimal price
        +BriefProduct()
        +BriefProduct(int, String, BigDecimal)
        +setProductId(int)
        +setName(String)
        +setPrice(BigDecimal)
        +toString() String
    }

    class Product {
        -String description
        -int stockQuantity
        -String material
        -Product(Builder)
        +getDescription() String
        +getStockQuantity() int
        +getMaterial() String
        +static createNewProduct(String, String, BigDecimal, int, String) Product
        +static updateExistingProduct(int, String, String, BigDecimal, int, String) Product
        +static createFromString(String) Product
        +static createFromJson(String) Product
        +toJson() String
        +toString() String
        +equals(Object) boolean
        +hashCode() int
        +isSameBriefProduct(BriefProduct) boolean
    }

    class ProductValidator {
        +static validateProductId(int)
        +static validateName(String)
        +static validatePrice(BigDecimal)
        +static validateStockQuantity(int)
        +static validateMaterial(String)
        +static validateProduct(Product)
    }

    IProduct <|.. BriefProduct : implements
    BriefProduct <|-- Product : extends
    Product ..> ProductValidator : uses
    BriefProduct ..> ProductValidator : uses
```

