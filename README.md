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
(https://mermaid.live/view#pako:eNrtWd1u2zYUfhWBQAEHdQLbcpxaFwWGZpf7wYpuwGDAUCw6EaZInkQn84IAbbruJhcFigLrzZoNewEns1vHSZxXoN5oh5RkmxTlyOkaYEN74Vr0OYc83_nOR1I5QC3PwshAAf6xi90W3rTNbd_cbbga_OuYPrFbdsd0ifYkwH569AvTdtWjjzyX-J7jZHl9Z7uWt5_-7Rvc8QKbeH4v_dtnlvW5ZZNFoWOTrOibmJi2EyyKEJvMR4g-793T6Bt6RUfhr3RE-_QCPt_TPnsKX2r0OnwKAxd0Qt_RITd7Gfn5uEU0f3urUCmVilqlwj6qpZXoxy89gjVvD_sc4KIwuXG7-Vig1YcP7zOUIcRv4HodPg-f0fECJ2bMnGbwg-ufYPeeDiAAWNKhBs5Des0HR-ERnbBgSYCZ4yrEWY0n_yPtQM81WMs0sDi9yBzFEugYBq7CI4g0gTwu6BC-9WdBZs5JuCmWqVB_g3ufnsHjBL5PNPhvDA9z0SLfaULCyt5y44mQDJ1krESA9QQcBgDLiNWE9jU2J5v8lK_kjCUVlUYrfLUFxQR2rGTEFRKMKg3AhM-0eD1X4XH4IpWPuJ5tTJo_NN1msOP5pOnYASmsqGoqgRmtf5KwClIKn9MxqzI9UyHIaMlg4xanrGoJB1ktRqyorJjhLzB4DpHjMmDXarizBnzNcerPUGLO4vx9ue3ijuO9l6_tlLNExYmpopwy7jwBqN95nn0wYkEaCARK-9r3rG6LNJCiMjLPdkzXcnDTtKxCFgnuC6KnYnpMbMYKKbH5_lcGvXU3Cou6kQBQdqYOl-GxAKWc2StegYGC3hkOMvyPzT2c4C6ucOqrQD8ArwT-lJXaE5YaSfZgJtmpRatizbfmXNXnelGSEyhK-ILDeTUja2oqwV8mmesRu91rerHaBIU8etPtWCbB86b_nry8lcQQEon2janqLJIYWUl5C6Rpl3A_i6lMT8egSMcxe8T9QRImttMNuAMY8344m7XJDQJVnZ4L8grU8rOptOkVoHrK-u4D9Iwht4yQYbDPpJfMm61e07ay6SL02-uE8ZkQfIBw8pOPEvC7EtCUtAWATyfaSJrQiKakT0vrriacGuglHS0U1jeQxyUPk605_0tNjmQvk5qSOCu16JM437E4n0SnYiDshPUaq8CQ6QJfw7lSjpc6Ly6Of8eK_K2N95Nb7DLKvAd-H0WZT7i2xco8uIVMy3AvOt-m6poZ7tbCnPKHoNISLTvoOGYvEegEKMHq5kuRIpuYADIiMgceOV4w1dSsWZdqob84OPkvXdWl33Xkm-Fjdc0mdjDBy_SLxT1yqTHI636z5blt2981ie25CmEW6zK9x1_zdI5ALxkD3zFOKF72CKmdqF3oMEduGc553mtMDyMcl7wbZKrqnzbH_Juj1KPsJvh07oA6XvQuJG9bKoJmvvG5qTmZlsKhi-EgxRzl77sAqpFrn2KGjIZtGzs579GpRP_rbIQdTAa7fwesREW0i0HrbAsZ6IANNxDZwbsgsAZ8tXDb7Dr83ngIpmaXeI97bgsZxO_iIvK97vYOMtqmE8BThE_8h4nEpGO633ve_CMyDtBPyKjo-tqDir5eqVer62W9putF1EPGRnlNr5U2HtTrur5RqpcPi-hn7q-v1WrrVb1crVbq9Y16ubZ--A-Nt7wV)







