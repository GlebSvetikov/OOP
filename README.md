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
https://mermaid.live/view#pako:eNrtWG9v20Qc_ionS5Nc1a0yJ11SS50EKyAkmCbGQIIi62pf0lOdu3B3TheqSmVIvN0bXvAOEF-glBXKxspXcL4Rv_OfxHYc19k0MbFVqmOff__ud8_znO1jw-M-MRxDkq9DwjyyS_FA4OEeQ_A3wkJRj44wU-iBJGJx9GNMWfXoHc6U4EGwzOtzynx-tHjvEzLikiouJov33vH993yq6kKnJsui7xKFaSDrIqQmswiJxY0bKPoxeh5dTr-PLqOz6Bkc_4zO9NX0MYr-mZ7CwLPoKvojuojNHid-gngKicG-abdaFrJtfei01pKbd7kiiI-JiLtrFTI7L5ZPB9q4fXtdt9hBQziaaTI9Anfm_XWQ61JGleuaUgmsyGCSms5tNsAjCSWICgUrhFovrnMunpgFyCWfW6ZBs4nO3HLGyb0sfT5JuZBC2PzssO-7fB_6AQ02JQn6TWoJRz50wh0J7oeekmZ2YiHFFQ5cqshQLtZZzDwgyj10mSsPuFBuQKUyDy3ELCT1dZ-SwE_PufCJWNr1rKiPIMKX7wpK-veScr6qapReegf5VI4CPEEfPPgwMSLML6D4BwDNb4Coc4BPDJ3oIsHTVfRk-l30dPooOitjN4VtDOBm2K3M8hwGz-H_9-hqScoUvvnJewH1DtGeAcxG6fT3jIoFKOPkADM_IC6gwFy28OsFtcgBEfSAMGUhKl0C93fex4Ek10WpZMKYkiMLzfkA9eCRgoahFFk7dznLQhfKWVzSPhfDQptK5VM2ChUC_OI6q6yf9_GYZI0sJp65VLRTgpepUxRLLjSkwnuMAxoTS7uaNb4lAmf8W6RI0fRI0FLwgmkZG4wr2p_M1EGazaXBfJ3Jv4p6LVnzLK1PYFPgk2y6ZRX5GVj9BPituXsZM_kcrpqpSWe2EzZVk9WzVQgJbAG6hLQn1-qNbsYqQqOFYimOygDZn7h0Bm44XYqCfKJ7-cpfXMw-FeEr0rJmyJIw_2zmMWPrvFcWwSH3gdr_IxVMOV1GTLnpb6XxdZHGn7QeTb-N_objo-kpAuW60MIUPwn9VSmGKz1a1cd_ZXr4GbA_ezlaRRe1avynuljqX0kX165xq1HCIgEX7CFIKXWqYRkIzcoAZeACWY4Acknf84tUCp6t052Ay5mkFWMuFlSP5F_jTbf5a0Jn5VfcZhleHry7YK7IKrD1Y49G6qdXyPU461MxxIpyZg6JlHhA1pbLUWqxzx9uYnk4IZLxLFfVNJLgDarXm3sDrs3233iWDWj3dk95yT2lzK1fQL1Pc4-zT-veupvSqSJomVIwfB2pdLdQ3LnmdNE-JhnXCOrCxyIvFFqA3flCoZ1y2jcIHYZlDAkICPUNxzjWw3uGOiBDUC0HTn3Sx2EQv5GcgCkOFb8_YZ7hKGC8ZQgeDg4Mp68_VFhGkjr9lpuZjDD7gvP8peEcGw8Nx7a7m9t2C35a7XbXtttdy5gYzkZnu7e5dbPX3bK3Wt1271ane2IZ38Qh2pvbW91ep9fdbrVv2re6vZN_AZSTYFY






