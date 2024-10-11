package org.jewelrystore;

import java.math.BigDecimal;

public interface IProduct {
    int getProductId();
    String getName();
    BigDecimal getPrice();
}