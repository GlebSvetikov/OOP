package org.jewelrystore;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import java.math.BigDecimal;
import java.util.Objects;
import java.io.IOException;



public class Product extends BriefProduct {
    private String description;
    private int stockQuantity;
    private String material;

    private static final ObjectMapper objectMapper = new ObjectMapper();

    private Product(Builder builder) {
        super(builder.productId, builder.name, builder.price);
        this.description = builder.description;
        this.stockQuantity = builder.stockQuantity;
        this.material = builder.material;
    }

    public String getDescription() {
        return description;
    }

    public int getStockQuantity() {
        return stockQuantity;
    }

    public String getMaterial() {
        return material;
    }

    public static Product createNewProduct(String name, String description, BigDecimal price, int stockQuantity, String material) {
        return new Builder()
                .name(name)
                .description(description)
                .price(price)
                .stockQuantity(stockQuantity)
                .material(material)
                .build();
    }

    public static Product updateExistingProduct(int productId, String name, String description, BigDecimal price, int stockQuantity, String material) {
        return new Builder()
                .productId(productId)
                .name(name)
                .description(description)
                .price(price)
                .stockQuantity(stockQuantity)
                .material(material)
                .build();
    }

    public static Product createFromString(String productString) {
        String[] parts = productString.split(",");
        if (parts.length != 6) {
            throw new IllegalArgumentException("Invalid product string format. Expected 6 comma-separated values.");
        }
        try {
            return new Builder()
                    .productId(Integer.parseInt(parts[0].trim()))
                    .name(parts[1].trim())
                    .description(parts[2].trim())
                    .price(new BigDecimal(parts[3].trim()))
                    .stockQuantity(Integer.parseInt(parts[4].trim()))
                    .material(parts[5].trim())
                    .build();
        } catch (NumberFormatException e) {
            throw new IllegalArgumentException("Invalid number format in product string.", e);
        }
    }

    public static Product createFromJson(String json) throws IOException {
        return objectMapper.readValue(json, Product.class);
    }

    public String toJson() throws JsonProcessingException {
        return objectMapper.writeValueAsString(this);
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (!(o instanceof Product)) return false;
        if (!super.equals(o)) return false;
        Product product = (Product) o;
        return stockQuantity == product.stockQuantity &&
                Objects.equals(description, product.description) &&
                Objects.equals(material, product.material);
    }

    @Override
    public int hashCode() {
        return Objects.hash(super.hashCode(), description, stockQuantity, material);
    }

    @Override
    public String toString() {
        return "Product{" +
                "productId=" + productId +
                ", name='" + name + '\'' +
                ", description='" + description + '\'' +
                ", price=" + price +
                ", stockQuantity=" + stockQuantity +
                ", material='" + material + '\'' +
                '}';
    }

    public boolean isSameBriefProduct(BriefProduct other) {
        return super.equals(other);
    }

    public static class Builder {
        private int productId;
        private String name;
        private String description;
        private BigDecimal price;
        private int stockQuantity;
        private String material;

        public Builder productId(int productId) {
            this.productId = productId;
            return this;
        }

        public Builder name(String name) {
            this.name = name;
            return this;
        }

        public Builder description(String description) {
            this.description = description;
            return this;
        }

        public Builder price(BigDecimal price) {
            this.price = price;
            return this;
        }

        public Builder stockQuantity(int stockQuantity) {
            this.stockQuantity = stockQuantity;
            return this;
        }

        public Builder material(String material) {
            this.material = material;
            return this;
        }

        public Product build() {
            Product product = new Product(this);
            ProductValidator.validateProduct(product);
            return product;
        }
    }
}