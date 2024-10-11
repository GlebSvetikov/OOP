package org.jewelrystore;

import java.math.BigDecimal;
import java.util.regex.Pattern;

public class ProductValidator {
    private static final Pattern NAME_PATTERN = Pattern.compile("^[\\p{L}\\p{N}\\s.,'-]+$");
    private static final Pattern MATERIAL_PATTERN = Pattern.compile("^[\\p{L}\\s]+$");

    public static void validateProductId(int productId) {
        if (productId < 0) {
            throw new IllegalArgumentException("Product ID must be a non-negative integer.");
        }
    }

    public static void validateName(String name) {
        if (name == null || name.trim().isEmpty() || !NAME_PATTERN.matcher(name).matches()) {
            throw new IllegalArgumentException("Product name must contain only letters, numbers, spaces, and basic punctuation, and cannot be empty.");
        }
    }

    public static void validatePrice(BigDecimal price) {
        if (price == null || price.compareTo(BigDecimal.ZERO) <= 0) {
            throw new IllegalArgumentException("Price must be a positive number.");
        }
    }

    public static void validateStockQuantity(int stockQuantity) {
        if (stockQuantity < 0) {
            throw new IllegalArgumentException("Stock quantity must be a non-negative integer.");
        }
    }

    public static void validateMaterial(String material) {
        if (material == null || material.trim().isEmpty() || !MATERIAL_PATTERN.matcher(material).matches()) {
            throw new IllegalArgumentException("Material must contain only letters and spaces, and cannot be empty.");
        }
    }

    public static void validateDescription(String description) {
        if (description == null || description.trim().isEmpty()) {
            throw new IllegalArgumentException("Description cannot be empty.");
        }
        if (description.length() > 1000) {
            throw new IllegalArgumentException("Description must not exceed 1000 characters.");
        }
    }

    public static void validateProduct(Product product) {
        validateProductId(product.getProductId());
        validateName(product.getName());
        validatePrice(product.getPrice());
        validateStockQuantity(product.getStockQuantity());
        validateMaterial(product.getMaterial());
        validateDescription(product.getDescription());
    }
}