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
        str product_code
    }

    PURCHASE {
        int purchase_id PK
        int customer_id FK
        int product_id FK
        date purchase_date
        int quantity
        decimal total_cost
    }
```

## Описание таблиц

**1. **CUSTOMER (Клиент)**:
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
![Untitled diagram-2024-12-07-202434](https://github.com/user-attachments/assets/f77930f5-d067-465f-867f-a4631903ea40)

## Ссылка на диаграмму последовательности
https://mermaid.live/view#pako:eNrtWd1O20gUfhVrpEpBpCg4IYVcVKrKXu6PtuqutEKKTDwBq8aTtSewWYTU0u3ecFGpqrS92bKrfYFAkzYECK8wfqOeGdtJZjwODt0i7apcQOycc-ac73znm7HZRw1iY1RDAf65jb0GXnesLd_a2fAM-GlZPnUaTsvyqPE4wH767teW4-nvPiQe9YnrZnn96Hg22Ut_9z1ukcChxO-kv3tg21_ZDp0VOjbJir6OqeW4wawIsck4QmRx547B3rBLNgh_ZwPWZefw-wPr8qvwpcGuwqdw45yN2HvWF2YvIz8fN6jhb20WzFKpaJgm_1UpLURffkMoNsgu9gW6RWnl2s3W44Hu3r-_yCGGEH-A61X4PHzGhjOcuDE4TaAHz7_B7APrgT8Ysr4Bvn12JW4OwkM24rES_4njXQgTL_1X2p6dGZDJOK60-KJMGk0GbAg3LsNDiDSCKs5ZHz51J0EmznESYyBTkd6Bd5edwuUIPo8M-DOEi6lgkW9SjpTXW2E7kkpho4w8JEyPwaEHoAx4P1jX4EvytU9EIqe8pKgtRuHbTWgkMGMhT31RlwGW8JkR53MZHoUvUuXI-WxhWn9S9-rBNvFp3XUCWljIaugUllH-o4RRUFL4nA15j9mpDkBOSQ6bsDjhPUv4x1sx4C3lrQx_g5tnEDnuAvZsafpeC6C6E5i4t5xAV525eNzE4OWbOe0qUXdiqmiXjMdOQupPUWgXjHiQDQTSZHznE7vdoBtI0xqVaNuWZ7u4btl2IYsFi5Lc6ZgeE5vTQilsevi1QW88jFJS1zIA-s7F4SI8kqBUK3slOtDT8DvDQYX_kbWLE9zlDMe-GvQD8ErgT1npPSHVSK97E71OJa2LNT2bU12fGsa0RocvBJyXE7KmlpL8VZJ5hDrNTp3EchMU8ghOu2VbFE-b_nv68lZRQygk2jbGsjNLY1QpFSOQpl3C_SymckEdgiQdxeyR9wdVmfhO1xMeYC0G4nQyJ9coVGV8KsirUPOvphOnVwDrCR-8TxA0Dt08SobBPpNfKnE2O3XHzuaLNHCvE8pnQvAJyikOPlrAb0tBU9oWAD6taCepwyRaikDNLbyGdG5gF2wwU1nfQB0XIky26PwvRTnSvUxqKuqsFaMv6nzb6nwcHYyBsSM-bLwFfS4MIokzrR7PdWKcHf-WJfkHB-8lT7DzSPMu-H0WaT4W4hZLc-8GOq3CPeuEm-prZrgbK3PKH4IqKdpO0HKtTqLQCVCS1fXPRZpqYgKoiKgceOiSYCyqWavON0P_CHTyP3dV5n7XkW-FzzU269jFFM8zMLbwyKXHILB79Qbxmo6_Y1GHeBpplhszfpa_EuUcgmJyCr7npNC87JFKO9a7sH6O2jKc87zbGB9HBC55t8hU179sj_m3R3VI-dPg06kz6nDW-5C8c6kJmvna57rp5GoK5y4OhBJzkH_wAmhHrp2KG3IeNh3s5nyWThX6X6cj7GEq2N1boCUqoh0MYufYqIb2-e0NRLfxDihsDT7auGm1XfHoeACmVpuSRx2vgWrUb-Mi8kl7axvVmpYbwFWET_xvicSkZXk_ETJ9iWr76BdUM5fNpapZXTWXV0prq2a1WkQdVFsul5dW1qrmSqVUvre6XDLvHRTRryJAZYmbVdbKZrVsVirV8sFH7oC7lQ






