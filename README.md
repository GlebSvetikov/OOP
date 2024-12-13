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

## Ссылка на диаграмму классов
https://mermaid.live/view#pako:eNrFWG1v2zYQ_iuCgALyYntN6qSxUBRomw3YsGFDO2DYlkGgpbPNhSJVkorjZfnvO1IvoSTaVrEPy4dYPt4d7557lR_DVGQQxmHKiFI3lGwkyW95gH8vXgTvVkpLkurAnoKqDuyX4KeVAnkPMnisqObvzRtSS7x9-0w9K4uMaIgmX1W0p6EasmJwWtEsEfWlKg5-oEr_0Rjxp3MbybKWL2oe4tbeicMqIRf3MJabC03X-2cboonHn5-lyMpUf4TiW8rgE_qgYbMfAZIEkrUQWcpOUkQNoSMdckZVwcjehbMN2I-Ecl-wDP2D4FoKxrohm0kohKJayH0cvMtIoUE6pzkKJjvKM7GLrZZf7bMbk7SUErhOlJA6WVNgWRygfwdZhMwMwh2WM1nyaOJJGYe0JTxjkGB4fWTIqPbRM2DgV3RPYeejGyMjuEd7PYcF2UCS4pcNRPaZl_mqTZM2FP1cqBHuAJ-YyFZ57FJVnTLxgVRyee8Jo5kDPJbFJ9D9FLIXRZNerg2ppnCK6s6o_myNcPnSLaR3Scnp5xKxwPbRcE-D-kG57BvQyWqf0Kxhw8c4oF14DdNdwhO1Nc4wxCS6s0zTgNefvfyqCc_Z5KqzR3ipZY9cIQmmdCEOVkIwV6QxDuuBkRT8Jk-D-Xzuk6rSbJyfqSh5N1cNlTDWoO92lqP5VNdrN60cR9rCHkiegB5RdwF3sT4VWvf8ACrDQh-wtKnUS9DIQx5g2oPtvaSwrhHwQ1UHyj3iJIdBHyskTZF6AynNCfNpMuXQ721oHwZJfa2qT-dkZSw7HuxeywCVSlpoKvjAOKUFluXnknBN9X7gUI4wS0rYeOtSbBMYGg67ti1MhsdrKXLTtCjfHDz-Swl-8DCjRxTvSc46h1oMtSHNx-cq7oH7PMk6-GKzzFVSgLR9vg9hM8V8Z1powuyJ6h2daQnI_gv-NxPH0ztMziRor8lCY7Pbx0xjwLacijzHARTVn5Meixl-p3jqWjzBZUw8xlOXa9uomodpUCFgEfRj_i7LvkE767z2oI_YYj2oPgiY2eS-NTwO1iVPTQH0LHeZfJabLtF26_7oU_1DT5vB_rhLQEohoxyUwlCP8fPA1mVwjr2QeFczTALb6X0rWn9UezYahKbaI491mhvQhDI1DEyzcfaXgzHajrrvu3icY32LJsNV2OxMQbt_f5cXDHLMMGJSp7Mbf4_t5PTWPltTu_7p7WB1tYu7f2_3re1e1H7D_vU_GoF43SDriigIPgxfH27eYxw52LLrDiTKlSbcDkWHx-VgOJVwy8X_bittWePAJ1bP9OagOx6YUJ2FHt8vqomhzWtkQtcJvqkl8ICbzOlN6uZ9x6Fs5TdoxK59ahn6D3vWgcXnS3anE4vquH0K0-QjsKqEtrRQwY7qbUA44u3WVfvTwJt_ZrP-u2cc3Ia0qUZ1G7oi9mcAK3Rw1TXi8KCBZyNkMbge_gN1ZmWPNAO_4ceUHSlqv7LOpur60nejYu8hO5u9dRcbI1IVhsIQZQEORLOeNHd5hI-CXmJPCNZCBqYHYfcRErWNUlZHoVWQNZ3mtJKDs9Rx7rQNw1nUE--Hsnld7_oxCKDxaJgHPey8wFpxO9Od-w86O0TCDXHF1xpyUMt8PiLCX6jFCe1JSQcIK-TkYwfCYbSGoTzi_xgtVrCehd4EQL8Me2futTms8FUHmyiOhzCchjnInNAsjEM7R25DvcWivg3tFbAmJdPmhidkJaUWn_Y8DWMtS5iGUpSbbRivCVP4rerm9U-wDUtB-O9CuF_D-DF8COPZq-ur-euLV9fXy8Vicb1YXkzDPZKvXl7OL6-XywWeXSwulk_T8G-r4GJ-eX6-PF9cvrx4eX79evnq6ulf1VISrg

## Ссылка на диаграмму последовательности
https://mermaid.live/view#pako:eNrtWd1O20gUfhVrpEpBpCg4IYVcVKrKXu6PtuqutEKKTDwBq8aTtSewWYTU0u3ecFGpqrS92bKrfYFAkzYECK8wfqOeGdtJZjwODt0i7apcQOycc-ac73znm7HZRw1iY1RDAf65jb0GXnesLd_a2fAM-GlZPnUaTsvyqPE4wH767teW4-nvPiQe9YnrZnn96Hg22Ut_9z1ukcChxO-kv3tg21_ZDp0VOjbJir6OqeW4wawIsck4QmRx547B3rBLNgh_ZwPWZefw-wPr8qvwpcGuwqdw45yN2HvWF2YvIz8fN6jhb20WzFKpaJgm_1UpLURffkMoNsgu9gW6RWnl2s3W44Hu3r-_yCGGEH-A61X4PHzGhjOcuDE4TaAHz7_B7APrgT8Ysr4Bvn12JW4OwkM24rES_4njXQgTL_1X2p6dGZDJOK60-KJMGk0GbAg3LsNDiDSCKs5ZHz51J0EmznESYyBTkd6Bd5edwuUIPo8M-DOEi6lgkW9SjpTXW2E7kkpho4w8JEyPwaEHoAx4P1jX4EvytU9EIqe8pKgtRuHbTWgkMGMhT31RlwGW8JkR53MZHoUvUuXI-WxhWn9S9-rBNvFp3XUCWljIaugUllH-o4RRUFL4nA15j9mpDkBOSQ6bsDjhPUv4x1sx4C3lrQx_g5tnEDnuAvZsafpeC6C6E5i4t5xAV525eNzE4OWbOe0qUXdiqmiXjMdOQupPUWgXjHiQDQTSZHznE7vdoBtI0xqVaNuWZ7u4btl2IYsFi5Lc6ZgeE5vTQilsevi1QW88jFJS1zIA-s7F4SI8kqBUK3slOtDT8DvDQYX_kbWLE9zlDMe-GvQD8ErgT1npPSHVSK97E71OJa2LNT2bU12fGsa0RocvBJyXE7KmlpL8VZJ5hDrNTp3EchMU8ghOu2VbFE-b_nv68lZRQygk2jbGsjNLY1QpFSOQpl3C_SymckEdgiQdxeyR9wdVmfhO1xMeYC0G4nQyJ9coVGV8KsirUPOvphOnVwDrCR-8TxA0Dt08SobBPpNfKnE2O3XHzuaLNHCvE8pnQvAJyikOPlrAb0tBU9oWAD6taCepwyRaikDNLbyGdG5gF2wwU1nfQB0XIky26PwvRTnSvUxqKuqsFaMv6nzb6nwcHYyBsSM-bLwFfS4MIokzrR7PdWKcHf-WJfkHB-8lT7DzSPMu-H0WaT4W4hZLc-8GOq3CPeuEm-prZrgbK3PKH4IqKdpO0HKtTqLQCVCS1fXPRZpqYgKoiKgceOiSYCyqWavON0P_CHTyP3dV5n7XkW-FzzU269jFFM8zMLbwyKXHILB79Qbxmo6_Y1GHeBpplhszfpa_EuUcgmJyCr7npNC87JFKO9a7sH6O2jKc87zbGB9HBC55t8hU179sj_m3R3VI-dPg06kz6nDW-5C8c6kJmvna57rp5GoK5y4OhBJzkH_wAmhHrp2KG3IeNh3s5nyWThX6X6cj7GEq2N1boCUqoh0MYufYqIb2-e0NRLfxDihsDT7auGm1XfHoeACmVpuSRx2vgWrUb-Mi8kl7axvVmpYbwFWET_xvicSkZXk_ETJ9iWr76BdUM5fNpapZXTWXV0prq2a1WkQdVFsul5dW1qrmSqVUvre6XDLvHRTRryJAZYmbVdbKZrVsVirV8sFH7oC7lQ






