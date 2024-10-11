package org.jewelrystore;

import java.math.BigDecimal;
import java.util.Objects;

public class BriefProduct implements IProduct {
    protected int productId;
    protected String name;
    protected BigDecimal price;

    // Default constructor
    protected BriefProduct() {}

    // Constructor with parameters
    public BriefProduct(int productId, String name, BigDecimal price) {
        setProductId(productId);
        setName(name);
        setPrice(price);
    }

    @Override
    public int getProductId() {
        return productId;
    }

    public void setProductId(int productId) {
        ProductValidator.validateProductId(productId);
        this.productId = productId;
    }

    @Override
    public String getName() {
        return name;
    }

    public void setName(String name) {
        ProductValidator.validateName(name);
        this.name = name;
    }

    @Override
    public BigDecimal getPrice() {
        return price;
    }

    public void setPrice(BigDecimal price) {
        ProductValidator.validatePrice(price);
        this.price = price;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (!(o instanceof BriefProduct)) return false;
        BriefProduct that = (BriefProduct) o;
        return productId == that.productId &&
                Objects.equals(name, that.name) &&
                Objects.equals(price, that.price);
    }

    @Override
    public int hashCode() {
        return Objects.hash(productId, name, price);
    }

    @Override
    public String toString() {
        return "BriefProduct{" +
                "productId=" + productId +
                ", name='" + name + '\'' +
                ", price=" + price +
                '}';
    }
}