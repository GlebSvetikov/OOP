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
https://mermaid.live/view#pako:eNrtWN1u2zYUfhWCQAEFVTxbTuJUwAoU6wbsYkOxtRiweRBokXaIyKJHUkndIEDaAbvtzS52tw17gSxrtqxds1eQ32ikJFuiJNvyugJFVyNWyKPzx8PvfJR8An2GCXShIN9EJPTJXYpGHI37IVCfCeKS-nSCQgkeCMKr0k8QDQESyX93rC7WVr3SByyUnAUB4XP1XOL6i2G98Rc0xOx4bpjOkmjecTKuWn1GJkxQyfhUW-Uzly-GHsJoIutC3sH4Q0ylmXJFuDLrTDtP3BC4COMs9feIki5dxl0iEQ2EmUlFuDKTTDvPxBC4OJ0ZGaTXGzdA_EP8Mr6afRdfxefxC3X9Iz7Xs9lTEP89O1OCF_F1_Ht8mag9Te048SXgo4HltNs2cBx92WlnsPiUSQLYkVqIxpNt5vLv4mlH27dv30wgCIoY1BJ9p7D94B5nOPJlLrKE5EiS0TQzyu9sK9vt1CsnMuIhyMFjBijBuQRvKzcrJJbfVx4KsC5AvLiOVLKd6RaDZbkVN7Div1gBjT02UEVTu2AJEgy3GhiNiPQOvdATB4xLL6BCWoc2CG0g9HxISYCzMeOY8NpaLkl8ku6I-OrrBsWJJlhtlje3seYDG0gmUeBRScbC3P5K2MgAyNJQGkkBY5P6XdCocwGmYhKgKXjwcapDQqwGef98r-D6q8LyhQJuAtr4MkXydfxs9m38fPYkPi93TdYwSes065raKC-V8EJ9f4uvl4TMGqe4Zj-g_mGCkEEkJQsrK6-W8wCFOCCKTPHSqt40yc_kQkuRFQmlDajwNBe-_xEKBFnnqphBRWQdUXJsgyrVZ16N-NXNHDI-NipUSp-Gk0gChUO0SistpUBHxKilGXthVVNRbWrpKGbWRjlqrI9QQJMe0abWCtsSJ8xbqdq6puoxpyXnhmoZHiGTdDhdEI6w3ma2KSMqtV-wwzLcEXUEsem8MmUO-Un19DPV3bpzr5I-vlCzZlyysziBm3LJ5tFqaESdKjqFrFxr2CZ5ANqUbrRRYygNph5d4FsNN8HLveIaXpHZ7vPoNRGbDczuXcIy-f7IOajTTl5lvTE_jhlWLf92EWTGBGUklev-jjXfFNb8UVPV7HH8l7o-mZ0BRWqXmrOSR6Q_a3lyo2eu1f5fE1Xq9t-YKrXRm0CVpQpm2oY0Y8ytNS6KsU03Fao027OipZyW0spIbo5eq9bBMmbMXqaNXSz5TzfSD5gwaW-Z59Uo_yU5q5u_W-xs_EbeLMKrAhsrZUk2hnZq1uhtTpHiseezcEj5GEnKQqsP73ACpiwCIuKk1Wr14QpSGhMh0IgM2MMWEodTIkI2j1u3qjRQg5VkvaMfDRq06OLQzuq1tlvfnUL_0SlU7ryfFe-fFZ6Rn696kW_abDVOyw2nxOtaLimuz8YDptDavJm0mUWOVvDv_2OboQ3HRJEExdCFJ1rch_KAjEkfumqIyRBFgezDfniqVFEk2efT0IeuVC1sQ86i0QF0h_pHDBum3rPf1OcqExR-yVhxCt0T-BC63a7T2u3sO7eczv6--tu14RS6Tq_V7bX395x2Z6-3297bPbXho8S-29rp3Or0nI7jdNv7O73e6T_0aPyE





