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
https://mermaid.live/edit#pako:eNrFWG1v2zYQ_iuCgAJya3vpEudFKAq0zQZs2LChHTBsyyDQ0tnmSpEqScXxuvz3HfUWiqJkF_uwfIjl493x7rlX-XOYigzCOEwZUeqWkq0k-R0P8O_Zs-DNWmlJUh1Up6Dqg-pL8NNagbwHGXyuqebv1SvSSLx-_UR9URYZ0RDNnte0x6EasmZwXNEiEc2lKg5-oEr_0Rrxp3UbybKOL2of4s7emcUqIRf3cCo3F5puDk82RDOPPz9LkZWpfg_Ft5TBB_RBw_ZwAkgSSNZBVFH2kiJqCB3pkTOqCkYONpxdwH4klPuCZejvBNdSMNYP2UJCIRTVQh7i4E1GCg3SOs1RMNlTnol9XGn5tXq2Y5KWUgLXiRJSJxsKLIsD9G-URcjMINxjeSFLHs08KWORdoRnDBIMr48MGdU-egYM_IruKex9dGNkBPdor-ewIFtIUvyyhah65mW-7tKkC4WbCw3CPeATE9k6j22qalImHkklm_eeMJpZwGNZfADtplB1UTRzcm1INYVT1HdGzWdnhM2X7iD9mJScfioRC2wfLfc8aB6Uzb4FnawPCc1aNnyMA9qH1zB9THiidsYZhphEHyumecCbTye_GsJTNtnqqiO8tGKPbCEJpnQhDtZCMFukNQ7rgZEU_CbPg-Vy6ZOq0-w0P1NR8n6uGiphrEXf7iyT-dTUaz-tLEe6wh5IHoEeUbcBt7E-Flr7fASVYaEPWLpUchI08pAHmDqwvZUUNg0CfqiaQNlHnOQw6GOFpClSbyGlOWE-TaYc3N6G9mGQ1Feq_rRO1say6WA7LQNUKmmhqeAD45QWWJafSsI11YeBQznCLClhp1uXYpvA0HDYd21hNjzeSJGbpkX5dvT4LyX46GFGJxQfSM56h1oMtSHNx2crdsB9mmQ9fLFZ5iopQFZ93oWwnWK-My00YdWJco5eaAnI_gv-NxPH0ztMziRor8lCY7Pdx0xjwLacijzHARQ1nzOHxQy_YzxNLR7hMiZO8TTl2jWq9mEe1AhUCPoxf5Nl36CdTV570EdssR6UCwJmNrnvDI-DTclTUwCO5TaTz3LTJbpu7Y4-5R562gz2x30CUgoZ5aAUhvoUP0e2LoNz7IXEu5phElSd3reiuaPas9EgNPUeOdVpbkETytQwMO3G6S4Hp2ibdN938WmOuRbNhquw2ZmCbv_-Li8Y5JhhxKRObzf-HtvJ8a19saHV-qd3g9W1Wtz9e7tvbfei9hv2r__RCMTrFlnXREHwbvj6cPsW48ihKrv-QKJcacKroWjx2BwMpxJuufjfbqUdaxz4xJqZ3h70xwMTqrfQ4_tFPTG0eY1M6CbBN7UEHnCTOb5J3b7tOZSt_QadsGsfW4b-w541svh8ye50ZFE9bZ_CNHkPrC6hHS1UsKd6FxCOeFt11f0y8OqfxcJ99YyDu5C2xajuwlqx9StAJTS66RpxeNDAsxNkMbYe_pEyq2QneoHf8CllEzXtV9ZbVG1fBm7U_A60zxu0mw5uZOrCUBiiLMCBaNaT9jJHeLF4PY16iT0h2AgZmB6E3UdI1HaSsiYMnYKs7TTTSow7o7PUcm5CfHQWueJuMNv3ddHLp0EIjUvDTHDAE758rsSroW4bMOruEAs7yDVfZ8moluXyhBh_oRYruEclhZPRdkb2QBwGbBjNCQBGtbgGNOPQnwPomeHvzb4ujxW-7mAjxRERhvMwB5kTmoVxWM2Su1DvsLLvwuoO2JCSaXPFI7KSUosPB56GsZYlzEMpyu0ujDeEKfxWd_TmZ9iWpSD8dyHsr2H8OXwI48XL1eXl8up8dXN1fnN2fn1xfTEPD0i_PL9anr9crc6uV5cXq8ubl4_z8O9Kxfny8vrq7Ozq5uzibPU1ij7-C4V7E-8

## Ссылка на диаграмму последовательности
https://mermaid.live/view#pako:eNrtWd1O20gUfhVrpEpBpCg4IYVcVKrKXu6PtuqutEKKTDwBq8aTtSewWYTU0u3ecFGpqrS92bKrfYFAkzYECK8wfqOeGdtJZjwODt0i7apcQOycc-ac73znm7HZRw1iY1RDAf65jb0GXnesLd_a2fAM-GlZPnUaTsvyqPE4wH767teW4-nvPiQe9YnrZnn96Hg22Ut_9z1ukcChxO-kv3tg21_ZDp0VOjbJir6OqeW4wawIsck4QmRx547B3rBLNgh_ZwPWZefw-wPr8qvwpcGuwqdw45yN2HvWF2YvIz8fN6jhb20WzFKpaJgm_1UpLURffkMoNsgu9gW6RWnl2s3W44Hu3r-_yCGGEH-A61X4PHzGhjOcuDE4TaAHz7_B7APrgT8Ysr4Bvn12JW4OwkM24rES_4njXQgTL_1X2p6dGZDJOK60-KJMGk0GbAg3LsNDiDSCKs5ZHz51J0EmznESYyBTkd6Bd5edwuUIPo8M-DOEi6lgkW9SjpTXW2E7kkpho4w8JEyPwaEHoAx4P1jX4EvytU9EIqe8pKgtRuHbTWgkMGMhT31RlwGW8JkR53MZHoUvUuXI-WxhWn9S9-rBNvFp3XUCWljIaugUllH-o4RRUFL4nA15j9mpDkBOSQ6bsDjhPUv4x1sx4C3lrQx_g5tnEDnuAvZsafpeC6C6E5i4t5xAV525eNzE4OWbOe0qUXdiqmiXjMdOQupPUWgXjHiQDQTSZHznE7vdoBtI0xqVaNuWZ7u4btl2IYsFi5Lc6ZgeE5vTQilsevi1QW88jFJS1zIA-s7F4SI8kqBUK3slOtDT8DvDQYX_kbWLE9zlDMe-GvQD8ErgT1npPSHVSK97E71OJa2LNT2bU12fGsa0RocvBJyXE7KmlpL8VZJ5hDrNTp3EchMU8ghOu2VbFE-b_nv68lZRQygk2jbGsjNLY1QpFSOQpl3C_SymckEdgiQdxeyR9wdVmfhO1xMeYC0G4nQyJ9coVGV8KsirUPOvphOnVwDrCR-8TxA0Dt08SobBPpNfKnE2O3XHzuaLNHCvE8pnQvAJyikOPlrAb0tBU9oWAD6taCepwyRaikDNLbyGdG5gF2wwU1nfQB0XIky26PwvRTnSvUxqKuqsFaMv6nzb6nwcHYyBsSM-bLwFfS4MIokzrR7PdWKcHf-WJfkHB-8lT7DzSPMu-H0WaT4W4hZLc-8GOq3CPeuEm-prZrgbK3PKH4IqKdpO0HKtTqLQCVCS1fXPRZpqYgKoiKgceOiSYCyqWavON0P_CHTyP3dV5n7XkW-FzzU269jFFM8zMLbwyKXHILB79Qbxmo6_Y1GHeBpplhszfpa_EuUcgmJyCr7npNC87JFKO9a7sH6O2jKc87zbGB9HBC55t8hU179sj_m3R3VI-dPg06kz6nDW-5C8c6kJmvna57rp5GoK5y4OhBJzkH_wAmhHrp2KG3IeNh3s5nyWThX6X6cj7GEq2N1boCUqoh0MYufYqIb2-e0NRLfxDihsDT7auGm1XfHoeACmVpuSRx2vgWrUb-Mi8kl7axvVmpYbwFWET_xvicSkZXk_ETJ9iWr76BdUM5fNpapZXTWXV0prq2a1WkQdVFsul5dW1qrmSqVUvre6XDLvHRTRryJAZYmbVdbKZrVsVirV8sFH7oC7lQ






